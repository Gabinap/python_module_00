"""
DataDeck - Exercise 0: Card Foundation
Abstract Base Class: Card

This module defines the abstract foundation for all card types in the
DataDeck system. It establishes the universal contract that all cards
must follow, ensuring consistency across different card implementations.

The Card class uses Python's ABC (Abstract Base Class) module to enforce
implementation of critical methods in subclasses, following the principle
of "design by contract" in object-oriented programming.

Classes:
    Card: Abstract base class defining the universal card blueprint

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from abc import ABC, abstractmethod


class Card(ABC):
    """
    Abstract base class representing a trading card.

    This class defines the universal interface that all card types must
    implement. It provides both abstract methods (must be implemented by
    subclasses) and concrete methods (inherited behavior).

    Attributes:
        name (str): The name of the card
        cost (int): The mana/resource cost to play the card
        rarity (str): The rarity tier of the card

    Abstract Methods:
        play: Execute the card's effect when played

    Concrete Methods:
        get_card_info: Retrieve comprehensive card information
        is_playable: Check if card can be played with available resources
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Initialize a Card with its fundamental attributes.

        Args:
            name (str): The name of the card
            cost (int): The mana/resource cost (must be non-negative)
            rarity (str): The rarity tier (e.g., 'Common', 'Legendary')

        Raises:
            ValueError: If cost is negative
            TypeError: If arguments have incorrect types
        """
        if not isinstance(name, str):
            raise TypeError("Card name must be a string")
        if not isinstance(cost, int):
            raise TypeError("Card cost must be an integer")
        if not isinstance(rarity, str):
            raise TypeError("Card rarity must be a string")
        if cost < 0:
            raise ValueError("Card cost cannot be negative")

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Execute the card's effect when played (ABSTRACT).

        This method must be implemented by all concrete card subclasses.
        It defines what happens when the card is played during a game.

        Args:
            game_state (dict): Current state of the game

        Returns:
            dict: Result of playing the card, including effects applied
        """
        pass

    def get_card_info(self) -> dict:
        """
        Retrieve comprehensive information about the card.

        Returns:
            dict: Dictionary containing all card attributes
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__,
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Check if the card can be played with available resources.

        Args:
            available_mana (int): Amount of mana/resources available

        Returns:
            bool: True if card cost <= available mana, False otherwise

        Raises:
            TypeError: If available_mana is not an integer
            ValueError: If available_mana is negative
        """
        if not isinstance(available_mana, int):
            raise TypeError("Available mana must be an integer")
        if available_mana < 0:
            raise ValueError("Available mana cannot be negative")

        return self.cost <= available_mana

    def __str__(self) -> str:
        """
        String representation of the card.

        Returns:
            str: Human-readable card description
        """
        return f"{self.name} ({self.rarity}) - Cost: {self.cost}"

    def __repr__(self) -> str:
        """
        Official string representation for debugging.

        Returns:
            str: Detailed card representation
        """
        return (
            f"{self.__class__.__name__}(name='{self.name}', "
            f"cost={self.cost}, rarity='{self.rarity}')"
        )
