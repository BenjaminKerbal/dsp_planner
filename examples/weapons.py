from dsp_planner.factory_planning import plan_building_order
from dsp_planner.items import AllItems as AI

if __name__ == "__main__":
    turrets: set[AI] = {
        AI.GAUSS_TURRET,
        AI.PLASMA_TURRET,
        AI.MISSILE_TURRET,
        AI.IMPLOSION_CANNON,
        AI.LASER_TURRET,
        AI.SR_PLASMA_TURRET,
    }

    plan = plan_building_order(turrets, 1)
    print(plan)

    ammo: set[AI] = {
        AI.MISSILE_SET,
        AI.SHELL_SET,
        AI.MAGNUM_AMMO_BOX,
        AI.TITANIUM_AMMO_BOX,
    }

    plan = plan_building_order(ammo, 1)
    print(plan)
