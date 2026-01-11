"""
Data Quest - Exercise 1: Score Cruncher
This module demonstrates list operations for score analytics. Processes player
scores from command-line arguments, calculates statistics (total, average,
hight, low, range), and handles invalid input gracefully.

Functions:
    main: Process player scores and display analytics

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-05)
"""

import sys


def ft_score_analytics():
    """
    Process player scores from command-line arguments and display analytics.
    
    Reads scores from sys.argv, converts them to integers, and calculates
    comprehensive statistics including total, average, high score, low score,
    and score range. Invalid inputs are gracefully skipped with warnings.
    
    The function uses lists to store and process scores, demonstrating basic
    list operations and built-in functions for statistical analysis.
    
    Returns:
        None: Prints analytics directly to stdout
        
    Examples:
        $ python3 ft_score_analytics.py 1500 2300 1800 2100 1950
        === Player Score Analytics ===
        Scores processed: [1500, 2300, 1800, 2100, 1950]
        Total players: 5
        Total score: 9650
        Average score: 1930.0
        High score: 2300
        Low score: 1500
        Score range: 800
    """
    user_args = sys.argv[1:]

    print("=== Player Score Analytics ===")

    if len(user_args) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
                " <score1> <score2> ...")
        return

    scores = []
    for arg in user_args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Warning: '{arg}' is not a valid score. Skipping...")

    if len(scores) == 0:
        print("No valid scores to process.")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
