"""
DataDeck - Exercise 3: Game Engine
CardFactory Interface

This module defines the abstract factory interface for creating cards.
Different factories can create different themed card sets (fantasy,
sci-fi, historical, etc).

Classes:
    CardFactory: Abstract base class for card factories

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from abc import ABC, abstractmethod
from typing import Any

from ex0.card import Card


class CardFactory(ABC):
    """
    Abstract factory interface for card creation.

    This interface defines the contract for creating different types
    of cards (creatures, spells, artifacts). Different implementations
    create different themed sets while maintaining the same interface.

    Abstract Methods:
        create_creature: Create a creature card
        create_spell: Create a spell card
        create_artifact: Create an artifact card
        create_themed_deck: Create a complete themed deck
        get_supported_types: List available card types

    Design Pattern:
        Abstract Factory Pattern - Provides an interface for creating
        families of related objects (card types) without specifying
        their concrete classes.
    """

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a creature card.

        Args:
            name_or_power: Either a specific creature name (str) or
                          a power level (int) for random generation.
                          If None, creates a random creature.

        Returns:
            CreatureCard instance with theme-appropriate attributes

        Examples:
            factory.create_creature("Dragon")
            factory.create_creature(5)
            factory.create_creature()

        Design Note:
            Different factories create different themed creatures:
            - FantasyCardFactory: Dragons, Goblins, Elves
            - SciFiCardFactory: Robots, Aliens, Cyborgs
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """
        Create a spell card.

        Args:
            name_or_power: Either a specific spell name (str) or
                          a power level (int) for random generation.
                          If None, creates a random spell.

        Returns:
            SpellCard instance with theme-appropriate attributes

        Examples:
            factory.create_spell("Fireball")
            factory.create_spell(3)
            factory.create_spell()
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """
        Create an artifact card.

        Args:
            name_or_power: Either a specific artifact name (str) or
                          a power level (int) for random generation.
                          If None, creates a random artifact.

        Returns:
            ArtifactCard instance with theme-appropriate attributes

        Examples:
            factory.create_artifact("Mana Ring")
            factory.create_artifact(2)
            factory.create_artifact()
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, Any]:
        """
        Create a complete themed deck of cards.

        Generates a balanced deck with a mix of creatures, spells,
        and artifacts appropriate for the factory's theme.

        Args:
            size: Number of cards in the deck

        Returns:
            Dictionary containing:
                - cards: List of Card objects
                - theme: Theme name (e.g., "Fantasy")
                - size: Total number of cards
                - composition: Breakdown by card type

        Raises:
            ValueError: If size is not positive

        Design Note:
            This demonstrates the factory creating a family of
            related objects that work together cohesively.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, Any]:
        """
        List all card types and variants this factory can create.

        Returns:
            Dictionary mapping card types to available variants:
                - creatures: List of creature names
                - spells: List of spell names
                - artifacts: List of artifact names

        Usage:
            Used by the game engine to display available options
            and validate creation requests.
        """
        pass
