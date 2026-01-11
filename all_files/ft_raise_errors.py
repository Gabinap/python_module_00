"""
Garden Guardian - Exercise 4: Raising Your Own Errors

This module demonstrates how to validate input and raise appropriate errors
with helpful messages when validation fails.

Functions:
    check_plant_health(plant_name, water_level, sunlight_hours): Validates
        plant parameters and raises errors for invalid values
    test_plant_checks(): Tests validation with good and bad inputs

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-02-01)
"""


def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validate plant health parameters and raise errors for invalid values.

    Args:
        plant_name (str): Name of the plant (cannot be empty)
        water_level (int): Water level from 1 to 10
        sunlight_hours (int): Daily sunlight hours from 2 to 12

    Returns:
        str: Success message if all parameters are valid

    Raises:
        ValueError: If plant_name is empty
        ValueError: If water_level is outside 1-10 range
        ValueError: If sunlight_hours is outside 2-12 range
    """
    if not plant_name or plant_name.strip() == "":
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        else:
            raise ValueError(f"Water level {water_level} is too low (min 1)")

    if sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        else:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    Test plant health validation with various inputs.

    Demonstrates raising and catching ValueError for different invalid inputs:
    - Empty plant names
    - Water levels outside valid range
    - Sunlight hours outside valid range
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing empty plant name...")
    try:
        result = check_plant_health("", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad water level...")
    try:
        result = check_plant_health("tomato", 15, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad sunlight hours...")
    try:
        result = check_plant_health("tomato", 5, 0)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
