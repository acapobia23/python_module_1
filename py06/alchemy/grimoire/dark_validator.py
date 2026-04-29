from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    validate = "INVALID"
    ingrs = ingredients.replace(",", " ").lower().split(" ")
    for item in ingrs:
        flag = False
        if item in allowed:
            validate = "VALID"
            flag = True
            break
    string = ingredients + " - " + validate
    return string