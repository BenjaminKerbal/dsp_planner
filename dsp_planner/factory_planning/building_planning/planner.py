from typing import cast

from ortools.constraint_solver import pywrapcp, routing_enums_pb2
from ortools.constraint_solver.pywrapcp import Assignment
from ortools.constraint_solver.routing_parameters_pb2 import RoutingSearchParameters

from ...recipes import Recipes
from ...types import GameItem, Recipe
from .build_plan_types import BuildingPlanResult, BuildingRecipeChange


def plan_building_order(buildings: set[GameItem], groups: int = 1) -> BuildingPlanResult:
    all_recipes_map: dict[GameItem, Recipe] = {
        recipe.output: recipe for recipe in vars(Recipes).values() if isinstance(recipe, Recipe)
    }
    recipes = tuple(all_recipes_map[b] for b in sorted(buildings))

    cost_matrix: list[list[int]] = _create_cost_matrix(recipes)
    manager = pywrapcp.RoutingIndexManager(len(recipes) + 1, groups, 0)  # +1 for depot (can be anywhere)
    routing = pywrapcp.RoutingModel(manager)

    def cost_callback(from_index: int, to_index: int) -> int:
        """Returns the cost between the two nodes."""
        from_node = cast(int, manager.IndexToNode(from_index))
        to_node = cast(int, manager.IndexToNode(to_index))
        return cost_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(cost_callback)
    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters: RoutingSearchParameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Balancing dimension to spread out the routes
    # num_nodes = len(recipes) + 1
    # routing.AddConstantDimension(
    #     1,  # each arc counts as 1 "hop"
    #     num_nodes,  # capacity (max hops per route)
    #     True,  # start cumul at 0
    #     "hops",
    # )
    # hops: RoutingDimension = routing.GetDimensionOrDie("hops")
    # hops.SetGlobalSpanCostCoefficient(100)  # increase to balance more aggressively

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        return _create_building_plan(manager, routing, solution, recipes, groups)
    raise RuntimeError("No solution found!")


def _create_cost_matrix(buildings: tuple[Recipe, ...]) -> list[list[int]]:
    """Create a cost matrix between building recipes."""
    # Add one extra size for the depot (which can be anywhere -> zero cost to all)
    size = len(buildings) + 1
    matrix = [[0] * size for _ in range(size)]
    for i in range(1, size):
        for j in range(1, size):
            if i != j:
                matrix[i][j] = _cost_function(buildings[i - 1], buildings[j - 1])
    return matrix


def _cost_function(a: Recipe, b: Recipe) -> int:
    """
    A simple cost metric between two building recipes.
    Direction is from a to b.
    """

    if a.output in b.inputs:
        return 0  # No cost if output of a is input to b

    if a.inputs == b.inputs:
        return 1  # Same inputs

    # Penalize more to add new items compared to removing items
    added_items = b.inputs - a.inputs
    removed_items = a.inputs - b.inputs
    return 1 + 2 * len(added_items) + len(removed_items)


def _create_building_plan(
    manager: pywrapcp.RoutingIndexManager,
    routing: pywrapcp.RoutingModel,
    solution: Assignment,
    recipes: tuple[Recipe, ...],
    groups: int,
) -> BuildingPlanResult:
    def next_index(index: int) -> int:
        return cast(int, solution.Value(routing.NextVar(index)))

    print(f"Total cost: {solution.ObjectiveValue()}")
    result: list[tuple[BuildingRecipeChange, ...]] = []
    for group_id in range(groups):
        if not routing.IsVehicleUsed(solution, group_id):
            continue
        building_order: list[Recipe] = []
        index = routing.Start(group_id)  # Start index (depot)
        while True:
            if routing.IsEnd(index := next_index(index)):
                break
            building_order.append(recipes[manager.IndexToNode(index) - 1])  # -1 to account for depot

        building_recipe_changes: list[BuildingRecipeChange] = [
            BuildingRecipeChange(building_order[0].output, building_order[0].inputs, set())
        ]
        for i in range(1, len(building_order)):
            building_recipe_changes.append(BuildingRecipeChange.from_recipes(building_order[i - 1], building_order[i]))
        result.append(tuple(building_recipe_changes))

    return BuildingPlanResult(solution.ObjectiveValue(), tuple(result))
