"""
DataDeck - Exercise 3: Game Engine
GameStrategy Interface

This module defines the abstract strategy interface for game AI.
Different strategies can be implemented to create various play styles
(aggressive, defensive, control, etc).

Classes:
    GameStrategy: Abstract base class for game strategies

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from abc import ABC, abstractmethod
from typing import Any


class GameStrategy(ABC):
    """
    Abstract interface for game strategies.

    This interface defines the contract for AI decision-making in
    the game. Different implementations can create various play styles
    like aggressive (attack-focused), defensive (control-focused),
    or combo-based strategies.

    Abstract Methods:
        execute_turn: Main decision-making method for a turn
        get_strategy_name: Return the strategy's identifier
        prioritize_targets: Order targets by strategic importance

    Design Pattern:
        Strategy Pattern - Encapsulates different algorithms
        (play styles) and makes them interchangeable at runtime.
    """

    @abstractmethod
    def execute_turn(
        self, hand: list[Any], battlefield: list[Any]
    ) -> dict[str, Any]:
        """
        Execute a complete turn using this strategy.

        This is the main decision-making method. It analyzes the
        current game state (hand and battlefield) and returns
        decisions about which cards to play and which targets to attack.

        Args:
            hand: List of cards available to play
            battlefield: List of cards currently in play

        Returns:
            Dictionary containing turn execution results:
                - strategy: Name of the strategy used
                - cards_played: List of card names played
                - mana_used: Total mana spent
                - targets_attacked: List of targets attacked
                - damage_dealt: Total damage dealt this turn

        Design Note:
            Different strategies will make different decisions given
            the same game state, demonstrating polymorphic behavior.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Return the name/identifier of this strategy.

        Returns:
            String identifying the strategy (e.g., "AggressiveStrategy")

        Usage:
            Used for logging, debugging, and displaying which
            strategy is currently active in the game engine.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        """
        Order targets by strategic importance.

        Different strategies prioritize different targets:
        - Aggressive: Enemy player first, then weak creatures
        - Defensive: Strong enemy creatures first
        - Control: High-value targets first

        Args:
            available_targets: List of potential attack targets

        Returns:
            Reordered list with highest priority targets first

        Design Note:
            This demonstrates how the Strategy Pattern allows
            different sorting/prioritization algorithms to be
            swapped at runtime.
        """
        pass
