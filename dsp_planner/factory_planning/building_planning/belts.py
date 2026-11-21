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
    changes: list[BuildingRecipeChange] = []
    previous: frozenset[GameItem] = frozenset()
    for recipe, on_belts in zip(row, _belt_contents(row, belts), strict=True):
        changes.append(
            BuildingRecipeChange(
                building=recipe.output,
                new_inputs=set(on_belts - previous - {recipe.output}),
                remove_inputs=set(previous - on_belts),
                output_to_belt=recipe.output in on_belts,
            )
        )
        previous = on_belts
    return tuple(changes)


def _belt_contents(row: Sequence[Recipe], belts: int) -> list[frozenset[GameItem]]:
    return _trim_unused_ends(row, _keep_needed_soonest(row, belts))


def _keep_needed_soonest(row: Sequence[Recipe], belts: int) -> list[frozenset[GameItem]]:
    """Items on the belts at each building when an item only leaves the belts to make room for one needed sooner.

    For a fixed order this needs the fewest feeds. A building's output goes on the belts when a later building in
    the row uses it.
    """
    on_belts: set[GameItem] = set()
    contents: list[frozenset[GameItem]] = []
    for recipe, next_use in zip(row, _next_uses(row), strict=True):
        on_belts |= recipe.inputs
        if recipe.output in next_use:
            on_belts.add(recipe.output)
        while len(on_belts) > belts:
            on_belts.remove(_needed_last(on_belts - recipe.inputs, next_use))
        contents.append(frozenset(on_belts))
    return contents


def _next_uses(row: Sequence[Recipe]) -> list[dict[GameItem, int]]:
    """For every building, the position of the next building further down the row that needs each item."""
    next_uses: list[dict[GameItem, int]] = []
    upcoming: dict[GameItem, int] = {}
    for position in reversed(range(len(row))):
        next_uses.append(upcoming.copy())
        upcoming.update(dict.fromkeys(row[position].inputs, position))
    next_uses.reverse()
    return next_uses


def _needed_last(candidates: set[GameItem], next_use: dict[GameItem, int]) -> GameItem:
    """The candidate that is needed furthest down the row, or not needed again at all."""
    return max(candidates, key=lambda item: next_use.get(item, math.inf))


def _trim_unused_ends(row: Sequence[Recipe], contents: Sequence[frozenset[GameItem]]) -> list[frozenset[GameItem]]:
    """End every belt at the last building that uses it."""
    trimmed: list[frozenset[GameItem]] = []
    still_needed: frozenset[GameItem] = frozenset()
    for recipe, on_belts in zip(reversed(row), reversed(contents), strict=True):
        still_needed = on_belts & (recipe.inputs | still_needed)
        trimmed.append(still_needed)
    return trimmed[::-1]
