"""Advanced transmutation spells using relative imports."""

from ..potions import healing_potion
from .basic import lead_to_gold


def philosophers_stone() -> str:
    """Create the legendary philosopher's stone."""
    gold_result = lead_to_gold()
    potion_result = healing_potion()
    return (
        f"Philosopher's stone created using {gold_result} and {potion_result}"
    )


def elixir_of_life() -> str:
    """Create the elixir of life, granting eternal youth."""
    return "Elixir of life: eternal youth achieved!"
