"""
DataDeck - Exercise 4: Tournament Platform
TournamentCard Implementation

This module implements TournamentCard, combining Card, Combatable,
and Rankable interfaces through multiple inheritance for tournament
competition.

Classes:
    TournamentCard: Card with combat and ranking capabilities

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from typing import Any

from ex0.card import Card
from ex2.combatable import Combatable

from ex4.rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Tournament-ready card with combat and ranking.

    TournamentCard demonstrates advanced multiple inheritance by
    implementing three interfaces: Card (base functionality),
    Combatable (combat abilities), and Rankable (tournament ranking).

    This creates a competitive card that can fight, track performance,
    and maintain tournament rankings.

    Attributes:
        name (str): Card name
        cost (int): Mana cost to play
        rarity (str): Card rarity level
        attack_power (int): Physical attack power
        health (int): Current health points
        max_health (int): Maximum health capacity
        defense (int): Defense rating
        rating (int): Tournament rating (ELO)
        wins (int): Total victories
        losses (int): Total defeats

    Methods:
        play: Implement Card's abstract method
        attack: Implement Combatable's abstract method
        defend: Implement Combatable's abstract method
        get_combat_stats: Implement Combatable's abstract method
        calculate_rating: Implement Rankable's abstract method
        update_wins: Implement Rankable's abstract method
        update_losses: Implement Rankable's abstract method
        get_rank_info: Implement Rankable's abstract method
        get_tournament_stats: Comprehensive tournament statistics

    Design Pattern:
        Multiple Inheritance - Combines three interfaces for
        tournament-ready competitive cards
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        defense: int,
    ) -> None:
        """
        Initialize a tournament card.

        Args:
            name: Card name
            cost: Mana cost to play
            rarity: Card rarity
            attack: Base attack power
            health: Maximum health points
            defense: Defense rating

        Raises:
            ValueError: If attack, health, or defense are invalid
        """
        super().__init__(name, cost, rarity)

        # Validate combat attributes
        if attack <= 0:
            raise ValueError("Attack must be positive")
        if health <= 0:
            raise ValueError("Health must be positive")
        if defense < 0:
            raise ValueError("Defense cannot be negative")

        # Combat attributes
        self.attack_power: int = attack
        self.max_health: int = health
        self.health: int = health
        self.defense: int = defense

        # Ranking attributes (starting values)
        self.wins: int = 0
        self.losses: int = 0

        # Calculate initial rating based on card power
        self.rating: int = self.calculate_rating()

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """
        Play the tournament card onto the battlefield.

        Implements Card's abstract play method. Summons the card
        with full combat and ranking capabilities.

        Args:
            game_state: Current game state information

        Returns:
            Dictionary containing play results:
                - card_played: Name of the card
                - mana_used: Cost paid
                - effect: Description of effect
                - tournament_ready: Tournament status
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament warrior summoned",
            "tournament_ready": True,
        }

    def attack(self, target: Any) -> dict[str, Any]:
        """
        Execute an attack in tournament combat.

        Implements Combatable's abstract attack method. Performs
        attack and returns combat results.

        Args:
            target: Entity being attacked

        Returns:
            Dictionary containing attack results:
                - attacker: Name of this card
                - target: Target identifier
                - damage: Damage dealt
                - combat_type: Attack type
        """
        target_name = getattr(target, "name", str(target))

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "tournament_melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        """
        Defend against incoming damage.

        Implements Combatable's abstract defend method. Applies
        defense and updates health.

        Args:
            incoming_damage: Raw damage being received

        Returns:
            Dictionary containing defense results:
                - defender: Name of this card
                - damage_taken: Actual damage after defense
                - damage_blocked: Amount blocked
                - still_alive: Survival status

        Raises:
            ValueError: If incoming_damage is negative
        """
        if incoming_damage < 0:
            raise ValueError("Incoming damage cannot be negative")

        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = max(0, incoming_damage - self.defense)

        self.health = max(0, self.health - damage_taken)

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        """
        Retrieve combat statistics.

        Implements Combatable's abstract method.

        Returns:
            Dictionary containing combat stats:
                - attack_power: Base attack
                - defense_rating: Defense value
                - health: Current/max health
                - combat_type: Specialization
        """
        return {
            "attack_power": self.attack_power,
            "defense_rating": self.defense,
            "health": f"{self.health}/{self.max_health}",
            "combat_type": "Tournament Warrior",
        }

    def calculate_rating(self) -> int:
        """
        Calculate current tournament rating.

        Implements Rankable's abstract method. Uses a simplified
        ELO-like system based on win/loss ratio and card power.

        Returns:
            Integer rating value

        Algorithm:
            - Base: 1200 adjusted by card cost
            - +16 per win
            - -16 per loss
        """
        base_rating = 1200 - ((7 - self.cost) * 50)
        rating_per_win = 16
        rating_per_loss = 16

        self.rating = (
            base_rating
            + (self.wins * rating_per_win)
            - (self.losses * rating_per_loss)
        )

        return self.rating

    def update_wins(self, wins: int) -> None:
        """
        Update win count.

        Implements Rankable's abstract method. Records victories
        and recalculates rating.

        Args:
            wins: Number of wins to add

        Raises:
            ValueError: If wins is negative
        """
        if wins < 0:
            raise ValueError("Wins cannot be negative")

        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        """
        Update loss count.

        Implements Rankable's abstract method. Records defeats
        and recalculates rating.

        Args:
            losses: Number of losses to add

        Raises:
            ValueError: If losses is negative
        """
        if losses < 0:
            raise ValueError("Losses cannot be negative")

        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict[str, Any]:
        """
        Retrieve ranking information.

        Implements Rankable's abstract method. Returns comprehensive
        tournament statistics.

        Returns:
            Dictionary containing:
                - rating: Current rating
                - wins: Total victories
                - losses: Total defeats
                - record: Win-loss record string
                - win_rate: Percentage of wins
        """
        total_games = self.wins + self.losses
        win_rate = (self.wins / total_games * 100) if total_games > 0 else 0

        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}",
            "win_rate": f"{win_rate:.1f}%",
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        """
        Get comprehensive tournament statistics.

        Combines card info, combat stats, and ranking info into
        a unified view for tournament displays.

        Returns:
            Dictionary with complete tournament statistics
        """
        base_info = self.get_card_info()
        combat_info = self.get_combat_stats()
        rank_info = self.get_rank_info()

        return {**base_info, "combat": combat_info, "ranking": rank_info}
