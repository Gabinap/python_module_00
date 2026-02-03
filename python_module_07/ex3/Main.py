"""
DataDeck - Exercise 3: Game Engine
Demonstration Script

This script demonstrates the Strategy Pattern and Abstract Factory
Pattern working together in a game engine.

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    """
    Demonstrate game engine with factory and strategy patterns.

    Shows how the Abstract Factory Pattern and Strategy Pattern
    combine to create a flexible, extensible game system.
    """
    print("=== DataDeck Game Engine ===")
    print()

    # Create factory and strategy
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")

    # Show available card types
    supported_types = factory.get_supported_types()
    print(f"Available types: {supported_types}")
    print()

    # Create and configure game engine
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    # Show initial status
    status = engine.get_engine_status()
    print("Engine configured:")
    print(f"- Factory: {status['factory_type']}")
    print(f"- Strategy: {status['strategy_type']}")
    print(f"- Starting hand: {status['hand_size']} cards")
    print(f"- Battlefield: {status['battlefield_size']} cards")
    print()

    # Simulate a turn
    print("Simulating aggressive turn...")
    turn_result = engine.simulate_turn()

    print(f"Turn {turn_result['turn_number']} complete:")
    print(f"Strategy: {turn_result['strategy_used']}")
    print()

    # Display actions taken
    actions = turn_result["actions"]
    print("Turn execution:")
    print(f"Cards played: {actions['cards_played']}")
    print(f"Mana used: {actions['mana_used']}")
    print(f"Targets attacked: {actions['targets_attacked']}")
    print(f"Damage dealt: {actions['damage_dealt']}")
    print()

    # Final status
    final_status = engine.get_engine_status()
    print("Game Report:")
    print(f"Turns simulated: {final_status['turns_simulated']}")
    print(f"Strategy used: {final_status['strategy_type']}")
    print(f"Total damage: {final_status['total_damage']}")
    print(f"Cards created: {final_status['cards_created']}")
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
