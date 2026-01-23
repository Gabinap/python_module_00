"""
DataDeck - Exercise 0: Card Foundation
Demonstration Script

This script demonstrates the abstract base class design pattern and
concrete implementation of the Card system. It showcases:
- Abstract class instantiation prevention
- Concrete class implementation
- Polymorphism through the Card interface
- Input validation and error handling

Functions:
    demonstrate_card_creation: Show card object instantiation
    demonstrate_card_playability: Test mana cost checking
    demonstrate_creature_combat: Show creature attack mechanics
    demonstrate_abstract_enforcement: Verify abstract pattern
    main: Orchestrate all demonstrations

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


def demonstrate_card_creation() -> None:
    """
    Demonstrate the creation of concrete card instances.

    Creates sample creature cards and displays their information,
    showcasing the proper instantiation and data encapsulation.
    """
    print("=== CARD CREATION DEMONSTRATION ===")
    print()

    # Create a legendary creature
    dragon = CreatureCard(
        name="Fire Dragon", cost=5, rarity="Legendary", attack=7, health=5
    )

    print(f"Created: {dragon}")
    print(f"Card Info: {dragon.get_card_info()}")
    print()


def demonstrate_card_playability(creature: CreatureCard) -> None:
    """
    Demonstrate the playability checking mechanism.

    Tests whether a card can be played given different mana amounts,
    showcasing the is_playable method functionality.

    Args:
        creature (CreatureCard): The creature to test
    """
    print("=== PLAYABILITY CHECK DEMONSTRATION ===")
    print()

    # Test with sufficient mana
    available_mana = 6
    print(f"Testing with {available_mana} mana available:")
    print(f"Can play {creature.name}? {creature.is_playable(available_mana)}")
    print()

    # Test with insufficient mana
    insufficient_mana = 3
    print(f"Testing with {insufficient_mana} mana available:")
    print(
        f"Can play {creature.name}? {creature.is_playable(insufficient_mana)}"
    )
    print()


def demonstrate_creature_combat(attacker: CreatureCard) -> None:
    """
    Demonstrate creature combat mechanics.

    Shows how creatures can attack targets and the resulting combat
    resolution, including play effects and attack results.

    Args:
        attacker (CreatureCard): The attacking creature
    """
    print("=== COMBAT MECHANICS DEMONSTRATION ===")
    print()

    # Simulate playing the creature
    game_state = {"battlefield": [], "mana": 10}
    play_result = attacker.play(game_state)

    print(f"Playing {attacker.name}:")
    print(f"  Mana used: {play_result['mana_used']}")
    print(f"  Effect: {play_result['effect']}")
    print(
        f"  Stats: {play_result['creature_stats']['attack']}/"
        f"{play_result['creature_stats']['health']}"
    )
    print()

    # Create a target creature
    target = CreatureCard(
        name="Goblin Warrior", cost=2, rarity="Common", attack=2, health=2
    )

    print(f"Target: {target}")
    print()

    # Execute combat
    combat_result = attacker.attack_target(target)
    print("Combat Resolution:")
    print(f"  Attacker: {combat_result['attacker']}")
    print(f"  Target: {combat_result['target']}")
    print(f"  Damage dealt: {combat_result['damage_dealt']}")
    print(f"  Combat resolved: {combat_result['combat_resolved']}")

    if "target_survived" in combat_result:
        print(f"  Target survived: {combat_result['target_survived']}")
        if not combat_result["target_survived"]:
            print(f"  Effect: {combat_result['effect']}")
    print()


def demonstrate_abstract_enforcement() -> None:
    """
    Demonstrate that abstract classes cannot be instantiated.

    Attempts to create a Card instance directly, which should fail,
    proving that the abstract pattern is properly enforced.
    """
    print("=== ABSTRACT CLASS ENFORCEMENT ===")
    print()

    print("Attempting to instantiate abstract Card class directly...")
    try:
        # This should raise TypeError
        _ = Card(name="Test", cost=1, rarity="Common")
        print("ERROR: Abstract class was instantiated (should not happen)!")
    except TypeError as e:
        print("SUCCESS: Cannot instantiate abstract class")
        print(f"Reason: {e}")
    print()


def main() -> None:
    """
    Main demonstration function orchestrating all examples.

    Executes a comprehensive demonstration of the Card foundation system,
    showcasing abstract base classes, concrete implementations, and
    the benefits of polymorphism in object-oriented design.
    """
    print("=" * 60)
    print("DATADECK CARD FOUNDATION")
    print("Exercise 0: Abstract Base Class Design Pattern")
    print("=" * 60)
    print()

    # Create a sample creature for demonstrations
    fire_dragon = CreatureCard(
        name="Fire Dragon", cost=5, rarity="Legendary", attack=7, health=5
    )

    # Run demonstrations
    demonstrate_card_creation()
    demonstrate_card_playability(fire_dragon)
    demonstrate_creature_combat(fire_dragon)
    demonstrate_abstract_enforcement()

    # Summary
    print("=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print()
    print("Key concepts demonstrated:")
    print("  ✓ Abstract Base Class (ABC) pattern")
    print("  ✓ Abstract method enforcement")
    print("  ✓ Concrete class implementation")
    print("  ✓ Polymorphism through common interface")
    print("  ✓ Input validation and error handling")
    print("  ✓ Method overriding (get_card_info)")
    print()
    print("The Card foundation provides a robust, extensible architecture")
    print("for building complex card game systems!")
    print()


if __name__ == "__main__":
    main()
