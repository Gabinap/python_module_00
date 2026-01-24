"""
DataDeck - Exercise 0: Card Foundation
Demonstration Script

This script demonstrates the abstract base class design pattern through
the DataDeck card system. It showcases proper implementation of abstract
base classes, concrete implementations, and polymorphism following the
specifications from the DataDeck v2.0 project documentation.

The demonstration follows the expected output format exactly as specified
in the project requirements, ensuring consistency with evaluation criteria.

Functions:
    main: Execute the demonstration following project specifications

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from ex0.CreatureCard import CreatureCard


def main() -> None:
    """
    Demonstrate abstract base class design and concrete implementation.

    Executes a comprehensive demonstration following the exact output
    format specified in the DataDeck project documentation. Shows:
    - Card information retrieval
    - Playability checking with different mana amounts
    - Card playing mechanics
    - Combat resolution
    """
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()

    # Create Fire Dragon creature
    dragon = CreatureCard(
        name="Fire Dragon", cost=5, rarity="Legendary", attack=7, health=5
    )

    # Display card information
    print("CreatureCard Info:")
    card_info = dragon.get_card_info()
    print(f"{card_info}")
    print()

    # Test playability with sufficient mana
    sufficient_mana = 6
    print(f"Playing Fire Dragon with {sufficient_mana} mana available:")
    print(f"Playable: {dragon.is_playable(sufficient_mana)}")

    # Simulate playing the card
    game_state = {"mana": sufficient_mana, "battlefield": []}
    play_result = dragon.play(game_state)
    print(f"Play result: {play_result}")
    print()

    # Demonstrate combat mechanics
    print("Fire Dragon attacks Goblin Warrior:")
    # Create target (string representation)
    attack_result = dragon.attack_target("Goblin Warrior")
    print(f"Attack result: {attack_result}")
    print()

    # Test playability with insufficient mana
    insufficient_mana = 3
    print(f"Testing insufficient mana ({insufficient_mana} available):")
    print(f"Playable: {dragon.is_playable(insufficient_mana)}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
