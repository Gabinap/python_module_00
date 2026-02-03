"""
DataDeck - Exercise 1: Deck Builder
Concrete Implementation: ArtifactCard

This module implements artifact cards that provide permanent game modifiers.
Artifacts are persistent cards that remain in play and provide ongoing
effects until they are destroyed.

Unlike spells which are consumed, artifacts have durability and remain
active, continuously affecting the game state. They represent magical
items, enchanted objects, or persistent magical constructs.

Classes:
    ArtifactCard: Concrete artifact card with ongoing effects

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from typing import Any

from ex0.Card import Card


class ArtifactCard(Card):
    """
    Concrete implementation of an artifact card.

    Artifacts are permanent cards that remain on the battlefield and
    provide continuous effects. They have durability which determines
    how long they last, and an effect description that explains their
    ongoing benefit.

    Attributes:
        name (str): The name of the artifact
        cost (int): The mana cost to play the artifact
        rarity (str): The rarity tier of the artifact
        durability (int): How many turns/uses before destruction
        effect (str): Description of the artifact's ongoing effect

    Methods:
        play: Deploy the artifact to the battlefield
        activate_ability: Trigger the artifact's ongoing effect
    """

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        """
        Initialize an ArtifactCard with durability and effect.

        Args:
            name (str): The name of the artifact
            cost (int): The mana cost (non-negative)
            rarity (str): The rarity tier
            durability (int): Durability value (must be positive)
            effect (str): Description of the permanent effect

        Raises:
            TypeError: If durability is not an integer or effect not string
            ValueError: If durability is not positive
        """

        super().__init__(name, cost, rarity)

        if not isinstance(durability, int):
            raise TypeError("Durability must be an integer")
        if not isinstance(effect, str):
            raise TypeError("Effect must be a string")
        if durability <= 0:
            raise ValueError("Durability must be positive")

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Deploy the artifact to the battlefield.

        Implementation of the abstract play method from Card. Artifacts
        enter the battlefield and remain there, providing their effect
        continuously until destroyed.

        Args:
            game_state (Dict[str, Any]): Current game state including
                                        battlefield, permanents, etc.

        Returns:
            Dict[str, Any]: Result containing:
                - card_played (str): Name of the artifact
                - mana_used (int): Cost paid to deploy
                - effect (str): Description including permanent status
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict[str, Any]:
        """
        Trigger the artifact's ongoing ability.

        Activates the artifact's effect, which can occur once per turn
        or under specific conditions. This represents the continuous
        benefit provided by having the artifact in play.

        Returns:
            Dict[str, Any]: Activation result containing:
                - artifact_name (str): Name of the artifact
                - effect_applied (str): Description of effect
                - durability_remaining (int): Current durability
                - still_active (bool): Whether artifact is still in play
        """
        return {
            "artifact_name": self.name,
            "effect_applied": self.effect,
            "durability_remaining": self.durability,
            "still_active": self.durability > 0,
        }

    def reduce_durability(self, amount: int = 1) -> bool:
        """
        Reduce the artifact's durability by specified amount.

        Each use or turn may reduce durability. When durability reaches
        zero, the artifact is destroyed and removed from play.

        Args:
            amount (int): Amount to reduce durability by (default 1)

        Returns:
            bool: True if artifact is still active, False if destroyed

        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Durability reduction must be non-negative")

        self.durability -= amount
        return self.durability > 0

    def get_card_info(self) -> dict[str, Any]:
        """
        Retrieve comprehensive artifact information.

        Overrides the base Card method to include artifact-specific
        details like durability and effect.

        Returns:
            Dict[str, Any]: Extended card info including artifact specifics
        """
        base_info = super().get_card_info()
        base_info.update(
            {"durability": self.durability, "effect": self.effect}
        )
        return base_info

    def __str__(self) -> str:
        """
        String representation of the artifact.

        Returns:
            str: Human-readable artifact description
        """
        return (
            f"{self.name} ({self.rarity}) - "
            f"Cost: {self.cost}, Durability: {self.durability}"
        )

    def __repr__(self) -> str:
        """
        Official string representation for debugging.

        Returns:
            str: Detailed artifact representation
        """
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"cost={self.cost}, rarity='{self.rarity}', "
            f"durability={self.durability}, effect='{self.effect}')"
        )
