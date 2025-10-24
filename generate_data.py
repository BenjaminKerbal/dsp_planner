from dsp_planner.generator import generate_game_recipes, generate_item_enums

if __name__ == "__main__":
    """Generate python code for game items and building recipes."""
    generate_item_enums()
    generate_game_recipes()
