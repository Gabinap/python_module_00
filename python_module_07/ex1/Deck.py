"""
DataDeck - Exercise 1: Deck Builder
Deck Management System

This module implements a comprehensive deck management system that can
handle any type of card through polymorphism. The Deck class provides
functionality for building, shuffling, and manipulating card collections.

The Deck demonstrates the power of abstract interfaces - it works with
the Card interface without needing to know about specific card types
(creatures, spells, artifacts, etc.).

Classes:
    Deck: Collection manager for Card objects

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

import random
from typing import Any

from ex0.Card import Card

from ex1.SpellCard import SpellCard


class Deck:
    """
    Deck management and manipulation system.

    A Deck is a collection of cards that can be shuffled, drawn from,
    and manipulated. It provides statistics about its composition and
    ensures type safety through the Card interface.

    The Deck demonstrates polymorphism - it can store and manage any
    object that inherits from Card (creatures, spells, artifacts, etc.)
    without knowing their specific types.

    Attributes:
        cards (List[Card]): The collection of cards in the deck

    Methods:
        add_card: Add a card to the deck
        remove_card: Remove a card by name
        shuffle: Randomize card order
        draw_card: Draw and remove the top card
        get_deck_stats: Retrieve deck statistics
    """

    def __init__(self) -> None:
        """
        Initialize an empty deck.

        Creates a new deck with no cards. Cards can be added using
        the add_card method.
        """
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck.

        Appends the specified card to the deck's collection. The card
        must be an instance of the Card class or its subclasses.

        Args:
            card (Card): The card to add to the deck

        Raises:
            TypeError: If card is not a Card instance
        """
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added to the deck")

        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove a card from the deck by name.

        Searches for and removes the first card matching the given name.
        If multiple cards with the same name exist, only the first is
        removed.

        Args:
            card_name (str): The name of the card to remove

        Returns:
            bool: True if card was found and removed, False otherwise

        Raises:
            TypeError: If card_name is not a string
        """
        if not isinstance(card_name, str):
            raise TypeError("Card name must be a string")

        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True

        return False

    def shuffle(self) -> None:
        """
        Randomize the order of cards in the deck.

        Uses the Fisher-Yates algorithm (via random.shuffle) to
        randomly permute the deck's card order. This is typically
        done before a game begins or when an effect requires it.

        Note:
            This operation modifies the deck in-place.
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card | None:
        """
        Draw and remove the top card from the deck.

        Removes and returns the last card in the deck (representing
        the "top" of the deck). If the deck is empty, returns None.

        Returns:
            Optional[Card]: The drawn card, or None if deck is empty

        Note:
            This operation modifies the deck by removing the drawn card.
        """
        if not self.cards:
            return None

        return self.cards.pop()

    def get_deck_stats(self) -> dict[str, Any]:
        """
        Calculate and return comprehensive deck statistics.

        Analyzes the deck's composition and provides statistics including
        total card count, breakdown by type, and average mana cost.

        Returns:
            Dict[str, Any]: Statistics containing:
                - total_cards (int): Total number of cards
                - creatures (int): Number of creature cards
                - spells (int): Number of spell cards
                - artifacts (int): Number of artifact cards
                - avg_cost (float): Average mana cost of all cards
        """
        total_cards = len(self.cards)

        if total_cards == 0:
            return {
                "total_cards": 0,
                "creatures": 0,
                "spells": 0,
                "artifacts": 0,
                "avg_cost": 0.0,
            }

        creature_count = sum(
            1
            for card in self.cards
            if card.__class__.__name__ == "CreatureCard"
        )
        spell_count = sum(
            1 for card in self.cards if isinstance(card, SpellCard)
        )
        artifact_count = sum(
            1
            for card in self.cards
            if card.__class__.__name__ == "ArtifactCard"
        )

        total_cost = sum(card.cost for card in self.cards)
        avg_cost = total_cost / total_cards

        return {
            "total_cards": total_cards,
            "creatures": creature_count,
            "spells": spell_count,
            "artifacts": artifact_count,
            "avg_cost": round(avg_cost, 1),
        }

    def __len__(self) -> int:
        """
        Return the number of cards in the deck.

        Allows using len(deck) to get the card count.

        Returns:
            int: Number of cards in the deck
        """
        return len(self.cards)

    def __str__(self) -> str:
        """
        String representation of the deck.

        Returns:
            str: Human-readable deck description
        """
        stats = self.get_deck_stats()
        return (
            f"Deck ({stats['total_cards']} cards): "
            f"{stats['creatures']} creatures, "
            f"{stats['spells']} spells, "
            f"{stats['artifacts']} artifacts"
        )

    def __repr__(self) -> str:
        """
        Official string representation for debugging.

        Returns:
            str: Detailed deck representation
        """
        return f"Deck(cards={len(self.cards)})"
