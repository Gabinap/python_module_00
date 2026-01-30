"""
DataDeck - Exercise 2: Ability System
Demonstration Script

This script demonstrates multiple inheritance by showing how EliteCard
implements Card, Combatable, and Magical interfaces simultaneously.

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from ex2.EliteCard import EliteCard


def main() -> None:
    """
    Demonstrate multiple inheritance with EliteCard.

    Shows how a single class can implement multiple interfaces,
    combining card, combat, and magical capabilities into one
    unified entity.
    """
    print("=== DataDeck Ability System ===")
    print()

    # Create an elite card with both combat and magic
    elite = EliteCard(
        name="Arcane Warrior",
        cost=6,
        rarity="Legendary",
        attack=5,
        health=7,
        defense=3,
        spell_power=4,
    )

    # Show inherited capabilities from all three interfaces
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

    # Demonstrate Card interface
    print(f"Playing {elite.name} (Elite Card):")
    game_state = {"current_turn": 1, "player_mana": 10}
    play_result = elite.play(game_state)
    print(f"Play result: {play_result}")
    print()

    # Demonstrate Combatable interface - Combat phase
    print("Combat phase:")
    attack_result = elite.attack("Enemy Goblin")
    print(f"Attack result: {attack_result}")
    print()

    defense_result = elite.defend(5)
    print(f"Defense result: {defense_result}")
    print()

    # Demonstrate Magical interface - Magic phase
    print("Magic phase:")
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")
    print()

    mana_result = elite.channel_mana(3)
    print(f"Mana channel: {mana_result}")
    print()

    # Show comprehensive stats
    print("Combat statistics:")
    print(elite.get_combat_stats())
    print()

    print("Magic statistics:")
    print(elite.get_magic_stats())
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
