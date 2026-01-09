"""
Garden Guardian - Exercise 2: Making Your Own Error Types

This module demonstrates creating custom exception types for garden-specific
problems. It includes a base GardenError and specialized errors for plants
and watering issues.

Classes:
    GardenError: Base exception for all garden-related problems
    PlantError: Exception for plant-specific problems
    WaterError: Exception for watering-related problems

Functions:
    check_plant_status(plant_name): Raises PlantError for wilting plants
    check_water_tank(tank_level): Raises WaterError for low water levels
    test_custom_errors(): Demonstrates using custom exceptions

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-02-01)
"""


class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-specific problems."""

    def __init__(self, plant_name, problem):
        """
        Initialize PlantError with plant details.

        Args:
            plant_name (str): Name of the plant with issues
            problem (str): Description of the plant problem
        """
        self.plant_name = plant_name
        self.problem = problem
        message = f"The {plant_name} plant {problem}!"
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for watering-related problems."""

    def __init__(self, issue):
        """
        Initialize WaterError with water issue details.

        Args:
            issue (str): Description of the water problem
        """
        self.issue = issue
        message = f"{issue}!"
        super().__init__(message)


def check_plant_status(plant_name):
    """
    Check the status of a plant and raise PlantError if there's a problem.

    Args:
        plant_name (str): Name of the plant to check

    Raises:
        PlantError: If the plant is wilting or has issues
    """
    if plant_name == "tomato":
        raise PlantError(plant_name, "is wilting")
    elif plant_name == "lettuce":
        raise PlantError(plant_name, "has yellow leaves")
    else:
        print(f"{plant_name} is healthy!")


def check_water_tank(tank_level):
    """
    Check water tank level and raise WaterError if insufficient.

    Args:
        tank_level (int): Current water level (0-100)

    Raises:
        WaterError: If water level is too low
    """
    if tank_level < 20:
        raise WaterError("Not enough water in the tank")
    elif tank_level < 0:
        raise WaterError("Water tank is empty")
    else:
        print(f"Water tank level is good: {tank_level}%")


def test_custom_errors():
    """
    Test and demonstrate custom exception handling.

    This function shows how to:
    - Raise custom exceptions
    - Catch specific exception types
    - Catch all garden errors with the base class
    """
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant_status("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        check_water_tank(10)
    except WaterError as e:
        print(f"Caught WaterError: {e.message}")
    print()

    print("Testing catching all garden errors...")
    errors_to_test = [
        ("tomato", None),
        (None, 5)
    ]

    for plant, water_level in errors_to_test:
        try:
            if plant:
                check_plant_status(plant)
            else:
                check_water_tank(water_level)
        except GardenError as e:
            print(f"Caught a garden error: {e.message}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
