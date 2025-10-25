from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


def string_transform(s: str) -> str:
    # fmt: off
    return (
            s.upper()
            .replace(" ", "_")
            .replace("-", "_")
            .replace(".", "_")
            .replace("(", "")
            .replace(")", "")
        )
    # fmt: on


class ItemType(Enum):
    COMPONENT = auto()
    TURRET = auto()
    PRODUCTION = auto()
    LOGISTICS = auto()
    RESOURCE = auto()
    MATRIX = auto()
    PRODUCT = auto()
    DARK_FOG = auto()
    MATERIAL = auto()
    DEFENSE = auto()

    @staticmethod
    def from_string(type_str: str) -> ItemType:
        return ItemType[type_str.upper()]


@dataclass(slots=True, frozen=True)
class GameItem:
    name: str
    id: int
    type: ItemType

    @property
    def field_name(self) -> str:
        return string_transform(self.name)

    @property
    def initialize_string(self) -> str:
        return f'{self.__class__.__name__}(name="{self.name}", id={self.id}, type=ItemType.{self.type.name})'

    def __lt__(self, other: GameItem) -> bool:
        return self.name < other.name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GameItem):
            return False
        return self.id == other.id


@dataclass(slots=True, frozen=True)
class BuildingRecipe:
    building: GameItem
    inputs: set[GameItem]

    @property
    def field_name(self) -> str:
        return self.building.field_name

    @property
    def initialize_string(self) -> str:
        return (
            f"{self.__class__.__name__}(building=AllItems.{self.building.field_name}, "
            f"inputs={"{"}{', '.join(f"AllItems.{item.field_name}" for item in self.inputs)},{"}"})"
        )

    def __lt__(self, other: BuildingRecipe) -> bool:
        return self.building.name < other.building.name


BUILDING_TYPES: set[ItemType] = {ItemType.LOGISTICS, ItemType.PRODUCTION, ItemType.DEFENSE}
