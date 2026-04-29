import alchemy.grimoire as gr

def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str:
    return f"Spell recorded: {spell_name} ({gr.validate_ingredients(ingredients)})"
