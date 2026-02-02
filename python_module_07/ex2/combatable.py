"""
DataDeck - Exercise 2: Ability System
Combatable Interface

This module defines the abstract combat interface that cards can
implement to gain combat capabilities (attacking, defending, etc).

Classes:
    Combatable: Abstract base class defining combat contract

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    """
    Abstract interface for combat capabilities.

    This interface defines the contract for any entity that can
    participate in combat. Classes implementing this interface must
    provide attack, defense, and combat statistics functionality.

    Abstract Methods:
        attack: Execute an attack against a target
        defend: Handle incoming damage with defense mechanics
        get_combat_stats: Retrieve current combat statistics

    Design Pattern:
        Interface Segregation - Separates combat concerns from other
        card abilities (magic, utility, etc)
    """

    @abstractmethod
    def attack(self, target: Any) -> dict[str, Any]:
        """
        Execute an attack against a target.

        This method handles combat mechanics, damage calculation,
        and returns detailed attack results.

        Args:
            target: The entity being attacked (can be card, player, etc)

        Returns:
            Dictionary containing attack results:
                - attacker: Name of the attacking entity
                - target: Name/identifier of the target
                - damage: Amount of damage dealt
                - combat_type: Type of attack (melee, ranged, etc)
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """
        Handle incoming damage with defense mechanics.

        This method processes incoming attacks, applies defense
        calculations (armor, shields, etc), and returns the results.

        Args:
            incoming_damage: Amount of damage being received

        Returns:
            Dictionary containing defense results:
                - defender: Name of the defending entity
                - damage_taken: Actual damage after defense
                - damage_blocked: Amount blocked by defense
                - still_alive: Whether defender survived

        Raises:
            ValueError: If incoming_damage is negative
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]:
        """
        Retrieve current combat statistics.

        Returns comprehensive combat-related information including
        attack power, defense rating, health, and combat modifiers.

        Returns:
            Dictionary containing combat stats:
                - attack_power: Base attack strength
                - defense_rating: Base defense capability
                - health: Current health points
                - combat_type: Combat specialization
        """
        pass
