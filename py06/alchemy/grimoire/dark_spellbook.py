from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]
    

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return "Spell recorded:" + f"({gr.validate_ingredients(ingredients)})"