from __future__ import annotations

from dataclasses import dataclass

from ...types import BuildingRecipe, GameItem


@dataclass(slots=True, frozen=True)
class BuildingRecipeChange:
    building: GameItem
    new_inputs: set[GameItem]
    remove_inputs: set[GameItem]

    @staticmethod
    def from_recipes(old_recipe: BuildingRecipe, new_recipe: BuildingRecipe) -> BuildingRecipeChange:
        return BuildingRecipeChange(
            building=new_recipe.building,
            new_inputs=new_recipe.inputs - old_recipe.inputs,
            remove_inputs=old_recipe.inputs - new_recipe.inputs,
        )

    def __str__(self) -> str:
        add_str = (
            "" if not self.new_inputs else "\n    Add: " + ", ".join(item.field_name for item in sorted(self.new_inputs))
        )
        remove_str = (
            ""
            if not self.remove_inputs
            else "\n    Remove: " + ", ".join(item.field_name for item in sorted(self.remove_inputs))
        )
        return f"{self.building.name}:{add_str}{remove_str}"


class BuildingPlanResult:
    _total_cost: int
    _building_recipe_changes: tuple[tuple[BuildingRecipeChange, ...], ...]

    def __init__(self, total_cost: int, building_recipe_changes: tuple[tuple[BuildingRecipeChange, ...], ...]) -> None:
        self._total_cost = total_cost
        self._building_recipe_changes = building_recipe_changes

    def __str__(self) -> str:
        def fmt_items(items: set[GameItem]) -> str:
            if not items:
                return "—"
            return ", ".join(sorted((it.name for it in items), key=str.lower))

        lines: list[str] = []
        for step_idx, group in enumerate(self._building_recipe_changes, start=1):
            lines.append(f"Plan {step_idx}")
            entries: list[tuple[str, str, str]] = []
            for change in group:
                added = fmt_items(change.new_inputs)
                removed = fmt_items(change.remove_inputs)
                entries.append((change.building.name, added, removed))

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
