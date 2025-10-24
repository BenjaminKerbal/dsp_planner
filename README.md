# Planning Module for [Dyson Sphere Program](https://store.steampowered.com/app/1366540/Dyson_Sphere_Program/)

This repo contains planning algorithms to help optimize factory building in `DSP`. Currently it includes:
- Building Order Planner: Optimize the order of building constructions to minimize changes in required items between consecutive buildings.


## Installation
Ensure that you have [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager installed. Then follow these steps:
1. run `uv venv`
2. Activate your environment:
    - Linux, Mac: `source .venv/bin/activate`
    - Windows: `.venv\Scripts\activate`
3. Install dependencies: `uv sync --group dev`

When the environment is set up correctly we then need to generate all building items and recipes from the game data. This is done automatically when you run the `generate_data.py` script in the root directory. This will fetch the html data from the [Dyson Sphere Program Wiki](https://dyson-sphere-program.fandom.com/wiki/Module:Recipe/Data) and parse it into python data structures.

## Planning Building Order
This planner aims to optimize the order of which to constructing buildings so that the items needed for each building recipe would change as little as possible between consecutive buildings.

To plan the building order, you can use the `plan_building_order` function from the `factory_planning` module. For example:

```python
from dsp_planner import BuildingItems as BI
from dsp_planner.factory_planning import plan_building_order

if __name__ == "__main__":
    buildings_in_plan: set[BI] = {
        BI.ARC_SMELTER,
        BI.MINING_MACHINE,
        BI.CHEMICAL_PLANT,
        BI.DEPOT_MK_I,
        BI.DEPOT_MK_II,
        BI.SPLITTER,
        BI.SATELLITE_SUBSTATION,
        BI.TESLA_TOWER,
        BI.WIRELESS_POWER_TOWER,
        BI.MATRIX_LAB,
        BI.STORAGE_TANK,
        BI.SPRAY_COATER,
        BI.ACCUMULATOR,
        BI.EM_RAIL_EJECTOR,
        BI.MINIATURE_PARTICLE_COLLIDER,
    }

    plan = plan_building_order(buildings_in_plan)
    print(plan)
```

