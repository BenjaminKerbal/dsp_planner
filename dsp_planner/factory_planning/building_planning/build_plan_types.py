from collections.abc import Iterable
from dataclasses import dataclass

from ...types import GameItem


@dataclass(slots=True, frozen=True)
class BuildingRecipeChange:
    building: GameItem
    new_inputs: set[GameItem]
    remove_inputs: set[GameItem]
    from_neighbors: set[GameItem]  # Inputs that a neighboring building hands over with a sorter

    def __str__(self) -> str:
        add_str = (
            "" if not self.new_inputs else "\n    Add: " + ", ".join(item.field_name for item in sorted(self.new_inputs))
        )
        remove_str = (
            ""
            if not self.remove_inputs
            else "\n    Remove: " + ", ".join(item.field_name for item in sorted(self.remove_inputs))
        )
        neighbor_str = (
            ""
            if not self.from_neighbors
            else "\n    From neighbor: " + ", ".join(item.field_name for item in sorted(self.from_neighbors))
        )
        return f"{self.building.name}:{add_str}{remove_str}{neighbor_str}"


class BuildingPlanResult:
    _building_recipe_changes: tuple[tuple[BuildingRecipeChange, ...], ...]

    def __init__(self, building_recipe_changes: tuple[tuple[BuildingRecipeChange, ...], ...]) -> None:
        self._building_recipe_changes = building_recipe_changes

    @property
    def total_feeds(self) -> int:
        """How many times an item has to be brought to a row from outside."""
        return sum(len(change.new_inputs) for row in self._building_recipe_changes for change in row)

    def __str__(self) -> str:
        def fmt_items(names: Iterable[str]) -> str:
            return ", ".join(sorted(names, key=str.lower)) or "—"

        lines: list[str] = [f"Items brought to the rows: {self.total_feeds}\n"]
        for step_idx, group in enumerate(self._building_recipe_changes, start=1):
            lines.append(f"Row {step_idx}")
            entries: list[tuple[str, str, str]] = []
            for change in group:
                added_names = [item.name for item in change.new_inputs]
                added_names += [f"{item.name} (from neighbor)" for item in change.from_neighbors]
                removed_names = [item.name for item in change.remove_inputs]
                entries.append((change.building.name, fmt_items(added_names), fmt_items(removed_names)))

            # Determine column widths
            col1_width = max(max([len(e[0]) for e in entries], default=-1), 25)
            col2_width = max(max([len(e[1]) for e in entries], default=-1), 40)
            col3_width = max(max([len(e[2]) for e in entries], default=-1), 40)

            # Build table
            border = f"  ┌{'─' * (col1_width + 2)}┬{'─' * (col2_width + 2)}┬{'─' * (col3_width + 2)}┐"
            header = f"  │ {'Building':<{col1_width}} │ {'+ Added':<{col2_width}} │ {'- Removed':<{col3_width}} │"
            divider = f"  ├{'─' * (col1_width + 2)}┼{'─' * (col2_width + 2)}┼{'─' * (col3_width + 2)}┤"
            footer = f"  └{'─' * (col1_width + 2)}┴{'─' * (col2_width + 2)}┴{'─' * (col3_width + 2)}┘\n"

            lines.append(border)
            lines.append(header)
            lines.append(divider)

            if len(entries) == 0:
                lines.append(f"  │ {'(no changes)':<{col1_width}} │ {'':<{col2_width}} │ {'':<{col3_width}} │")
            else:
                for bname, added, removed in entries:
                    lines.append(f"  │ {bname:<{col1_width}} │ {added:<{col2_width}} │ {removed:<{col3_width}} │")

            lines.append(footer)

        return "\n".join(lines).rstrip()
