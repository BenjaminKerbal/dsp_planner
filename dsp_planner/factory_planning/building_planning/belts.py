"""Which items are on the belts along a row of buildings, for a given building order."""

import math
from collections.abc import Sequence

from ...types import GameItem, Recipe
from .build_plan_types import BuildingRecipeChange


def count_feeds(row: Sequence[Recipe], belts: int) -> int:
    """How many times an item has to be brought to the row from outside."""
    return sum(len(change.new_inputs) for change in row_changes(row, belts))


def row_changes(row: Sequence[Recipe], belts: int) -> tuple[BuildingRecipeChange, ...]:
    """Which belts start and end at each building when every building can reach `belts` belts."""
    from_neighbors = [_from_neighbors(row, position) for position in range(len(row))]
    belt_needs = [
        frozenset(recipe.inputs - handed_over) for recipe, handed_over in zip(row, from_neighbors, strict=True)
    ]

    changes: list[BuildingRecipeChange] = []
    previous: frozenset[GameItem] = frozenset()
    for recipe, handed_over, on_belts in zip(row, from_neighbors, _belt_contents(belt_needs, belts), strict=True):
        changes.append(
            BuildingRecipeChange(
                building=recipe.output,
                new_inputs=set(on_belts - previous),
                remove_inputs=set(previous - on_belts),
                from_neighbors=handed_over,
            )
        )
        previous = on_belts
    return tuple(changes)


def _from_neighbors(row: Sequence[Recipe], position: int) -> set[GameItem]:
    """Inputs of the building at `position` that a neighboring building produces and hands over with a sorter."""
    neighbors = [row[index] for index in (position - 1, position + 1) if 0 <= index < len(row)]
    return row[position].inputs & {neighbor.output for neighbor in neighbors}


def _belt_contents(needs: Sequence[frozenset[GameItem]], belts: int) -> list[frozenset[GameItem]]:
    return _trim_unused_ends(needs, _keep_needed_soonest(needs, belts))


def _keep_needed_soonest(needs: Sequence[frozenset[GameItem]], belts: int) -> list[frozenset[GameItem]]:
    """Items on the belts at each building when an item only leaves the belts to make room for one needed sooner.

    For a fixed order this needs the fewest feeds.
    """
    on_belts: set[GameItem] = set()
    contents: list[frozenset[GameItem]] = []
    for needed, next_use in zip(needs, _next_uses(needs), strict=True):
        on_belts |= needed
        while len(on_belts) > belts:
            on_belts.remove(_needed_last(on_belts - needed, next_use))
        contents.append(frozenset(on_belts))
    return contents


def _next_uses(needs: Sequence[frozenset[GameItem]]) -> list[dict[GameItem, int]]:
    """For every building, the position of the next building further down the row that needs each item."""
    next_uses: list[dict[GameItem, int]] = []
    upcoming: dict[GameItem, int] = {}
    for position in reversed(range(len(needs))):
        next_uses.append(upcoming.copy())
        upcoming.update(dict.fromkeys(needs[position], position))
    next_uses.reverse()
    return next_uses


def _needed_last(candidates: set[GameItem], next_use: dict[GameItem, int]) -> GameItem:
    """The candidate that is needed furthest down the row, or not needed again at all."""
    return max(candidates, key=lambda item: next_use.get(item, math.inf))


def _trim_unused_ends(
    needs: Sequence[frozenset[GameItem]], contents: Sequence[frozenset[GameItem]]
) -> list[frozenset[GameItem]]:
    """End every belt at the last building that uses it."""
    trimmed: list[frozenset[GameItem]] = []
    still_needed: frozenset[GameItem] = frozenset()
    for needed, on_belts in zip(reversed(needs), reversed(contents), strict=True):
        still_needed = on_belts & (needed | still_needed)
        trimmed.append(still_needed)
    return trimmed[::-1]
