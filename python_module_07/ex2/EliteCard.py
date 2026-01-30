"""
DataDeck - Exercise 2: Ability System
EliteCard Implementation

This module implements EliteCard, a powerful card type that combines
combat, magical, and base card capabilities through multiple
inheritance.

Classes:
    EliteCard: Card with combat AND magical abilities

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from typing import Any

from ex0.Card import Card

from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Elite card combining combat, magic, and base card functionality.

    EliteCard demonstrates multiple inheritance by implementing three
    interfaces simultaneously: Card (base functionality), Combatable
    (combat abilities), and Magical (spellcasting abilities).

    This creates a versatile card type that can fight, cast spells,
    and participate in standard card game mechanics.

    Attributes:
        name (str): Card name
        cost (int): Mana cost to play
        rarity (str): Card rarity level
        attack_power (int): Physical attack power
        health (int): Current health points
        max_health (int): Maximum health capacity
        defense (int): Defense rating for damage reduction
        current_mana (int): Available mana for spells
        max_mana (int): Maximum mana capacity
        spell_power (int): Magical damage modifier
        known_spells (List[str]): Available spells

    Methods:
        play: Implement Card's abstract method
        attack: Implement Combatable's abstract method
        defend: Implement Combatable's abstract method
        get_combat_stats: Implement Combatable's abstract method
        cast_spell: Implement Magical's abstract method
        channel_mana: Implement Magical's abstract method
        get_magic_stats: Implement Magical's abstract method
        get_tournament_stats: Comprehensive statistics

    Design Pattern:
        Multiple Inheritance - Combines multiple interfaces into
        a single unified implementation
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        defense: int,
        spell_power: int,
    ) -> None:
        """
        Initialize an elite card with combat and magical attributes.

        Args:
            name: Card name
            cost: Mana cost to play the card
            rarity: Card rarity (Common, Rare, Legendary, etc)
            attack: Base attack power for combat
            health: Maximum health points
            defense: Defense rating for damage reduction
            spell_power: Magical power modifier for spells

        Raises:
            ValueError: If attack, health, defense, or spell_power
                       are not positive integers
        """
        # Initialize parent Card class
        super().__init__(name, cost, rarity)

        # Validate combat attributes
        if attack <= 0:
            raise ValueError("Attack must be positive")
        if health <= 0:
            raise ValueError("Health must be positive")
        if defense < 0:
            raise ValueError("Defense cannot be negative")
        if spell_power <= 0:
            raise ValueError("Spell power must be positive")

        # Combat attributes
        self.attack_power: int = attack
        self.max_health: int = health
        self.health: int = health
        self.defense: int = defense

        # Magical attributes
        self.max_mana: int = 10  # Standard mana pool
        self.current_mana: int = 10
        self.spell_power: int = spell_power
        self.known_spells: list[str] = [
            "Fireball",
            "Ice Lance",
            "Healing Touch",
        ]

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Play the elite card onto the battlefield.

        Implements Card's abstract play method. Summons the elite
        card with both combat and magical capabilities.

        Args:
            game_state: Current game state information

        Returns:
            Dictionary containing play results:
                - card_played: Name of the card
                - mana_used: Cost paid
                - effect: Description of summoning effect
                - combat_ready: Combat status
                - magic_ready: Magic status
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite warrior summoned with combat and magic",
            "combat_ready": True,
            "magic_ready": True,
        }

    def attack(self, target: Any) -> dict[str, Any]:
        """
        Execute a physical attack against a target.

        Implements Combatable's abstract attack method. Calculates
        damage and returns detailed combat results.

        Args:
            target: Entity being attacked

        Returns:
            Dictionary containing attack results:
                - attacker: Name of this card
                - target: Target identifier
                - damage: Damage dealt
                - combat_type: Attack type
        """
        target_name = getattr(target, "name", str(target))

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """
        Handle incoming damage with defense mechanics.

        Implements Combatable's abstract defend method. Applies
        defense rating to reduce damage and updates health.

        Args:
            incoming_damage: Raw damage being received

        Returns:
            Dictionary containing defense results:
                - defender: Name of this card
                - damage_taken: Actual damage after defense
                - damage_blocked: Amount blocked by defense
                - still_alive: Survival status

        Raises:
            ValueError: If incoming_damage is negative
        """
        if incoming_damage < 0:
            raise ValueError("Incoming damage cannot be negative")

        # Calculate damage reduction
        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = max(0, incoming_damage - self.defense)

        # Update health
        self.health = max(0, self.health - damage_taken)

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """
        Retrieve current combat statistics.

        Implements Combatable's abstract method. Returns detailed
        combat-related information.

        Returns:
            Dictionary containing combat stats:
                - attack_power: Base attack
                - defense_rating: Defense value
                - health: Current/max health
                - combat_type: Specialization
        """
        return {
            "attack_power": self.attack_power,
            "defense_rating": self.defense,
            "health": f"{self.health}/{self.max_health}",
            "combat_type": "Elite Warrior",
        }

    def cast_spell(
        self, spell_name: str, targets: list[Any]
    ) -> dict[str, Any]:
        """
        Cast a magical spell on targets.

        Implements Magical's abstract method. Consumes mana to cast
        spells with effects based on spell_power.

        Args:
            spell_name: Name of spell to cast
            targets: List of affected entities

        Returns:
            Dictionary containing spell results:
                - caster: Name of this card
                - spell: Spell name
                - targets: Target names
                - mana_used: Mana consumed

        Raises:
            ValueError: If spell_name empty or targets empty
        """
        if not spell_name:
            raise ValueError("Spell name cannot be empty")
        if not targets:
            raise ValueError("Targets list cannot be empty")

        # Mana cost based on spell power
        mana_cost = min(4, self.spell_power)
        actual_cost = min(mana_cost, self.current_mana)
        self.current_mana -= actual_cost

        # Convert targets to names
        target_names = [getattr(t, "name", str(t)) for t in targets]

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": target_names,
            "mana_used": actual_cost,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        """
        Channel mana to increase magical resources.

        Implements Magical's abstract method. Adds mana to current
        pool up to maximum capacity.

        Args:
            amount: Mana to gain

        Returns:
            Dictionary containing channeling results:
                - channeled: Mana gained
                - total_mana: Current mana after channeling

        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")

        # Add mana up to max capacity
        old_mana = self.current_mana
        self.current_mana = min(self.max_mana, self.current_mana + amount)
        actual_gain = self.current_mana - old_mana

        return {"channeled": actual_gain, "total_mana": self.current_mana}

    def get_magic_stats(self) -> dict[str, Any]:
        """
        Retrieve current magical statistics.

        Implements Magical's abstract method. Returns detailed
        magic-related information.

        Returns:
            Dictionary containing magic stats:
                - current_mana: Available mana
                - max_mana: Maximum capacity
                - spell_power: Magical strength
                - known_spells: Available spells
        """
        return {
            "current_mana": self.current_mana,
            "max_mana": self.max_mana,
            "spell_power": self.spell_power,
            "known_spells": self.known_spells,
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        """
        Get comprehensive statistics for tournament display.

        Combines card info, combat stats, and magic stats into
        a single unified view for tournament systems.

        Returns:
            Dictionary with complete card statistics
        """
        base_info = self.get_card_info()
        combat_info = self.get_combat_stats()
        magic_info = self.get_magic_stats()

        return {**base_info, "combat": combat_info, "magic": magic_info}
