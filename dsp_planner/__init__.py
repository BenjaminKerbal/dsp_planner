from warnings import warn

try:
    from .building_recipes import BuildingRecipes
    from .items import AllItems, BuildingItems

    __all__ = [
        "AllItems",
        "BuildingItems",
        "BuildingRecipes",
    ]
except ImportError:
    warn(
        "Failed to import generated data modules, have you run generate_data.py? If you are running that script now, this can be ignored."
    )
