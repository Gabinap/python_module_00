"""
DataDeck - Exercise 4: Tournament Platform
Rankable Interface

This module defines the abstract ranking interface for tournament
participation. Cards implementing this interface can compete in
tournaments and maintain ratings.

Classes:
    Rankable: Abstract base class for ranking capabilities

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from abc import ABC, abstractmethod
from typing import Any


class Rankable(ABC):
    """
    Abstract interface for ranking and rating systems.

    This interface defines the contract for entities that can
    participate in ranked competitions. Implementations must
    provide rating calculation, win/loss tracking, and ranking
    information retrieval.

    Abstract Methods:
        calculate_rating: Compute current rating/ELO
        update_wins: Record victories
        update_losses: Record defeats
        get_rank_info: Retrieve ranking statistics

    Design Pattern:
        Interface Segregation - Separates ranking concerns from
        other card abilities (combat, magic, etc)
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate current rating/ELO score.

        Computes the entity's competitive rating based on win/loss
        record, match difficulty, and other factors.

        Returns:
            Integer rating value (e.g., 1200 for starting rating)

        Design Note:
            Different implementations may use different rating
            algorithms (ELO, Glicko, TrueSkill, etc)
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update win count.

        Records victories in tournament matches. Used for
        maintaining accurate win/loss records.

        Args:
            wins: Number of wins to add

        Raises:
            ValueError: If wins is negative
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update loss count.

        Records defeats in tournament matches. Used for
        maintaining accurate win/loss records.

        Args:
            losses: Number of losses to add

        Raises:
            ValueError: If losses is negative
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict[str, Any]:
        """
        Retrieve current ranking information.

        Returns comprehensive ranking statistics including
        rating, win/loss record, and rank tier.

        Returns:
            Dictionary containing:
                - rating: Current rating/ELO
                - wins: Total victories
                - losses: Total defeats
                - win_rate: Percentage of wins
                - rank_tier: Competitive tier (Bronze, Silver, etc)
        """
        pass
