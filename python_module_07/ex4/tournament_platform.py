"""
DataDeck - Exercise 4: Tournament Platform
TournamentPlatform Implementation

This module implements the tournament platform that manages
tournament cards, creates matches, and maintains leaderboards.

Classes:
    TournamentPlatform: Tournament management system

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

import random
from typing import Any

from ex4.tournament_card import TournamentCard


class TournamentPlatform:
    """
    Tournament platform management system.

    Manages tournament operations including card registration,
    match creation, rating updates, and leaderboard generation.

    Attributes:
        _cards: Dictionary mapping card IDs to TournamentCard objects
        _matches_played: Counter for total matches
        _platform_status: Current platform status

    Methods:
        register_card: Register a card for tournament play
        create_match: Create and resolve a match between two cards
        get_leaderboard: Generate ranked leaderboard
        generate_tournament_report: Generate comprehensive report

    Design Pattern:
        Repository Pattern - Encapsulates card storage and retrieval
        with a clean API for tournament operations
    """

    def __init__(self) -> None:
        """Initialize tournament platform."""
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played: int = 0
        self._platform_status: str = "active"

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a card for tournament competition.

        Generates a unique ID and stores the card in the platform.

        Args:
            card: TournamentCard to register

        Returns:
            String card ID (e.g., "dragon_001")

        Raises:
            TypeError: If card is not a TournamentCard
        """
        if not isinstance(card, TournamentCard):
            raise TypeError("Only TournamentCard instances can register")

        words = card.name.lower().split()
        base_name = words[-1] if words else "card"

        count = sum(
            1
            for card_id in self._cards.keys()
            if card_id.startswith(base_name + "_")
        )

        card_id = f"{base_name}_{count + 1:03d}"

        self._cards[card_id] = card

        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        """
        Create and resolve a match between two cards.

        Simulates a tournament match, determines winner, updates
        ratings using ELO-like system.

        Args:
            card1_id: ID of first card
            card2_id: ID of second card

        Returns:
            Dictionary containing match results:
                - winner: ID of winning card
                - loser: ID of losing card
                - winner_rating: Updated rating of winner
                - loser_rating: Updated rating of loser

        Raises:
            ValueError: If card IDs don't exist or are the same
        """

        if card1_id not in self._cards:
            raise ValueError(f"Card {card1_id} not registered")
        if card2_id not in self._cards:
            raise ValueError(f"Card {card2_id} not registered")
        if card1_id == card2_id:
            raise ValueError("Card cannot match against itself")

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        if card1.attack_power > card2.attack_power:
            winner_id = card1_id
            loser_id = card2_id
            winner = card1
            loser = card2
        elif card2.attack_power > card1.attack_power:
            winner_id = card2_id
            loser_id = card1_id
            winner = card2
            loser = card1
        else:
            if random.random() < 0.5:
                winner_id = card1_id
                loser_id = card2_id
                winner = card1
                loser = card2
            else:
                winner_id = card2_id
                loser_id = card1_id
                winner = card2
                loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        self._matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list[dict[str, Any]]:
        """
        Generate tournament leaderboard.

        Ranks all registered cards by rating (highest first).

        Returns:
            List of dictionaries containing:
                - rank: Position on leaderboard (1, 2, 3, ...)
                - card_id: Card identifier
                - name: Card name
                - rating: Current rating
                - record: Win-loss record
        """

        card_items = list(self._cards.items())

        sorted_cards = sorted(
            card_items, key=lambda x: x[1].rating, reverse=True
        )

        leaderboard = []
        for rank, (card_id, card) in enumerate(sorted_cards, start=1):
            rank_info = card.get_rank_info()
            leaderboard.append(
                {
                    "rank": rank,
                    "card_id": card_id,
                    "name": card.name,
                    "rating": card.rating,
                    "record": rank_info["record"],
                }
            )

        return leaderboard

    def generate_tournament_report(self) -> dict[str, Any]:
        """
        Generate comprehensive tournament report.

        Returns platform statistics including total cards,
        matches played, average rating, and status.

        Returns:
            Dictionary containing:
                - total_cards: Number of registered cards
                - matches_played: Total matches completed
                - avg_rating: Average rating of all cards
                - platform_status: Current status
        """
        if not self._cards:
            return {
                "total_cards": 0,
                "matches_played": self._matches_played,
                "avg_rating": 0,
                "platform_status": self._platform_status,
            }

        total_rating = sum(card.rating for card in self._cards.values())
        avg_rating = total_rating // len(self._cards)

        return {
            "total_cards": len(self._cards),
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": self._platform_status,
        }
