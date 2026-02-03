"""
DataDeck - Exercise 4: Tournament Platform
Package initialization for tournament system.

This package demonstrates advanced interface composition by combining
Card, Combatable, and Rankable interfaces into tournament-ready cards.

Classes:
    Rankable: Abstract interface for ranking and rating
    TournamentCard: Card with combat and ranking capabilities
    TournamentPlatform: Tournament management system

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from ex4.Rankable import Rankable
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


__all__ = ["Rankable", "TournamentCard", "TournamentPlatform"]
