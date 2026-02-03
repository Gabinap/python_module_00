"""
DataDeck - Exercise 2: Ability System
Package initialization for ability interfaces and elite cards.

This package demonstrates multiple inheritance by combining combat,
magic, and card interfaces into unified elite cards.

Classes:
    Combatable: Abstract interface for combat capabilities
    Magical: Abstract interface for magical abilities
    EliteCard: Implementation combining Card, Combatable, and Magical

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical


__all__ = ["Combatable", "Magical", "EliteCard"]
