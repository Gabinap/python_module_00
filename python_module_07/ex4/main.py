"""
DataDeck - Exercise 4: Tournament Platform
Demonstration Script

This script demonstrates advanced interface composition by combining
Card, Combatable, and Rankable interfaces in a tournament system.

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-30)
"""

from ex4.tournament_card import TournamentCard
from ex4.tournament_platform import TournamentPlatform


def main() -> None:
    """
    Demonstrate tournament platform with multiple inheritance.

    Shows how TournamentCard implements Card, Combatable, and
    Rankable interfaces simultaneously in a competitive system.
    """
    print("=== DataDeck Tournament Platform ===")
    print()

    platform = TournamentPlatform()

    dragon = TournamentCard(
        name="Fire Dragon",
        cost=7,
        rarity="Legendary",
        attack=7,
        health=7,
        defense=3,
    )

    wizard = TournamentCard(
        name="Ice Wizard", cost=6, rarity="Rare", attack=5, health=6, defense=4
    )

    print("Registering Tournament Cards...")
    print()
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")
    print()

    print(f"{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")
    print()

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")
    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )
    print()

    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(report)
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
