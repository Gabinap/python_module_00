"""
DataDeck - Exercise 2: Ability System
Magical Interface

This module defines the abstract magic interface that cards can
implement to gain magical capabilities (spellcasting, mana
channeling, etc).

Classes:
    Magical: Abstract base class defining magic contract

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from abc import ABC, abstractmethod
from typing import Any


class Magical(ABC):
    """
    Abstract interface for magical capabilities.

    This interface defines the contract for any entity that can
    use magic. Classes implementing this interface must provide
    spellcasting, mana management, and magic statistics.

    Abstract Methods:
        cast_spell: Cast a magical spell on targets
        channel_mana: Manage mana resources
        get_magic_stats: Retrieve current magic statistics

    Design Pattern:
        Interface Segregation - Separates magical concerns from
        combat and other abilities
    """

    @abstractmethod
    def cast_spell(
        self, spell_name: str, targets: list[Any]
    ) -> dict[str, Any]:
        """
        Cast a magical spell on one or more targets.

        This method handles spell mechanics, mana consumption,
        and multi-target spell effects.

        Args:
            spell_name: Name of the spell to cast
            targets: List of entities affected by the spell

        Returns:
            Dictionary containing spell results:
                - caster: Name of the entity casting the spell
                - spell: Name of the spell cast
                - targets: List of affected targets
                - mana_used: Mana consumed by the spell

        Raises:
            ValueError: If spell_name is empty or targets is empty
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]:
        """
        Channel mana to increase magical resources.

        This method manages mana generation, allowing entities to
        gain additional magical energy for future spellcasting.

        Args:
            amount: Amount of mana to channel

        Returns:
            Dictionary containing channeling results:
                - channeled: Amount of mana gained
                - total_mana: Total mana after channeling

        Raises:
            ValueError: If amount is not positive
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]:
        """
        Retrieve current magical statistics.

        Returns comprehensive magic-related information including
        current mana, spell power, and known spells.

        Returns:
            Dictionary containing magic stats:
                - current_mana: Available mana for spells
                - max_mana: Maximum mana capacity
                - spell_power: Magical strength modifier
                - known_spells: List of available spells
        """
        pass
