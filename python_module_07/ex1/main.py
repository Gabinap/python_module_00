"""
DataDeck - Exercise 1: Deck Builder
Demonstration Script

This script demonstrates polymorphism in action through the Deck Builder
system. It showcases how a single Deck class can manage multiple card
types (creatures, spells, artifacts) through the common Card interface.

The demonstration follows the expected output format exactly as specified
in the DataDeck project documentation, highlighting the power of
polymorphic design.

Functions:
    main: Execute the demonstration following project specifications

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-23)
"""

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main():
    """
    Demonstrate polymorphic deck management system.

    Creates a deck with different card types (creature, spell, artifact),
    showcases deck statistics, and demonstrates polymorphic behavior
    where each card type is played through the same interface but
    produces different effects.
    """
    print("=== DataDeck Deck Builder ===")
    print()

    deck: Deck = Deck()

    print("Building deck with different card types...")

    fire_dragon = CreatureCard(
        name="Fire Dragon", cost=5, rarity="Legendary", attack=7, health=5
    )
    deck.add_card(fire_dragon)

    mana_crystal = ArtifactCard(
        name="Mana Crystal",
        cost=4,
        rarity="Uncommon",
        durability=5,
        effect="+1 mana per turn",
    )
    deck.add_card(mana_crystal)

    lightning_bolt = SpellCard(
        name="Lightning Bolt", cost=3, rarity="Common", effect_type="damage"
    )
    deck.add_card(lightning_bolt)

    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")
    print()

    deck.shuffle()

    print("Drawing and playing cards:")
    print()

    game_state = {"mana": 10, "battlefield": []}

    while len(deck) > 0:
        card = deck.draw_card()
        if card:
            card_type = card.__class__.__name__.replace("Card", "")
            print(f"Drew: {card.name} ({card_type})")
            play_result = card.play(game_state)
            print(f"Play result: {play_result}")
            print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
