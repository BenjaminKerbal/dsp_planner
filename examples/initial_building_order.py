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
