def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    validate = "INVALID"
    ingrs = ingredients.replace(",", " ").lower().split(" ")
    for item in ingrs:
        if item in allowed:
            validate = "VALID"
            break
    string = ingredients + " - " + validate
    return string