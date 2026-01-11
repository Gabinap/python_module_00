"""
Data Quest - Exercise 6: Data Alchemist
This module demonstrates comprehension operations for elegant data
transformation. Showcases list, dictionary, and set comprehensions for
filtering, mapping, and transforming gaming data efficiently.

Functions:
    main: Demonstrate all three types of comprehensions

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-11)
"""


def main():
    """
    Demonstrate data transformation using comprehensions.
    
    Showcases list comprehensions for filtering and transforming,
    dict comprehensions for mapping and grouping, and set comprehensions
    for finding unique values in gaming analytics data.
    
    Returns:
        None: Prints comprehension demonstrations directly to stdout
    """
    print("=== Game Analytics Dashboard ===")
    print()
    
    player_scores = [
        {'name': 'alice', 'score': 2300, 'region': 'north', 'active': True},
        {'name': 'bob', 'score': 1800, 'region': 'east', 'active': True},
        {'name': 'charlie', 'score': 2150, 'region': 'north', 'active': True},
        {'name': 'diana', 'score': 2050, 'region': 'south', 'active': False},
        {'name': 'eve', 'score': 1650, 'region': 'east', 'active': True},
        {'name': 'frank', 'score': 1900, 'region': 'central', 'active': False}
    ]
    
    player_achievements = {
        'alice': ['first_kill', 'level_10', 'boss_slayer', 'speed_demon', 'treasure_hunter'],
        'bob': ['first_kill', 'level_10', 'collector'],
        'charlie': ['level_10', 'boss_slayer', 'speed_demon', 'treasure_hunter', 
                    'perfectionist', 'elite_warrior', 'master_explorer'],
        'diana': ['first_kill', 'treasure_hunter', 'collector', 'speed_demon'],
        'eve': ['level_10', 'first_kill'],
        'frank': ['boss_slayer', 'collector', 'elite_warrior']
    }
    
    print("=== List Comprehension Examples ===")
    
    high_scorers = [player['name'] for player in player_scores if player['score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    
    scores_doubled = [player['score'] * 2 for player in player_scores]
    print(f"Scores doubled: {scores_doubled}")
    
    active_players = [player['name'] for player in player_scores if player['active']]
    print(f"Active players: {active_players}")
    print()
    
    print("=== Dict Comprehension Examples ===")
    
    player_score_map = {player['name']: player['score'] for player in player_scores}
    print(f"Player scores: {player_score_map}")
    
    score_categories = {
        'high': len([p for p in player_scores if p['score'] > 2000]),
        'medium': len([p for p in player_scores if 1800 <= p['score'] <= 2000]),
        'low': len([p for p in player_scores if p['score'] < 1800])
    }
    print(f"Score categories: {score_categories}")
    
    achievement_counts = {name: len(achievements) 
                         for name, achievements in player_achievements.items()}
    print(f"Achievement counts: {achievement_counts}")
    print()

    print("=== Set Comprehension Examples ===")
    
    unique_players = {player['name'] for player in player_scores}
    print(f"Unique players: {unique_players}")
    
    all_achievements_list = [achievement 
                            for achievements in player_achievements.values() 
                            for achievement in achievements]
    unique_achievements = {achievement for achievement in all_achievements_list}
    print(f"Unique achievements: {unique_achievements}")
    
    active_regions = {player['region'] for player in player_scores if player['active']}
    print(f"Active regions: {active_regions}")
    print()
    
    print("=== Combined Analysis ===")
    
    total_players = len(unique_players)
    print(f"Total players: {total_players}")
    
    total_unique_achievements = len(unique_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")
    
    all_scores = [player['score'] for player in player_scores]
    average_score = sum(all_scores) / len(all_scores)
    print(f"Average score: {average_score}")
   
    top_score = max(all_scores)
    top_players = [player['name'] for player in player_scores 
                   if player['score'] == top_score]
    top_player = top_players[0]
    
    top_achievement_count = max(achievement_counts.values())
    top_achievers = [name for name, count in achievement_counts.items() 
                    if count == top_achievement_count]
    
    print(f"Top performer: {top_player} ({top_score} points, "
          f"{achievement_counts[top_player]} achievements)")


if __name__ == "__main__":
    main()