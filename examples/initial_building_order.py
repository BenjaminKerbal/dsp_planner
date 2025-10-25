from dsp_planner import BuildingItems as BI
from dsp_planner.factory_planning import plan_building_order

if __name__ == "__main__":
    buildings_in_plan: set[BI] = {
        BI.TESLA_TOWER,
        BI.WIRELESS_POWER_TOWER,
        BI.SATELLITE_SUBSTATION,
        BI.SOLAR_PANEL,
        BI.ACCUMULATOR,
        BI.GEOTHERMAL_POWER_STATION,
        BI.RAY_RECEIVER,
        BI.SPLITTER,
        BI.AUTOMATIC_PILER,
        BI.SPRAY_COATER,
        BI.DEPOT_MK_I,
        BI.DEPOT_MK_II,
        BI.STORAGE_TANK,
        BI.LOGISTICS_DISTRIBUTOR,
        BI.LOGISTICS_BOT,
        BI.PLANETARY_LOGISTICS_STATION,
        BI.LOGISTICS_BOT,
        BI.INTERSTELLAR_LOGISTICS_STATION,
        BI.INTERSTELLAR_LOGISTICS_VESSEL,
        BI.ORBITAL_COLLECTOR,
        BI.MINING_MACHINE,
        BI.ADVANCED_MINING_MACHINE,
        BI.WATER_PUMP,
        BI.OIL_EXTRACTOR,
        BI.FRACTIONATOR,
        BI.CHEMICAL_PLANT,
        BI.QUANTUM_CHEMICAL_PLANT,
        BI.MINIATURE_PARTICLE_COLLIDER,
        BI.ARC_SMELTER,
        BI.MATRIX_LAB,
        BI.EM_RAIL_EJECTOR,
    }

    plan = plan_building_order(buildings_in_plan)
    print(plan)
