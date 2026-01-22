"""Spell recording and management."""


def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Record a spell with validated ingredients.

    Uses late import technique as required by the subject to demonstrate
    how to avoid circular dependencies (even though there's no actual
    circular dependency in this specific case).

    Args:
        spell_name: Name of the spell to record.
        ingredients: Ingredients used in the spell.

    Returns:
        str: Message indicating if spell was recorded or rejected.
    """
    # Late import to avoid circular dependency (as required by subject)
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if "VALID" in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    else:
        return f"Spell rejected: {spell_name} ({validation_result})"
