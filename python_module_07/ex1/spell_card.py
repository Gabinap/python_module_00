"""
DataDeck - Exercise 1: Deck Builder
Concrete Implementation: SpellCard

This module implements spell cards that produce instant magical effects.
Spells are one-time use cards that are consumed when played, representing
direct magical intervention in the game.

Spells can have various effect types (damage, heal, buff, debuff) and
target specific game entities. They follow the abstract Card interface
while adding spell-specific functionality.

Classes:
    SpellCard: Concrete spell card with instant effects

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from typing import Any

from ex0.card import Card


class SpellCard(Card):
    """
    Concrete implementation of a spell card.

    Spells are instant-effect cards that are consumed upon use. They
    represent magical interventions that can damage, heal, buff, or
    debuff targets in the game. Unlike creatures, spells do not remain
    on the battlefield after being played.

    Attributes:
        name (str): The name of the spell
        cost (int): The mana cost to cast the spell
        rarity (str): The rarity tier of the spell
        effect_type (str): Type of effect (damage, heal, buff, debuff)

    Methods:
        play: Cast the spell and produce its effect
        resolve_effect: Process the spell's effect on targets
    """

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """
        Initialize a SpellCard with its effect type.

        Args:
            name (str): The name of the spell
            cost (int): The mana cost (non-negative)
            rarity (str): The rarity tier
            effect_type (str): Effect type (damage, heal, buff, debuff)

        Raises:
            TypeError: If effect_type is not a string
            ValueError: If effect_type is not valid
        """
        super().__init__(name, cost, rarity)

        if not isinstance(effect_type, str):
            raise TypeError("Effect type must be a string")

        valid_effects = ["damage", "heal", "buff", "debuff"]
        if effect_type.lower() not in valid_effects:
            raise ValueError(f"Effect type must be one of {valid_effects}")

        self.effect_type = effect_type.lower()

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Cast the spell and produce its instant effect.

        Implementation of the abstract play method from Card. Spells
        are consumed upon casting, producing an immediate effect and
        then being discarded.

        Args:
            game_state (Dict[str, Any]): Current game state including
                                        targets, battlefield, etc.

        Returns:
            Dict[str, Any]: Result containing:
                - card_played (str): Name of the spell
                - mana_used (int): Cost paid to cast
                - effect (str): Description of the spell effect
        """
        effect_description = self._generate_effect_description()

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_description,
        }

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        """
        Process the spell's effect on specified targets.

        Applies the spell's effect to one or more targets. The exact
        behavior depends on the effect_type (damage, heal, buff, debuff).

        Args:
            targets (List[Any]): List of targets for the spell effect

        Returns:
            Dict[str, Any]: Effect resolution result containing:
                - spell_name (str): Name of the spell
                - effect_type (str): Type of effect applied
                - targets_affected (List[str]): Names of affected targets
                - effect_resolved (bool): Whether effect succeeded
        """
        target_names = [
            getattr(target, "name", str(target)) for target in targets
        ]

        return {
            "spell_name": self.name,
            "effect_type": self.effect_type,
            "targets_affected": target_names,
            "effect_resolved": True,
        }

    def _generate_effect_description(self) -> str:
        """
        Generate a description of the spell's effect.

        Private helper method that creates a human-readable description
        of what the spell does based on its effect_type.

        Returns:
            str: Description of the spell effect
        """
        effect_descriptions = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to target",
            "buff": "Grant +2/+2 to target creature",
            "debuff": "Apply -2/-2 to target creature",
        }

        return effect_descriptions.get(
            self.effect_type, f"Apply {self.effect_type} effect"
        )

    def get_card_info(self) -> dict[str, Any]:
        """
        Retrieve comprehensive spell information.

        Overrides the base Card method to include spell-specific details.

        Returns:
            Dict[str, Any]: Extended card information including effect type
        """
        base_info = super().get_card_info()
        base_info.update({"effect_type": self.effect_type})
        return base_info

    def __str__(self) -> str:
        """
        String representation of the spell.

        Returns:
            str: Human-readable spell description
        """
        return (
            f"{self.name} ({self.rarity}) - "
            f"Cost: {self.cost}, Effect: {self.effect_type}"
        )

    def __repr__(self) -> str:
        """
        Official string representation for debugging.

        Returns:
            str: Detailed spell representation
        """
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"cost={self.cost}, rarity='{self.rarity}', "
            f"effect_type='{self.effect_type}')"
        )
