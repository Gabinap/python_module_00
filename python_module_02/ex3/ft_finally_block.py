"""
Garden Guardian - Exercise 3: Finally Block - Always Clean Up

This module demonstrates the importance of the finally block for ensuring
cleanup operations always execute, even when errors occur during processing.

Functions:
    water_plants(plant_list): Waters plants and ensures cleanup with finally
    test_watering_system(): Demonstrates finally block behavior

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-02-01)
"""


def water_plants(plant_list):
    """
    Water a list of plants, ensuring the watering system is always closed.

    Args:
        plant_list (list): List of plant names to water

    Raises:
        TypeError: If a plant name is None or invalid
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise TypeError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Test the watering system with both normal and error scenarios.

    Demonstrates that the finally block always executes for cleanup,
    regardless of whether an error occurs.
    """
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("Watering completed successfully!")
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
