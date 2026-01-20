"""
Data Quest - Exercise 2: Position Tracker
This module demonstrates tuple operations for 3D coordinate management.
Creates immutable 3D positions, calculates Euclidean distances, parses
coordinate strings, and showcases tuple unpacking techniques.

Functions:
    calculate_distance: Calculate 3D Euclidean distance between two points
    parse_coordinates: Parse coordinate string into tuple
    main: Demonstrate coordinate system operations

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-05)
"""

import math


def calculate_distance(pos1, pos2):
    """
    Calculate the 3D Euclidean distance between two positions.

    Uses the formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)

    Args:
        pos1: Tuple of (x, y, z) coordinates for first position
        pos2: Tuple of (x, y, z) coordinates for second position

    Returns:
        float: The Euclidean distance between the two points

    Examples:
        >>> calculate_distance((0, 0, 0), (3, 4, 0))
        5.0
    """
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def parse_coordinates(coord_string):
    """
    Parse a coordinate string into a 3D position tuple.

    Expects format "x,y,z" where x, y, z are numeric values.

    Args:
        coord_string: String containing coordinates separated by commas

    Returns:
        tuple: Parsed (x, y, z) coordinates as integers

    Raises:
        ValueError: If string format is invalid or contains non-numeric values

    Examples:
        >>> parse_coordinates("3,4,0")
        (3, 4, 0)
    """
    parts = coord_string.split(",")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main():
    """
    Demonstrate 3D coordinate system operations with tuples.

    Showcases tuple creation, distance calculation, coordinate parsing,
    error handling, and tuple unpacking techniques.

    Returns:
        None: Prints demonstrations directly to stdout
    """
    print("=== Game Coordinate System ===")
    print()

    position = (10, 20, 5)
    print(f"Position created: {position}")
    origin = (0, 0, 0)
    dist = calculate_distance(origin, position)
    print(f"Distance between {origin} and {position}: {dist:.2f}")
    print()

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    try:
        parsed_pos = parse_coordinates(coord_str)
        print(f"Parsed position: {parsed_pos}")
        dist = calculate_distance(origin, parsed_pos)
        print(f"Distance between {origin} and {parsed_pos}: {dist}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print()

    invalid_coord = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_coord}"')
    try:
        parsed_pos = parse_coordinates(invalid_coord)
        print(f"Parsed position: {parsed_pos}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print()

    print("Unpacking demonstration:")
    demo_pos = (3, 4, 0)
    x, y, z = demo_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
