"""
Module docstring.
Functions:
    check_temperature(temp_str: str): verifie validity of the temperature
    main(): Demonstration program
Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-02-01)
"""


def check_temperature(temp_str: str):
    """
    Validates temperature input and checks if it's suitable for plants.

    Args:
        temp_str: Temperature value as string

    Returns:
        Temperature value if valid, None otherwise
    """
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return None
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return None
    print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input():
    """
    Demonstrates temperature validation with various test cases.
    """
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    check_temperature('25')
    print("\nTesting temperature: abc")
    check_temperature('abc')
    print("\nTesting temperature: 100")
    check_temperature('100')
    print("\nTesting temperature: -50")
    check_temperature('-50')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
