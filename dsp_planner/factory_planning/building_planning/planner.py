import math
from datetime import timedelta
from typing import cast

from ortools.constraint_solver import pywrapcp, routing_enums_pb2
from ortools.constraint_solver.pywrapcp import Assignment
from ortools.constraint_solver.routing_parameters_pb2 import RoutingSearchParameters

from ...recipes import Recipes
from ...types import GameItem, Recipe
from .build_plan_types import BuildingPlanResult, BuildingRecipeChange


def plan_building_order(
    buildings: set[GameItem],
    max_row_length: int | None = None,
    search_time: timedelta = timedelta(seconds=5),
) -> BuildingPlanResult:
    """Order the buildings in as few rows as `max_row_length` allows (one row if not given)."""
    all_recipes_map: dict[GameItem, Recipe] = {
        recipe.output: recipe for recipe in vars(Recipes).values() if isinstance(recipe, Recipe)
    }
    recipes = tuple(all_recipes_map[b] for b in sorted(buildings))
    row_length = max_row_length or len(recipes)
    rows = math.ceil(len(recipes) / row_length)

    cost_matrix: list[list[int]] = _create_cost_matrix(recipes)
    manager = pywrapcp.RoutingIndexManager(len(recipes) + 1, rows, 0)  # +1 for the start and end of every row
    routing = pywrapcp.RoutingModel(manager)

    def cost_callback(from_index: int, to_index: int) -> int:
        """Returns the cost between the two nodes."""
        from_node = cast(int, manager.IndexToNode(from_index))
        to_node = cast(int, manager.IndexToNode(to_index))
        return cost_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(cost_callback)
    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Each arc counts as one, so a row with n buildings has n + 1 arcs including the one back to the row end
    routing.AddConstantDimension(1, row_length + 1, True, "row_length")

    search_parameters: RoutingSearchParameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    search_parameters.time_limit.FromTimedelta(search_time)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        return _create_building_plan(manager, routing, solution, recipes, rows)
    raise RuntimeError("No solution found!")


def _create_cost_matrix(buildings: tuple[Recipe, ...]) -> list[list[int]]:
    """Create a cost matrix between building recipes.

    Node 0 is the start and end of every row: starting a row costs adding all inputs of its first building,
    ending a row is free.
    """
    size = len(buildings) + 1
    matrix = [[0] * size for _ in range(size)]
    for i in range(1, size):
        matrix[0][i] = _row_start_cost(buildings[i - 1])
        for j in range(1, size):
            if i != j:
                matrix[i][j] = _cost_function(buildings[i - 1], buildings[j - 1])
    return matrix


def _cost_function(a: Recipe, b: Recipe) -> int:
    """
    A simple cost metric between two building recipes.
    Direction is from a to b.
    """
    # The output of a can be passed straight on to b, so it doesn't need to be added
    added_items = b.inputs - a.inputs - {a.output}
    removed_items = a.inputs - b.inputs
    return _change_cost(added_items, removed_items)


def _row_start_cost(first: Recipe) -> int:
    return _change_cost(added_items=first.inputs, removed_items=set())


def _change_cost(added_items: set[GameItem], removed_items: set[GameItem]) -> int:
    # Penalize more to add new items compared to removing items
    return 1 + 2 * len(added_items) + len(removed_items)


def _create_building_plan(
    manager: pywrapcp.RoutingIndexManager,
    routing: pywrapcp.RoutingModel,
    solution: Assignment,
    recipes: tuple[Recipe, ...],
    rows: int,
) -> BuildingPlanResult:
    def next_index(index: int) -> int:
        return cast(int, solution.Value(routing.NextVar(index)))

    print(f"Total cost: {solution.ObjectiveValue()}")
    result: list[tuple[BuildingRecipeChange, ...]] = []
    for row in range(rows):
        if not routing.IsVehicleUsed(solution, row):
            continue
        building_order: list[Recipe] = []
        index = routing.Start(row)  # Start index (row start)
        while True:
            if routing.IsEnd(index := next_index(index)):
                break
            building_order.append(recipes[manager.IndexToNode(index) - 1])  # -1 to account for the row start node

        building_recipe_changes: list[BuildingRecipeChange] = [
            BuildingRecipeChange(building_order[0].output, building_order[0].inputs, set())
        ]
        for i in range(1, len(building_order)):
            building_recipe_changes.append(BuildingRecipeChange.from_recipes(building_order[i - 1], building_order[i]))
        result.append(tuple(building_recipe_changes))

    return BuildingPlanResult(solution.ObjectiveValue(), tuple(result))
