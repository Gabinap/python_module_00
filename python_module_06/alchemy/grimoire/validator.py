"""Spell ingredient validation utilities."""


def validate_ingredients(ingredients: str) -> str:
    """
    Validate spell ingredients against known elemental components.

    Args:
        ingredients: String containing ingredient names.

    Returns:
        str: Validation result indicating VALID or INVALID.
    """
    valid_elements = ["fire", "water", "earth", "air"]
    ingredients_lower = ingredients.lower()
    is_valid = any(element in ingredients_lower for element in valid_elements)

    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
