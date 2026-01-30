"""
DataDeck - Exercise 1: Deck Builder
Package initialization file for the deck builder module.

This package provides concrete card type implementations (Spell, Artifact)
and a comprehensive deck management system that can handle any card type
through polymorphism.

Exports:
    SpellCard: Concrete spell card implementation
    ArtifactCard: Concrete artifact card implementation
    Deck: Deck management and manipulation class

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from .ArtifactCard import ArtifactCard
from .Deck import Deck
from .SpellCard import SpellCard


__all__ = ["SpellCard", "ArtifactCard", "Deck"]

__version__ = "1.0"
__author__ = "gagulhon (@École 42)"
