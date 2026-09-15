from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    formated_ingredients = ingredients.lower()
    is_valid = any(i in formated_ingredients for i in allowed)

    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
