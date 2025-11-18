from subprocess import run
from typing import Any

from ..types import GameItem, Recipe
from .common import GAME_DATA_LOCATION
from .table_data_extraction import extract_data

_GameRecipeType = list[dict[str, Any]]


def generate_game_recipes() -> None:
    # Import here to ensure that items are generated first
    from ..items import AllItems

    file_location = GAME_DATA_LOCATION / "recipes.py"
    file_location.unlink(missing_ok=True)
    recipe_data: _GameRecipeType = extract_data("game_recipes")
    item_map = {item.id: item for item in vars(AllItems).values() if isinstance(item, GameItem)}

    def get_game_items(item_id: tuple[int, ...]) -> tuple[GameItem, ...]:
        # Assumes item_id is a tuple of two IDs, odd is item id, even is count
        return tuple(item_map[index] for i, index in enumerate(item_id) if i % 2 == 0)

    def create_recipe(data: dict[str, Any]) -> Recipe | None:
        if len(data.get("outputs", [])) != 2:
            return None  # Building recipes only have one output # TODO: Support multiple outputs

        output = get_game_items(data["outputs"])[0]
        return Recipe(
            output=output,
            inputs=set(get_game_items(data["inputs"])),
        )

    # Create all recipes
    all_recipes = tuple(r for recipe in recipe_data if (r := create_recipe(recipe)) is not None)
    _INDENT = " " * 4
    with open(file_location, "w", encoding="utf-8") as f:
        f.write("# Auto-generated file. Do not edit.\n")
        f.write("from __future__ import annotations\n\n")
        f.write(f"from .items import {AllItems.__name__}\n")
        f.write(f"from .types import {Recipe.__name__}\n\n\n")
        f.write("class Recipes:\n")

        # Add all items
        for item in sorted(all_recipes):
            f.write(f"{_INDENT}{item.field_name} = {item.initialize_string}\n")

    # Run code formatter
    run(["uvx", "ruff", "format", str(file_location)])
