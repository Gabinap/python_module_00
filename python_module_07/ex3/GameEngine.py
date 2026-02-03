"""
DataDeck - Exercise 3: Game Engine
GameEngine Implementation

This module implements the game engine that orchestrates gameplay
by combining a CardFactory (for creating cards) and a GameStrategy
(for making decisions).

Classes:
    GameEngine: Game orchestrator combining factory and strategy

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from typing import Any

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    Game engine orchestrator.

    Combines a CardFactory and GameStrategy to simulate gameplay.
    The engine uses the factory to create cards and the strategy
    to make gameplay decisions.

    Attributes:
        _factory: CardFactory for creating cards
        _strategy: GameStrategy for making decisions
        _hand: Current hand of cards
        _battlefield: Cards currently in play
        _turns_simulated: Counter for simulation tracking

    Methods:
        configure_engine: Set factory and strategy
        simulate_turn: Execute one turn of gameplay
        get_engine_status: Get current engine state

    Design Pattern:
        This demonstrates composition - the engine uses both a
        factory (for creation) and strategy (for behavior) without
        inheriting from either.
    """

    def __init__(self) -> None:
        """Initialize game engine with empty configuration."""
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._hand: list[Any] = []
        self._battlefield: list[Any] = []
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """
        Configure the engine with factory and strategy.

        Args:
            factory: CardFactory for creating cards
            strategy: GameStrategy for decision-making

        Example:
            engine = GameEngine()
            engine.configure_engine(
                FantasyCardFactory(),
                AggressiveStrategy()
            )
        """
        self._factory = factory
        self._strategy = strategy

        self._prepare_game_state()

    def _prepare_game_state(self) -> None:
        """
        Initialize game state with starting hand.

        Private method that creates an initial hand of cards
        using the configured factory.
        """
        if self._factory is None:
            return

        self._hand = []
        for _ in range(3):
            card = self._factory.create_creature()
            self._hand.append(card)
            self._cards_created += 1

        for _ in range(2):
            card = self._factory.create_spell()
            self._hand.append(card)
            self._cards_created += 1

        for _ in range(2):
            card = self._factory.create_artifact()
            self._hand.append(card)
            self._cards_created += 1

    def simulate_turn(self) -> dict[str, Any]:
        """
        Simulate one complete turn of gameplay.

        Uses the configured strategy to make decisions about
        which cards to play and which targets to attack.

        Returns:
            Dictionary containing turn results:
                - turn_number: Which turn this was
                - strategy_used: Name of strategy
                - cards_in_hand: Hand size before turn
                - cards_on_battlefield: Battlefield size before
                - actions: Results from strategy.execute_turn()

        Raises:
            RuntimeError: If engine not configured

        Design Note:
            The engine delegates decision-making to the strategy,
            demonstrating the Strategy Pattern's separation of
            algorithm from context.
        """
        if self._factory is None or self._strategy is None:
            raise RuntimeError(
                "Engine not configured. Call configure_engine() first"
            )

        self._turns_simulated += 1

        hand_size = len(self._hand)
        battlefield_size = len(self._battlefield)

        actions = self._strategy.execute_turn(self._hand, self._battlefield)

        self._process_actions(actions)

        self._total_damage += actions.get("damage_dealt", 0)

        return {
            "turn_number": self._turns_simulated,
            "strategy_used": self._strategy.get_strategy_name(),
            "cards_in_hand": hand_size,
            "cards_on_battlefield": battlefield_size,
            "actions": actions,
        }

    def _process_actions(self, actions: dict[str, Any]) -> None:
        """
        Process actions and update game state.

        Private method that moves played cards from hand to
        battlefield based on strategy decisions.

        Args:
            actions: Dictionary of actions taken this turn
        """
        cards_played = actions.get("cards_played", [])

        for card_name in cards_played:
            for card in self._hand[:]:
                if getattr(card, "name", "") == card_name:
                    self._hand.remove(card)
                    self._battlefield.append(card)
                    break

    def get_engine_status(self) -> dict[str, Any]:
        """
        Get current engine state and statistics.

        Returns:
            Dictionary containing:
                - factory_type: Class name of factory
                - strategy_type: Class name of strategy
                - turns_simulated: Number of turns executed
                - cards_created: Total cards created
                - total_damage: Cumulative damage dealt
                - hand_size: Current hand size
                - battlefield_size: Current battlefield size
                - supported_types: Types factory can create

        Usage:
            Used for debugging, monitoring, and displaying
            game state to players or observers.
        """
        if self._factory is None or self._strategy is None:
            return {"configured": False, "error": "Engine not configured"}

        return {
            "configured": True,
            "factory_type": self._factory.__class__.__name__,
            "strategy_type": self._strategy.__class__.__name__,
            "turns_simulated": self._turns_simulated,
            "cards_created": self._cards_created,
            "total_damage": self._total_damage,
            "hand_size": len(self._hand),
            "battlefield_size": len(self._battlefield),
            "supported_types": self._factory.get_supported_types(),
        }
