"""
Data Quest - Exercise 3: Achievement Hunter
This module demonstrates set operations for achievement tracking. Manages
unique achievement collections, finds common achievements, identifies rare
ones, and enforces globally unique achievements that only one player can own.

Functions:
    validate_achievements: Enforce globally unique achievement rules
    main: Demonstrate achievement tracking system with sets

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-05)
"""


def validate_achievements(player_name, achievements, global_unique,
                          claimed_by):
    """
    Validate and clean achievements, enforcing globally unique rules.

    Removes achievements that are globally unique if they've already been
    claimed by another player. Prints warnings for rejected achievements.

    Args:
        player_name: Name of the player claiming achievements
        achievements: Set of achievements the player is trying to claim
        global_unique: Set of achievement names that are globally unique
        claimed_by: Dictionary mapping unique achievements to their owner

    Returns:
        set: Validated achievements with globally unique ones removed if needed
    """
    validated = set()

    for achievement in achievements:
        if achievement in global_unique:
            if achievement in claimed_by:
                print(f"Warning: '{achievement}' already claimed by "
                      f"{claimed_by[achievement]}. "
                      f"Rejecting for {player_name}.")
            else:
                claimed_by[achievement] = player_name
                validated.add(achievement)
        else:
            validated.add(achievement)

    return validated


def main():
    """
    Demonstrate achievement tracking system using sets.

    Showcases set creation, deduplication, union, intersection, and
    difference operations for analyzing player achievements. Enforces
    globally unique achievements that only the first claimer can own.

    Returns:
        None: Prints analytics directly to stdout
    """
    print("=== Achievement Tracker System ===")
    print()

    global_unique_achievements = set(['first_kill', 'world_first'])
    claimed_unique = {}

    alice_raw = set(['first_kill', 'level_10', 'treasure_hunter',
                     'speed_demon'])
    bob_raw = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie_raw = set(['level_10', 'treasure_hunter', 'boss_slayer', 
                       'speed_demon', 'perfectionist', 'first_kill'])

    print("Validating achievements...")
    print()

    alice_achievements = validate_achievements('alice', alice_raw, 
                                               global_unique_achievements,
                                               claimed_unique)
    bob_achievements = validate_achievements('bob', bob_raw,
                                            global_unique_achievements,
                                            claimed_unique)
    charlie_achievements = validate_achievements('charlie', charlie_raw,
                                                 global_unique_achievements,
                                                 claimed_unique)

    print()
    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    print()

    print("=== Achievement Analytics ===")
    print()

    all_achievements = alice_achievements.union(bob_achievements,
                                                charlie_achievements)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print()

    common_all = alice_achievements.intersection(bob_achievements,
                                                 charlie_achievements)
    print(f"Common to all players: {common_all}")
    print()

    common_any_two = alice_achievements.intersection(bob_achievements).union(
        alice_achievements.intersection(charlie_achievements),
        bob_achievements.intersection(charlie_achievements)
    )
    rare_achievements = all_achievements.difference(common_any_two)

    print(f"Rare achievements (1 player): {rare_achievements}")
    print()

    alice_bob_common = alice_achievements.intersection(bob_achievements)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice_achievements.difference(bob_achievements)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob_achievements.difference(alice_achievements)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
