"""
DataDeck - Exercise 3: Game Engine
AggressiveStrategy Implementation

This module implements an aggressive gameplay strategy that prioritizes
dealing damage and maintaining board presence through low-cost creatures.

Classes:
    AggressiveStrategy: Concrete aggressive strategy implementation

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from typing import Any

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Aggressive gameplay strategy implementation.

    This strategy focuses on:
    - Playing low-cost creatures first for board presence
    - Attacking enemy creatures and player directly
    - Prioritizing damage over defense
    - Maintaining constant pressure

    Methods:
        execute_turn: Play cheap creatures and attack aggressively
        get_strategy_name: Return "AggressiveStrategy"
        prioritize_targets: Enemy player first, then weak creatures

    Play Style:
        "The best defense is a good offense" - always attack,
        prioritize damage, ignore defense.
    """

    def execute_turn(
        self, hand: list[Any], battlefield: list[Any]
    ) -> dict[str, Any]:
        """
        Execute an aggressive turn.

        Strategy:
        1. Sort hand by cost (lowest first)
        2. Play as many cheap creatures as possible
        3. Attack with all available creatures
        4. Target enemy player directly when possible

        Args:
            hand: Cards available to play
            battlefield: Cards currently in play

        Returns:
            Dictionary with turn results:
                - strategy: "AggressiveStrategy"
                - cards_played: Names of cards played
                - mana_used: Total mana spent
                - targets_attacked: Targets attacked
                - damage_dealt: Total damage dealt
        """
        cards_played = []
        mana_used = 0
        targets_attacked = []
        damage_dealt = 0

        available_mana = 10

        sorted_hand = sorted(hand, key=lambda card: getattr(card, "cost", 0))

        for card in sorted_hand:
            card_cost = getattr(card, "cost", 0)
            card_name = getattr(card, "name", str(card))

            if mana_used + card_cost <= available_mana:
                cards_played.append(card_name)
                mana_used += card_cost

        for attacker in battlefield:
            targets_attacked.append("Enemy Player")

            attack_power = getattr(
                attacker, "attack_power", getattr(attacker, "attack", 3)
            )
            damage_dealt += attack_power

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        """
        Return strategy identifier.

        Returns:
            "AggressiveStrategy"
        """
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        """
        Prioritize targets for aggressive play.

        Priority order:
        1. Enemy player (direct damage wins games)
        2. Weak creatures (easy kills)
        3. Strong creatures (only if blocking our attacks)

        Args:
            available_targets: List of possible targets

        Returns:
            Sorted list with highest priority first
        """

        players = []
        creatures = []

        for target in available_targets:
            target_type = getattr(target, "type", "creature")
            if target_type == "player":
                players.append(target)
            else:
                creatures.append(target)

        sorted_creatures = sorted(
            creatures, key=lambda c: getattr(c, "health", 100)
        )

        return players + sorted_creatures
