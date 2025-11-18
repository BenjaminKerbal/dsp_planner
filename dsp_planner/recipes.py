# Auto-generated file. Do not edit.
from __future__ import annotations

from .items import AllItems
from .types import Recipe


class Recipes:
    ACCUMULATOR = Recipe(
        output=AllItems.ACCUMULATOR,
        inputs={
            AllItems.CRYSTAL_SILICON,
            AllItems.IRON_INGOT,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    ADVANCED_MINING_MACHINE = Recipe(
        output=AllItems.ADVANCED_MINING_MACHINE,
        inputs={
            AllItems.GRATING_CRYSTAL,
            AllItems.QUANTUM_CHIP,
            AllItems.SUPER_MAGNETIC_RING,
            AllItems.FRAME_MATERIAL,
            AllItems.TITANIUM_ALLOY,
        },
    )
    ANNIHILATION_CONSTRAINT_SPHERE = Recipe(
        output=AllItems.ANNIHILATION_CONSTRAINT_SPHERE,
        inputs={
            AllItems.PARTICLE_CONTAINER,
            AllItems.PROCESSOR,
        },
    )
    ANTIMATTER_CAPSULE = Recipe(
        output=AllItems.ANTIMATTER_CAPSULE,
        inputs={
            AllItems.PARTICLE_CONTAINER,
            AllItems.ANTIMATTER,
            AllItems.PLASMA_CAPSULE,
            AllItems.HYDROGEN,
        },
    )
    ANTIMATTER_FUEL_ROD = Recipe(
        output=AllItems.ANTIMATTER_FUEL_ROD,
        inputs={
            AllItems.ANNIHILATION_CONSTRAINT_SPHERE,
            AllItems.ANTIMATTER,
            AllItems.TITANIUM_ALLOY,
            AllItems.HYDROGEN,
        },
    )
    ARC_SMELTER = Recipe(
        output=AllItems.ARC_SMELTER,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.STONE_BRICK,
            AllItems.CIRCUIT_BOARD,
            AllItems.MAGNETIC_COIL,
        },
    )
    ARTIFICIAL_STAR = Recipe(
        output=AllItems.ARTIFICIAL_STAR,
        inputs={
            AllItems.ANNIHILATION_CONSTRAINT_SPHERE,
            AllItems.QUANTUM_CHIP,
            AllItems.TITANIUM_ALLOY,
            AllItems.FRAME_MATERIAL,
        },
    )
    ASSEMBLING_MACHINE_MK_I = Recipe(
        output=AllItems.ASSEMBLING_MACHINE_MK_I,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
            AllItems.CIRCUIT_BOARD,
        },
    )
    ASSEMBLING_MACHINE_MK_II = Recipe(
        output=AllItems.ASSEMBLING_MACHINE_MK_II,
        inputs={
            AllItems.PROCESSOR,
            AllItems.GRAPHENE,
            AllItems.ASSEMBLING_MACHINE_MK_I,
        },
    )
    ASSEMBLING_MACHINE_MK_III = Recipe(
        output=AllItems.ASSEMBLING_MACHINE_MK_III,
        inputs={
            AllItems.QUANTUM_CHIP,
            AllItems.ASSEMBLING_MACHINE_MK_II,
            AllItems.PARTICLE_BROADBAND,
        },
    )
    ATTACK_DRONE = Recipe(
        output=AllItems.ATTACK_DRONE,
        inputs={
            AllItems.PARTICLE_CONTAINER,
            AllItems.PROTOTYPE,
            AllItems.ELECTROMAGNETIC_TURBINE,
            AllItems.PROCESSOR,
        },
    )
    AUTOMATIC_PILER = Recipe(
        output=AllItems.AUTOMATIC_PILER,
        inputs={
            AllItems.STEEL,
            AllItems.GEAR,
            AllItems.PROCESSOR,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    BATTLEFIELD_ANALYSIS_BASE = Recipe(
        output=AllItems.BATTLEFIELD_ANALYSIS_BASE,
        inputs={
            AllItems.STEEL,
            AllItems.ENGINE,
            AllItems.MICROCRYSTALLINE_COMPONENT,
            AllItems.CIRCUIT_BOARD,
        },
    )
    CARBON_NANOTUBE = Recipe(
        output=AllItems.CARBON_NANOTUBE,
        inputs={
            AllItems.TITANIUM_INGOT,
            AllItems.GRAPHENE,
        },
    )
    CARBON_NANOTUBE = Recipe(
        output=AllItems.CARBON_NANOTUBE,
        inputs={
            AllItems.STALAGMITE_CRYSTAL,
        },
    )
    CASIMIR_CRYSTAL = Recipe(
        output=AllItems.CASIMIR_CRYSTAL,
        inputs={
            AllItems.TITANIUM_CRYSTAL,
            AllItems.GRAPHENE,
            AllItems.HYDROGEN,
        },
    )
    CASIMIR_CRYSTAL = Recipe(
        output=AllItems.CASIMIR_CRYSTAL,
        inputs={
            AllItems.GRATING_CRYSTAL,
            AllItems.GRAPHENE,
            AllItems.HYDROGEN,
        },
    )
    CHEMICAL_PLANT = Recipe(
        output=AllItems.CHEMICAL_PLANT,
        inputs={
            AllItems.STEEL,
            AllItems.CIRCUIT_BOARD,
            AllItems.STONE_BRICK,
            AllItems.GLASS,
        },
    )
    CIRCUIT_BOARD = Recipe(
        output=AllItems.CIRCUIT_BOARD,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.COPPER_INGOT,
        },
    )
    COMBUSTIBLE_UNIT = Recipe(
        output=AllItems.COMBUSTIBLE_UNIT,
        inputs={
            AllItems.COAL,
        },
    )
    CONVEYOR_BELT_MK_I = Recipe(
        output=AllItems.CONVEYOR_BELT_MK_I,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
        },
    )
    CONVEYOR_BELT_MK_II = Recipe(
        output=AllItems.CONVEYOR_BELT_MK_II,
        inputs={
            AllItems.ELECTROMAGNETIC_TURBINE,
            AllItems.CONVEYOR_BELT_MK_I,
        },
    )
    CONVEYOR_BELT_MK_III = Recipe(
        output=AllItems.CONVEYOR_BELT_MK_III,
        inputs={
            AllItems.GRAPHENE,
            AllItems.SUPER_MAGNETIC_RING,
            AllItems.CONVEYOR_BELT_MK_II,
        },
    )
    COPPER_INGOT = Recipe(
        output=AllItems.COPPER_INGOT,
        inputs={
            AllItems.COPPER_ORE,
        },
    )
    CORVETTE = Recipe(
        output=AllItems.CORVETTE,
        inputs={
            AllItems.PARTICLE_CONTAINER,
            AllItems.PROCESSOR,
            AllItems.TITANIUM_ALLOY,
            AllItems.REINFORCED_THRUSTER,
        },
    )
    CRYSTAL_EXPLOSIVE_UNIT = Recipe(
        output=AllItems.CRYSTAL_EXPLOSIVE_UNIT,
        inputs={
            AllItems.CRYSTAL_SILICON,
            AllItems.EXPLOSIVE_UNIT,
            AllItems.CASIMIR_CRYSTAL,
        },
    )
    CRYSTAL_SHELL_SET = Recipe(
        output=AllItems.CRYSTAL_SHELL_SET,
        inputs={
            AllItems.CRYSTAL_EXPLOSIVE_UNIT,
            AllItems.TITANIUM_ALLOY,
            AllItems.HIGH_EXPLOSIVE_SHELL_SET,
        },
    )
    CRYSTAL_SILICON = Recipe(
        output=AllItems.CRYSTAL_SILICON,
        inputs={
            AllItems.FRACTAL_SILICON,
        },
    )
    CRYSTAL_SILICON = Recipe(
        output=AllItems.CRYSTAL_SILICON,
        inputs={
            AllItems.HIGH_PURITY_SILICON,
        },
    )
    DEPOT_MK_I = Recipe(
        output=AllItems.DEPOT_MK_I,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.STONE_BRICK,
        },
    )
    DEPOT_MK_II = Recipe(
        output=AllItems.DEPOT_MK_II,
        inputs={
            AllItems.STEEL,
            AllItems.STONE_BRICK,
        },
    )
    DESTROYER = Recipe(
        output=AllItems.DESTROYER,
        inputs={
            AllItems.PROCESSOR,
            AllItems.STRANGE_MATTER,
            AllItems.REINFORCED_THRUSTER,
            AllItems.FRAME_MATERIAL,
        },
    )
    DEUTERIUM = Recipe(
        output=AllItems.DEUTERIUM,
        inputs={
            AllItems.HYDROGEN,
        },
    )
    DEUTERON_FUEL_ROD = Recipe(
        output=AllItems.DEUTERON_FUEL_ROD,
        inputs={
            AllItems.DEUTERIUM,
            AllItems.TITANIUM_ALLOY,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    DIAMOND = Recipe(
        output=AllItems.DIAMOND,
        inputs={
            AllItems.ENERGETIC_GRAPHITE,
        },
    )
    DIAMOND = Recipe(
        output=AllItems.DIAMOND,
        inputs={
            AllItems.KIMBERLITE_ORE,
        },
    )
    DYSON_SPHERE_COMPONENT = Recipe(
        output=AllItems.DYSON_SPHERE_COMPONENT,
        inputs={
            AllItems.PROCESSOR,
            AllItems.SOLAR_SAIL,
            AllItems.FRAME_MATERIAL,
        },
    )
    EM_RAIL_EJECTOR = Recipe(
        output=AllItems.EM_RAIL_EJECTOR,
        inputs={
            AllItems.STEEL,
            AllItems.GEAR,
            AllItems.PROCESSOR,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    ELECTRIC_MOTOR = Recipe(
        output=AllItems.ELECTRIC_MOTOR,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
            AllItems.MAGNETIC_COIL,
        },
    )
    ELECTROMAGNETIC_MATRIX = Recipe(
        output=AllItems.ELECTROMAGNETIC_MATRIX,
        inputs={
            AllItems.CIRCUIT_BOARD,
            AllItems.MAGNETIC_COIL,
        },
    )
    ELECTROMAGNETIC_TURBINE = Recipe(
        output=AllItems.ELECTROMAGNETIC_TURBINE,
        inputs={
            AllItems.ELECTRIC_MOTOR,
            AllItems.MAGNETIC_COIL,
        },
    )
    ENERGETIC_GRAPHITE = Recipe(
        output=AllItems.ENERGETIC_GRAPHITE,
        inputs={
            AllItems.COAL,
        },
    )
    ENERGY_EXCHANGER = Recipe(
        output=AllItems.ENERGY_EXCHANGER,
        inputs={
            AllItems.PARTICLE_CONTAINER,
            AllItems.STEEL,
            AllItems.TITANIUM_ALLOY,
            AllItems.PROCESSOR,
        },
    )
    ENERGY_MATRIX = Recipe(
        output=AllItems.ENERGY_MATRIX,
        inputs={
            AllItems.ENERGETIC_GRAPHITE,
            AllItems.HYDROGEN,
        },
    )
    ENGINE = Recipe(
        output=AllItems.ENGINE,
        inputs={
            AllItems.COPPER_INGOT,
            AllItems.MAGNETIC_COIL,
        },
    )
    EXPLOSIVE_UNIT = Recipe(
        output=AllItems.EXPLOSIVE_UNIT,
        inputs={
            AllItems.PLASTIC,
            AllItems.COMBUSTIBLE_UNIT,
            AllItems.SULFURIC_ACID,
        },
    )
    FOUNDATION = Recipe(
        output=AllItems.FOUNDATION,
        inputs={
            AllItems.STEEL,
            AllItems.STONE_BRICK,
        },
    )
    FRACTIONATOR = Recipe(
        output=AllItems.FRACTIONATOR,
        inputs={
            AllItems.STEEL,
            AllItems.PROCESSOR,
            AllItems.STONE_BRICK,
            AllItems.GLASS,
        },
    )
    FRAME_MATERIAL = Recipe(
        output=AllItems.FRAME_MATERIAL,
        inputs={
            AllItems.HIGH_PURITY_SILICON,
            AllItems.CARBON_NANOTUBE,
            AllItems.TITANIUM_ALLOY,
        },
    )
    GAUSS_TURRET = Recipe(
        output=AllItems.GAUSS_TURRET,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
            AllItems.CIRCUIT_BOARD,
            AllItems.MAGNETIC_COIL,
        },
    )
    GEAR = Recipe(
        output=AllItems.GEAR,
        inputs={
            AllItems.IRON_INGOT,
        },
    )
    GEOTHERMAL_POWER_STATION = Recipe(
        output=AllItems.GEOTHERMAL_POWER_STATION,
        inputs={
            AllItems.PHOTON_COMBINER,
            AllItems.STEEL,
            AllItems.COPPER_INGOT,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    GLASS = Recipe(
        output=AllItems.GLASS,
        inputs={
            AllItems.STONE,
        },
    )
    GRAPHENE = Recipe(
        output=AllItems.GRAPHENE,
        inputs={
            AllItems.ENERGETIC_GRAPHITE,
            AllItems.SULFURIC_ACID,
        },
    )
    GRAVITON_LENS = Recipe(
        output=AllItems.GRAVITON_LENS,
        inputs={
            AllItems.DIAMOND,
            AllItems.STRANGE_MATTER,
        },
    )
    GRAVITY_MATRIX = Recipe(
        output=AllItems.GRAVITY_MATRIX,
        inputs={
            AllItems.QUANTUM_CHIP,
            AllItems.GRAVITON_LENS,
        },
    )
    GRAVITY_MISSILE_SET = Recipe(
        output=AllItems.GRAVITY_MISSILE_SET,
        inputs={
            AllItems.CRYSTAL_EXPLOSIVE_UNIT,
            AllItems.STRANGE_MATTER,
            AllItems.SUPERSONIC_MISSILE_SET,
        },
    )
    HIGH_EXPLOSIVE_SHELL_SET = Recipe(
        output=AllItems.HIGH_EXPLOSIVE_SHELL_SET,
        inputs={
            AllItems.EXPLOSIVE_UNIT,
            AllItems.SHELL_SET,
            AllItems.TITANIUM_INGOT,
        },
    )
    HIGH_PURITY_SILICON = Recipe(
        output=AllItems.HIGH_PURITY_SILICON,
        inputs={
            AllItems.SILICON_ORE,
        },
    )
    HYDROGEN_FUEL_ROD = Recipe(
        output=AllItems.HYDROGEN_FUEL_ROD,
        inputs={
            AllItems.TITANIUM_INGOT,
            AllItems.HYDROGEN,
        },
    )
    IMPLOSION_CANNON = Recipe(
        output=AllItems.IMPLOSION_CANNON,
        inputs={
            AllItems.ELECTRIC_MOTOR,
            AllItems.STEEL,
            AllItems.CIRCUIT_BOARD,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    INFORMATION_MATRIX = Recipe(
        output=AllItems.INFORMATION_MATRIX,
        inputs={
            AllItems.PROCESSOR,
            AllItems.PARTICLE_BROADBAND,
        },
    )
    INTERSTELLAR_LOGISTICS_STATION = Recipe(
        output=AllItems.INTERSTELLAR_LOGISTICS_STATION,
        inputs={
            AllItems.PLANETARY_LOGISTICS_STATION,
            AllItems.PARTICLE_CONTAINER,
            AllItems.TITANIUM_ALLOY,
        },
    )
    INTERSTELLAR_LOGISTICS_VESSEL = Recipe(
        output=AllItems.INTERSTELLAR_LOGISTICS_VESSEL,
        inputs={
            AllItems.PROCESSOR,
            AllItems.TITANIUM_ALLOY,
            AllItems.REINFORCED_THRUSTER,
        },
    )
    IRON_INGOT = Recipe(
        output=AllItems.IRON_INGOT,
        inputs={
            AllItems.IRON_ORE,
        },
    )
    JAMMER_TOWER = Recipe(
        output=AllItems.JAMMER_TOWER,
        inputs={
            AllItems.DIAMOND,
            AllItems.PROCESSOR,
            AllItems.COPPER_INGOT,
            AllItems.PLASMA_EXCITER,
        },
    )
    JAMMING_CAPSULE = Recipe(
        output=AllItems.JAMMING_CAPSULE,
        inputs={
            AllItems.ELECTROMAGNETIC_TURBINE,
            AllItems.PLASMA_EXCITER,
            AllItems.HYDROGEN,
        },
    )
    LASER_TURRET = Recipe(
        output=AllItems.LASER_TURRET,
        inputs={
            AllItems.PHOTON_COMBINER,
            AllItems.STEEL,
            AllItems.PLASMA_EXCITER,
            AllItems.CIRCUIT_BOARD,
        },
    )
    LOGISTICS_BOT = Recipe(
        output=AllItems.LOGISTICS_BOT,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.PROCESSOR,
            AllItems.ENGINE,
        },
    )
    LOGISTICS_DISTRIBUTOR = Recipe(
        output=AllItems.LOGISTICS_DISTRIBUTOR,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.PLASMA_EXCITER,
            AllItems.PROCESSOR,
        },
    )
    LOGISTICS_DRONE = Recipe(
        output=AllItems.LOGISTICS_DRONE,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.THRUSTER,
            AllItems.PROCESSOR,
        },
    )
    MAGNET = Recipe(
        output=AllItems.MAGNET,
        inputs={
            AllItems.IRON_ORE,
        },
    )
    MAGNETIC_COIL = Recipe(
        output=AllItems.MAGNETIC_COIL,
        inputs={
            AllItems.MAGNET,
            AllItems.COPPER_INGOT,
        },
    )
    MAGNUM_AMMO_BOX = Recipe(
        output=AllItems.MAGNUM_AMMO_BOX,
        inputs={
            AllItems.COPPER_INGOT,
        },
    )
    MATRIX_LAB = Recipe(
        output=AllItems.MATRIX_LAB,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GLASS,
            AllItems.CIRCUIT_BOARD,
            AllItems.MAGNETIC_COIL,
        },
    )
    MICROCRYSTALLINE_COMPONENT = Recipe(
        output=AllItems.MICROCRYSTALLINE_COMPONENT,
        inputs={
            AllItems.COPPER_INGOT,
            AllItems.HIGH_PURITY_SILICON,
        },
    )
    MINI_FUSION_POWER_PLANT = Recipe(
        output=AllItems.MINI_FUSION_POWER_PLANT,
        inputs={
            AllItems.PROCESSOR,
            AllItems.CARBON_NANOTUBE,
            AllItems.TITANIUM_ALLOY,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    MINIATURE_PARTICLE_COLLIDER = Recipe(
        output=AllItems.MINIATURE_PARTICLE_COLLIDER,
        inputs={
            AllItems.SUPER_MAGNETIC_RING,
            AllItems.FRAME_MATERIAL,
            AllItems.TITANIUM_ALLOY,
            AllItems.PROCESSOR,
            AllItems.GRAPHENE,
        },
    )
    MINING_MACHINE = Recipe(
        output=AllItems.MINING_MACHINE,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
            AllItems.CIRCUIT_BOARD,
            AllItems.MAGNETIC_COIL,
        },
    )
    MISSILE_SET = Recipe(
        output=AllItems.MISSILE_SET,
        inputs={
            AllItems.ENGINE,
            AllItems.COMBUSTIBLE_UNIT,
            AllItems.COPPER_INGOT,
            AllItems.CIRCUIT_BOARD,
        },
    )
    MISSILE_TURRET = Recipe(
        output=AllItems.MISSILE_TURRET,
        inputs={
            AllItems.ELECTRIC_MOTOR,
            AllItems.STEEL,
            AllItems.ENGINE,
            AllItems.CIRCUIT_BOARD,
        },
    )
    NEGENTROPY_SMELTER = Recipe(
        output=AllItems.NEGENTROPY_SMELTER,
        inputs={
            AllItems.QUANTUM_CHIP,
            AllItems.ENERGY_SHARD,
            AllItems.PLANE_SMELTER,
            AllItems.NEGENTROPY_SINGULARITY,
        },
    )
    OIL_EXTRACTOR = Recipe(
        output=AllItems.OIL_EXTRACTOR,
        inputs={
            AllItems.STEEL,
            AllItems.PLASMA_EXCITER,
            AllItems.STONE_BRICK,
            AllItems.CIRCUIT_BOARD,
        },
    )
    OIL_REFINERY = Recipe(
        output=AllItems.OIL_REFINERY,
        inputs={
            AllItems.STEEL,
            AllItems.PLASMA_EXCITER,
            AllItems.STONE_BRICK,
            AllItems.CIRCUIT_BOARD,
        },
    )
    ORBITAL_COLLECTOR = Recipe(
        output=AllItems.ORBITAL_COLLECTOR,
        inputs={
            AllItems.ACCUMULATOR_FULL,
            AllItems.REINFORCED_THRUSTER,
            AllItems.INTERSTELLAR_LOGISTICS_STATION,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    ORGANIC_CRYSTAL = Recipe(
        output=AllItems.ORGANIC_CRYSTAL,
        inputs={
            AllItems.PLANT_FUEL,
            AllItems.LOG,
            AllItems.WATER,
        },
    )
    ORGANIC_CRYSTAL = Recipe(
        output=AllItems.ORGANIC_CRYSTAL,
        inputs={
            AllItems.REFINED_OIL,
            AllItems.PLASTIC,
            AllItems.WATER,
        },
    )
    PARTICLE_BROADBAND = Recipe(
        output=AllItems.PARTICLE_BROADBAND,
        inputs={
            AllItems.CRYSTAL_SILICON,
            AllItems.CARBON_NANOTUBE,
            AllItems.PLASTIC,
        },
    )
    PARTICLE_CONTAINER = Recipe(
        output=AllItems.PARTICLE_CONTAINER,
        inputs={
            AllItems.COPPER_INGOT,
            AllItems.ELECTROMAGNETIC_TURBINE,
            AllItems.GRAPHENE,
        },
    )
    PARTICLE_CONTAINER = Recipe(
        output=AllItems.PARTICLE_CONTAINER,
        inputs={
            AllItems.UNIPOLAR_MAGNET,
            AllItems.COPPER_INGOT,
        },
    )
    PHOTON_COMBINER = Recipe(
        output=AllItems.PHOTON_COMBINER,
        inputs={
            AllItems.PRISM,
            AllItems.CIRCUIT_BOARD,
        },
    )
    PHOTON_COMBINER = Recipe(
        output=AllItems.PHOTON_COMBINER,
        inputs={
            AllItems.GRATING_CRYSTAL,
            AllItems.CIRCUIT_BOARD,
        },
    )
    PILE_SORTER = Recipe(
        output=AllItems.PILE_SORTER,
        inputs={
            AllItems.SORTER_MK_III,
            AllItems.PROCESSOR,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    PLANE_FILTER = Recipe(
        output=AllItems.PLANE_FILTER,
        inputs={
            AllItems.TITANIUM_GLASS,
            AllItems.CASIMIR_CRYSTAL,
        },
    )
    PLANE_SMELTER = Recipe(
        output=AllItems.PLANE_SMELTER,
        inputs={
            AllItems.PLANE_FILTER,
            AllItems.ARC_SMELTER,
            AllItems.UNIPOLAR_MAGNET,
            AllItems.FRAME_MATERIAL,
        },
    )
    PLANETARY_LOGISTICS_STATION = Recipe(
        output=AllItems.PLANETARY_LOGISTICS_STATION,
        inputs={
            AllItems.PARTICLE_CONTAINER,
            AllItems.STEEL,
            AllItems.TITANIUM_INGOT,
            AllItems.PROCESSOR,
        },
    )
    PLANETARY_SHIELD_GENERATOR = Recipe(
        output=AllItems.PLANETARY_SHIELD_GENERATOR,
        inputs={
            AllItems.PARTICLE_CONTAINER,
            AllItems.STEEL,
            AllItems.ELECTROMAGNETIC_TURBINE,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    PLASMA_CAPSULE = Recipe(
        output=AllItems.PLASMA_CAPSULE,
        inputs={
            AllItems.MAGNET,
            AllItems.DEUTERIUM,
            AllItems.GRAPHENE,
        },
    )
    PLASMA_EXCITER = Recipe(
        output=AllItems.PLASMA_EXCITER,
        inputs={
            AllItems.PRISM,
            AllItems.MAGNETIC_COIL,
        },
    )
    PLASMA_TURRET = Recipe(
        output=AllItems.PLASMA_TURRET,
        inputs={
            AllItems.SUPER_MAGNETIC_RING,
            AllItems.TITANIUM_GLASS,
            AllItems.PROCESSOR,
            AllItems.TITANIUM_ALLOY,
            AllItems.PLASMA_EXCITER,
        },
    )
    PLASTIC = Recipe(
        output=AllItems.PLASTIC,
        inputs={
            AllItems.REFINED_OIL,
            AllItems.ENERGETIC_GRAPHITE,
        },
    )
    PRECISION_DRONE = Recipe(
        output=AllItems.PRECISION_DRONE,
        inputs={
            AllItems.PHOTON_COMBINER,
            AllItems.PROTOTYPE,
            AllItems.ELECTROMAGNETIC_TURBINE,
            AllItems.CIRCUIT_BOARD,
        },
    )
    PRISM = Recipe(
        output=AllItems.PRISM,
        inputs={
            AllItems.GLASS,
        },
    )
    PROCESSOR = Recipe(
        output=AllItems.PROCESSOR,
        inputs={
            AllItems.MICROCRYSTALLINE_COMPONENT,
            AllItems.CIRCUIT_BOARD,
        },
    )
    PROLIFERATOR_MK_I = Recipe(
        output=AllItems.PROLIFERATOR_MK_I,
        inputs={
            AllItems.COAL,
        },
    )
    PROLIFERATOR_MK_II = Recipe(
        output=AllItems.PROLIFERATOR_MK_II,
        inputs={
            AllItems.DIAMOND,
            AllItems.PROLIFERATOR_MK_I,
        },
    )
    PROLIFERATOR_MK_III = Recipe(
        output=AllItems.PROLIFERATOR_MK_III,
        inputs={
            AllItems.CARBON_NANOTUBE,
            AllItems.PROLIFERATOR_MK_II,
        },
    )
    PROTOTYPE = Recipe(
        output=AllItems.PROTOTYPE,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.CIRCUIT_BOARD,
            AllItems.PLASMA_EXCITER,
            AllItems.ENGINE,
        },
    )
    QUANTUM_CHEMICAL_PLANT = Recipe(
        output=AllItems.QUANTUM_CHEMICAL_PLANT,
        inputs={
            AllItems.TITANIUM_GLASS,
            AllItems.CHEMICAL_PLANT,
            AllItems.QUANTUM_CHIP,
            AllItems.STRANGE_MATTER,
        },
    )
    QUANTUM_CHIP = Recipe(
        output=AllItems.QUANTUM_CHIP,
        inputs={
            AllItems.PLANE_FILTER,
            AllItems.PROCESSOR,
        },
    )
    RAY_RECEIVER = Recipe(
        output=AllItems.RAY_RECEIVER,
        inputs={
            AllItems.PHOTON_COMBINER,
            AllItems.SUPER_MAGNETIC_RING,
            AllItems.STEEL,
            AllItems.HIGH_PURITY_SILICON,
            AllItems.PROCESSOR,
        },
    )
    RE_COMPOSING_ASSEMBLER = Recipe(
        output=AllItems.RE_COMPOSING_ASSEMBLER,
        inputs={
            AllItems.MATTER_RECOMBINATOR,
            AllItems.QUANTUM_CHIP,
            AllItems.ASSEMBLING_MACHINE_MK_III,
            AllItems.ENERGY_SHARD,
        },
    )
    REFINED_OIL = Recipe(
        output=AllItems.REFINED_OIL,
        inputs={
            AllItems.REFINED_OIL,
            AllItems.COAL,
            AllItems.HYDROGEN,
        },
    )
    REINFORCED_THRUSTER = Recipe(
        output=AllItems.REINFORCED_THRUSTER,
        inputs={
            AllItems.ELECTROMAGNETIC_TURBINE,
            AllItems.TITANIUM_ALLOY,
        },
    )
    SR_PLASMA_TURRET = Recipe(
        output=AllItems.SR_PLASMA_TURRET,
        inputs={
            AllItems.STEEL,
            AllItems.PLASMA_EXCITER,
            AllItems.PROCESSOR,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    SATELLITE_SUBSTATION = Recipe(
        output=AllItems.SATELLITE_SUBSTATION,
        inputs={
            AllItems.FRAME_MATERIAL,
            AllItems.WIRELESS_POWER_TOWER,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    SELF_EVOLUTION_LAB = Recipe(
        output=AllItems.SELF_EVOLUTION_LAB,
        inputs={
            AllItems.MATRIX_LAB,
            AllItems.SILICON_BASED_NEURON,
            AllItems.QUANTUM_CHIP,
            AllItems.DARK_FOG_MATRIX,
        },
    )
    SHELL_SET = Recipe(
        output=AllItems.SHELL_SET,
        inputs={
            AllItems.COMBUSTIBLE_UNIT,
            AllItems.COPPER_INGOT,
        },
    )
    SIGNAL_TOWER = Recipe(
        output=AllItems.SIGNAL_TOWER,
        inputs={
            AllItems.CRYSTAL_SILICON,
            AllItems.STEEL,
            AllItems.WIRELESS_POWER_TOWER,
        },
    )
    SILICON_ORE = Recipe(
        output=AllItems.SILICON_ORE,
        inputs={
            AllItems.STONE,
        },
    )
    SMALL_CARRIER_ROCKET = Recipe(
        output=AllItems.SMALL_CARRIER_ROCKET,
        inputs={
            AllItems.QUANTUM_CHIP,
            AllItems.DEUTERON_FUEL_ROD,
            AllItems.DYSON_SPHERE_COMPONENT,
        },
    )
    SOLAR_PANEL = Recipe(
        output=AllItems.SOLAR_PANEL,
        inputs={
            AllItems.HIGH_PURITY_SILICON,
            AllItems.COPPER_INGOT,
            AllItems.CIRCUIT_BOARD,
        },
    )
    SOLAR_SAIL = Recipe(
        output=AllItems.SOLAR_SAIL,
        inputs={
            AllItems.PHOTON_COMBINER,
            AllItems.GRAPHENE,
        },
    )
    SORTER_MK_I = Recipe(
        output=AllItems.SORTER_MK_I,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.CIRCUIT_BOARD,
        },
    )
    SORTER_MK_II = Recipe(
        output=AllItems.SORTER_MK_II,
        inputs={
            AllItems.ELECTRIC_MOTOR,
            AllItems.SORTER_MK_I,
        },
    )
    SORTER_MK_III = Recipe(
        output=AllItems.SORTER_MK_III,
        inputs={
            AllItems.ELECTROMAGNETIC_TURBINE,
            AllItems.SORTER_MK_II,
        },
    )
    SPACE_WARPER = Recipe(
        output=AllItems.SPACE_WARPER,
        inputs={
            AllItems.GRAVITON_LENS,
        },
    )
    SPACE_WARPER = Recipe(
        output=AllItems.SPACE_WARPER,
        inputs={
            AllItems.GRAVITY_MATRIX,
        },
    )
    SPLITTER = Recipe(
        output=AllItems.SPLITTER,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
            AllItems.CIRCUIT_BOARD,
        },
    )
    SPRAY_COATER = Recipe(
        output=AllItems.SPRAY_COATER,
        inputs={
            AllItems.STEEL,
            AllItems.MICROCRYSTALLINE_COMPONENT,
            AllItems.PLASMA_EXCITER,
            AllItems.CIRCUIT_BOARD,
        },
    )
    STEEL = Recipe(
        output=AllItems.STEEL,
        inputs={
            AllItems.IRON_INGOT,
        },
    )
    STONE_BRICK = Recipe(
        output=AllItems.STONE_BRICK,
        inputs={
            AllItems.STONE,
        },
    )
    STORAGE_TANK = Recipe(
        output=AllItems.STORAGE_TANK,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.STONE_BRICK,
            AllItems.GLASS,
        },
    )
    STRANGE_ANNIHILATION_FUEL_ROD = Recipe(
        output=AllItems.STRANGE_ANNIHILATION_FUEL_ROD,
        inputs={
            AllItems.FRAME_MATERIAL,
            AllItems.STRANGE_MATTER,
            AllItems.ANTIMATTER_FUEL_ROD,
            AllItems.CORE_ELEMENT,
        },
    )
    STRANGE_MATTER = Recipe(
        output=AllItems.STRANGE_MATTER,
        inputs={
            AllItems.PARTICLE_CONTAINER,
            AllItems.DEUTERIUM,
            AllItems.IRON_INGOT,
        },
    )
    STRUCTURE_MATRIX = Recipe(
        output=AllItems.STRUCTURE_MATRIX,
        inputs={
            AllItems.DIAMOND,
            AllItems.TITANIUM_CRYSTAL,
        },
    )
    SULFURIC_ACID = Recipe(
        output=AllItems.SULFURIC_ACID,
        inputs={
            AllItems.REFINED_OIL,
            AllItems.STONE,
            AllItems.WATER,
        },
    )
    SUPER_MAGNETIC_RING = Recipe(
        output=AllItems.SUPER_MAGNETIC_RING,
        inputs={
            AllItems.MAGNET,
            AllItems.ENERGETIC_GRAPHITE,
            AllItems.ELECTROMAGNETIC_TURBINE,
        },
    )
    SUPERALLOY_AMMO_BOX = Recipe(
        output=AllItems.SUPERALLOY_AMMO_BOX,
        inputs={
            AllItems.TITANIUM_ALLOY,
            AllItems.TITANIUM_AMMO_BOX,
        },
    )
    SUPERSONIC_MISSILE_SET = Recipe(
        output=AllItems.SUPERSONIC_MISSILE_SET,
        inputs={
            AllItems.PROCESSOR,
            AllItems.THRUSTER,
            AllItems.MISSILE_SET,
            AllItems.EXPLOSIVE_UNIT,
        },
    )
    SUPPRESSING_CAPSULE = Recipe(
        output=AllItems.SUPPRESSING_CAPSULE,
        inputs={
            AllItems.TITANIUM_GLASS,
            AllItems.JAMMING_CAPSULE,
            AllItems.SUPER_MAGNETIC_RING,
        },
    )
    TESLA_TOWER = Recipe(
        output=AllItems.TESLA_TOWER,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.MAGNETIC_COIL,
        },
    )
    THERMAL_POWER_PLANT = Recipe(
        output=AllItems.THERMAL_POWER_PLANT,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
            AllItems.STONE_BRICK,
            AllItems.MAGNETIC_COIL,
        },
    )
    THRUSTER = Recipe(
        output=AllItems.THRUSTER,
        inputs={
            AllItems.STEEL,
            AllItems.COPPER_INGOT,
        },
    )
    TITANIUM_ALLOY = Recipe(
        output=AllItems.TITANIUM_ALLOY,
        inputs={
            AllItems.STEEL,
            AllItems.TITANIUM_INGOT,
            AllItems.SULFURIC_ACID,
        },
    )
    TITANIUM_AMMO_BOX = Recipe(
        output=AllItems.TITANIUM_AMMO_BOX,
        inputs={
            AllItems.TITANIUM_INGOT,
            AllItems.MAGNUM_AMMO_BOX,
        },
    )
    TITANIUM_CRYSTAL = Recipe(
        output=AllItems.TITANIUM_CRYSTAL,
        inputs={
            AllItems.ORGANIC_CRYSTAL,
            AllItems.TITANIUM_INGOT,
        },
    )
    TITANIUM_GLASS = Recipe(
        output=AllItems.TITANIUM_GLASS,
        inputs={
            AllItems.TITANIUM_INGOT,
            AllItems.GLASS,
            AllItems.WATER,
        },
    )
    TITANIUM_INGOT = Recipe(
        output=AllItems.TITANIUM_INGOT,
        inputs={
            AllItems.TITANIUM_ORE,
        },
    )
    TRAFFIC_MONITOR = Recipe(
        output=AllItems.TRAFFIC_MONITOR,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
            AllItems.GLASS,
            AllItems.CIRCUIT_BOARD,
        },
    )
    UNIVERSE_MATRIX = Recipe(
        output=AllItems.UNIVERSE_MATRIX,
        inputs={
            AllItems.ANTIMATTER,
            AllItems.STRUCTURE_MATRIX,
            AllItems.ELECTROMAGNETIC_MATRIX,
            AllItems.GRAVITY_MATRIX,
            AllItems.ENERGY_MATRIX,
            AllItems.INFORMATION_MATRIX,
        },
    )
    VERTICAL_LAUNCHING_SILO = Recipe(
        output=AllItems.VERTICAL_LAUNCHING_SILO,
        inputs={
            AllItems.QUANTUM_CHIP,
            AllItems.TITANIUM_ALLOY,
            AllItems.GRAVITON_LENS,
            AllItems.FRAME_MATERIAL,
        },
    )
    WATER_PUMP = Recipe(
        output=AllItems.WATER_PUMP,
        inputs={
            AllItems.ELECTRIC_MOTOR,
            AllItems.IRON_INGOT,
            AllItems.STONE_BRICK,
            AllItems.CIRCUIT_BOARD,
        },
    )
    WIND_TURBINE = Recipe(
        output=AllItems.WIND_TURBINE,
        inputs={
            AllItems.IRON_INGOT,
            AllItems.GEAR,
            AllItems.MAGNETIC_COIL,
        },
    )
    WIRELESS_POWER_TOWER = Recipe(
        output=AllItems.WIRELESS_POWER_TOWER,
        inputs={
            AllItems.PLASMA_EXCITER,
            AllItems.TESLA_TOWER,
        },
    )
