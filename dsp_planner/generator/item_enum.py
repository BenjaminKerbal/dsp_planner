from typing import Any

from ..types import BUILDING_TYPES, GameItem, ItemType
from .common import GAME_DATA_LOCATION
from .table_data_extraction import extract_data

_GameItemsType = dict[int, dict[str, Any]]


def generate_item_enums() -> None:
    data: _GameItemsType = extract_data("game_items")
    file_location = GAME_DATA_LOCATION / "items.py"
    file_location.unlink(missing_ok=True)
    all_game_items = sorted(
        (GameItem(item["name"], index, ItemType.from_string(item["type"])) for index, item in data.items()), reverse=True
    )
    building_items = tuple(item for item in all_game_items if item.type in BUILDING_TYPES)

    _INDENT = " " * 4
    with open(file_location, "w", encoding="utf-8") as f:
        f.write("# Auto-generated file. Do not edit.\n")
        f.write("from __future__ import annotations\n\n")
        f.write("from .types import GameItem, ItemType\n\n\n")

        # Add all items
        f.write("class AllItems:\n")
        for item in all_game_items:
            f.write(f"{_INDENT}{item.field_name} = {item.initialize_string}\n")

        # Add building items
        f.write("\n\nclass BuildingItems:\n")
        for item in building_items:
            f.write(f"{_INDENT}{item.field_name} = {item.initialize_string}\n")
