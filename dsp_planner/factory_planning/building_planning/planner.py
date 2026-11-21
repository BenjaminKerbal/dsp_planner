import math
import random
import time
from collections.abc import Iterable, Iterator
from datetime import timedelta

from ...recipes import Recipes
from ...types import GameItem, Recipe
from .belts import count_feeds, row_changes
from .build_plan_types import BuildingPlanResult

# Early in the search, a change that needs two more feeds is accepted about a third of the time
_START_TEMPERATURE = 2.0

_Layout = list[list[Recipe]]


def plan_building_order(
    buildings: set[GameItem],
    max_row_length: int | None = None,
    belts: int = 6,
    search_time: timedelta = timedelta(seconds=5),
) -> BuildingPlanResult:
    """Order the buildings so that items have to be brought to the rows as few times as possible.

    The buildings are split into as few rows as `max_row_length` allows (one row if not given), and every building
    can reach `belts` belts.
    """
    all_recipes_map: dict[GameItem, Recipe] = {
        recipe.output: recipe for recipe in vars(Recipes).values() if isinstance(recipe, Recipe)
    }
    recipes = tuple(all_recipes_map[b] for b in sorted(buildings))
    _check_enough_belts(recipes, belts)

    row_length = max_row_length or len(recipes)
    rows = math.ceil(len(recipes) / row_length)
    initial_layout = [list(recipes[row::rows]) for row in range(rows)]
    layout = _anneal(initial_layout, row_length, belts, search_time)
    return BuildingPlanResult(tuple(row_changes(row, belts) for row in layout))


def _check_enough_belts(recipes: Iterable[Recipe], belts: int) -> None:
    for recipe in recipes:
        if len(recipe.inputs) > belts:
            raise ValueError(
                f"{recipe.output.name} needs {len(recipe.inputs)} inputs, but a building can only reach {belts} belts"
            )


def _anneal(initial_layout: _Layout, max_row_length: int, belts: int, search_time: timedelta) -> _Layout:
    """Search for the layout with the fewest feeds using simulated annealing.

    Rows are never changed in place, so copying the outer list is enough to keep a layout.
    """
    rng = random.Random(0)
    layout = list(initial_layout)
    feeds = [count_feeds(row, belts) for row in layout]
    best_layout, best_feeds = list(layout), sum(feeds)
    for temperature in _cooling_schedule(search_time):
        changed_rows = _random_change(layout, max_row_length, rng)
        new_feeds = {index: count_feeds(row, belts) for index, row in changed_rows.items()}
        feed_change = sum(new_feeds[index] - feeds[index] for index in changed_rows)
        if not _accept(feed_change, temperature, rng):
            continue
        for index, row in changed_rows.items():
            layout[index] = row
            feeds[index] = new_feeds[index]
        if sum(feeds) < best_feeds:
            best_layout, best_feeds = list(layout), sum(feeds)
    return best_layout


def _cooling_schedule(search_time: timedelta) -> Iterator[float]:
    """Temperatures falling linearly from the start temperature towards zero over the search time."""
    start = time.monotonic()
    duration = search_time.total_seconds()
    elapsed = 0.0
    while elapsed < duration:
        yield _START_TEMPERATURE * (1 - elapsed / duration)
        elapsed = time.monotonic() - start


def _accept(feed_change: int, temperature: float, rng: random.Random) -> bool:
    """Always accept improvements, and worse layouts with a chance that shrinks as the temperature drops."""
    if feed_change <= 0:
        return True
    return rng.random() < math.exp(-feed_change / temperature)


def _random_change(layout: _Layout, max_row_length: int, rng: random.Random) -> dict[int, list[Recipe]]:
    """A small random change to the layout, as the new contents of the rows it touches."""
    first, second = rng.randrange(len(layout)), rng.randrange(len(layout))
    if first != second:
        new_first, new_second = _exchange_between_rows(layout[first], layout[second], max_row_length, rng)
        return {first: new_first, second: new_second}
    if len(layout[first]) < 2:
        return {}
    return {first: _reorder_row(layout[first], rng)}


def _exchange_between_rows(
    from_row: list[Recipe], to_row: list[Recipe], max_row_length: int, rng: random.Random
) -> tuple[list[Recipe], list[Recipe]]:
    """Move a building to the other row if it has room, or swap two buildings between the rows."""
    new_from, new_to = from_row.copy(), to_row.copy()
    taken = rng.randrange(len(new_from))
    if len(new_to) < max_row_length and rng.random() < 0.5:
        new_to.insert(rng.randrange(len(new_to) + 1), new_from.pop(taken))
    else:
        given = rng.randrange(len(new_to))
        new_from[taken], new_to[given] = new_to[given], new_from[taken]
    return new_from, new_to


def _reorder_row(row: list[Recipe], rng: random.Random) -> list[Recipe]:
    """Swap two buildings, move one of them, or reverse the stretch between them."""
    new_row = row.copy()
    first, last = sorted(rng.sample(range(len(row)), 2))
    match rng.randrange(3):
        case 0:
            new_row[first], new_row[last] = new_row[last], new_row[first]
        case 1:
            new_row.insert(last, new_row.pop(first))
        case _:
            new_row[first : last + 1] = reversed(new_row[first : last + 1])
    return new_row
