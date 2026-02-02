"""
DataDeck - Exercise 0: Card Foundation
Concrete Implementation: CreatureCard

This module implements a concrete creature card type that inherits from
the abstract Card base class. Creatures are permanents that can attack
and defend, forming the core combat system of the game.

The CreatureCard class demonstrates:
- Inheritance from an abstract base class
- Implementation of abstract methods
- Extension with additional creature-specific functionality
- Input validation for game balance

Classes:
    CreatureCard: Concrete creature card with combat capabilities

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from ex0.card import Card


class CreatureCard(Card):
    """
    Concrete implementation of a creature card.

    Creatures are permanent cards that remain on the battlefield and can
    engage in combat. They have attack and health values that determine
    their effectiveness in battle.

    Attributes:
        name (str): The name of the creature
        cost (int): The mana cost to summon the creature
        rarity (str): The rarity tier of the creature
        attack (int): The damage dealt by the creature
        health (int): The hit points of the creature

    Methods:
        play: Summon the creature to the battlefield
        attack_target: Attack another creature or player
    """

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        """
        Initialize a CreatureCard with combat statistics.

        Args:
            name (str): The name of the creature
            cost (int): The mana cost (non-negative)
            rarity (str): The rarity tier
            attack (int): Attack power (must be positive)
            health (int): Hit points (must be positive)

        Raises:
            TypeError: If attack or health are not integers
            ValueError: If attack or health are not positive
        """

        super().__init__(name, cost, rarity)

        if not isinstance(attack, int):
            raise TypeError("Attack must be an integer")
        if not isinstance(health, int):
            raise TypeError("Health must be an integer")
        if attack <= 0:
            raise ValueError("Attack must be positive")
        if health <= 0:
            raise ValueError("Health must be positive")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """
        Summon the creature to the battlefield.

        Implementation of the abstract play method from Card. This method
        processes the creature entering the battlefield and updates the
        game state accordingly.

        Args:
            game_state (dict): Current game state including battlefield,
                              available mana, etc.

        Returns:
            dict: Result containing:
                - card_played (str): Name of the creature
                - mana_used (int): Cost paid to summon
                - effect (str): Description of the summoning
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        """
        Attack another creature or player.

        Processes combat between this creature and a target. The target
        can be another creature or a player name as string.

        Args:
            target: The target to attack (creature object or string)

        Returns:
            dict: Combat result containing:
                - attacker (str): Name of attacking creature
                - target (str): Name or identifier of target
                - damage_dealt (int): Damage inflicted
                - combat_resolved (bool): Whether combat was successful
        """
        target_name = getattr(target, "name", str(target))

        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        """
        Retrieve comprehensive creature information.

        Overrides the base Card method to include creature-specific stats.

        Returns:
            dict: Extended card information including combat stats
        """
        base_info = super().get_card_info()
        base_info.update({"attack": self.attack, "health": self.health})
        return base_info

    def __str__(self) -> str:
        """
        String representation of the creature.

        Returns:
            str: Human-readable creature description with stats
        """
        return (
            f"{self.name} ({self.rarity}) - "
            f"Cost: {self.cost}, {self.attack}/{self.health}"
        )

    def __repr__(self) -> str:
        """
        Official string representation for debugging.

        Returns:
            str: Detailed creature representation
        """
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"cost={self.cost}, rarity='{self.rarity}', "
            f"attack={self.attack}, health={self.health})"
        )
