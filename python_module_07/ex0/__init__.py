"""
DataDeck - Exercise 0: Card Foundation
Package initialization file for the card foundation module.

This package provides the foundational abstract classes and concrete
implementations for the DataDeck trading card game system.

Exports:
    Card: Abstract base class for all cards
    CreatureCard: Concrete creature card implementation

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from .card import Card
from .creature_card import CreatureCard


__all__ = ["Card", "CreatureCard"]

__version__ = "1.0"
__author__ = "gagulhon (@École 42)"
