from warnings import warn

try:
    from .items import AllItems, BuildingItems
    from .recipes import Recipes

    __all__ = [
        "AllItems",
        "BuildingItems",
        "Recipes",
    ]
except ImportError:
    warn(
        "Failed to import generated data modules, have you run generate_data.py? If you are running that script now, this can be ignored."
    )
