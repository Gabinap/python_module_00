"""
Data Quest - Exercise 3: Achievement Hunter
This module demonstrates set operations for achievement tracking. Manages
unique achievement collections, finds common and rare achievements, and
showcases set operations for player comparison.

Functions:
    main: Demonstrate achievement tracking system with sets

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-05)
"""


def main():
    """
    Demonstrate achievement tracking system using sets.

    Showcases set creation, automatic deduplication, union, intersection,
    and difference operations for analyzing player achievements.

    Returns:
        None: Prints analytics directly to stdout
    """
    print("=== Achievement Tracker System ===")
    print()

    alice_achievements = set(['first_kill', 'level_10', 'treasure_hunter',
                              'speed_demon'])
    bob_achievements = set(['first_kill', 'level_10', 'boss_slayer',
                            'collector'])
    charlie_achievements = set(['level_10', 'treasure_hunter', 'boss_slayer',
                                'speed_demon', 'perfectionist'])

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    print()

    print("=== Achievement Analytics ===")

    all_achievements = alice_achievements.union(bob_achievements,
                                                charlie_achievements)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print()

    common_all = alice_achievements.intersection(bob_achievements,
                                                 charlie_achievements)
    print(f"Common to all players: {common_all}")
    print()

    achievement_counts = set()
    for achievement in all_achievements:
        count = 0
        if achievement in alice_achievements:
            count = count + 1
        if achievement in bob_achievements:
            count = count + 1
        if achievement in charlie_achievements:
            count = count + 1
        if count == 1:
            achievement_counts.add(achievement)

    print(f"Rare achievements (1 player): {alice_achievements.difference(bob_achievements, charlie_achievements) | bob_achievements.difference(alice_achievements, charlie_achievements) | charlie_achievements.difference(alice_achievements, bob_achievements)}")
    print()

    alice_bob_common = alice_achievements.intersection(bob_achievements)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice_achievements.difference(bob_achievements)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob_achievements.difference(alice_achievements)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
