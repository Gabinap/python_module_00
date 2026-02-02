"""
DataDeck - Exercise 3: Game Engine
Package initialization for game engine components.

This package demonstrates the Strategy Pattern and Abstract Factory
Pattern working together to create a flexible game engine.

Classes:
    GameStrategy: Abstract interface for game strategies
    CardFactory: Abstract interface for card creation
    AggressiveStrategy: Concrete aggressive gameplay strategy
    FantasyCardFactory: Concrete factory for fantasy-themed cards
    GameEngine: Game orchestrator combining factory and strategy

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from ex3.aggressive_strategy import AggressiveStrategy
from ex3.card_factory import CardFactory
from ex3.fantasy_card_factory import FantasyCardFactory
from ex3.game_engine import GameEngine
from ex3.game_strategy import GameStrategy


__all__ = [
    "GameStrategy",
    "CardFactory",
    "AggressiveStrategy",
    "FantasyCardFactory",
    "GameEngine",
]
