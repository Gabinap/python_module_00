"""
Garden Guardian - Exercise 5: Garden Management System

This module demonstrates a complete garden management system that combines
all error handling techniques: custom exceptions, try/except/finally blocks,
error raising, and graceful error recovery.

Classes:
    GardenError: Base exception for garden-related problems
    PlantError: Exception for plant-specific issues
    WaterError: Exception for water-related issues
    GardenManager: Main class managing garden operations

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

    pass


class WaterError(GardenError):
    """Exception raised for watering-related problems."""

    pass


class GardenManager:
    """
    Manages garden operations with robust error handling.

    Attributes:
        plants (dict): Dictionary storing plant information
        water_tank (int): Current water tank level (0-100)
    """

    def __init__(self):
        """Initialize garden manager with empty plant list and full tank."""
        self.plants = {}
        self.water_tank = 100

    def add_plant(self, name, water_need=5, sun_need=8):
        """
        Add a plant to the garden.

        Args:
            name (str): Plant name
            water_need (int): Water level needed (1-10)
            sun_need (int): Sunlight hours needed (2-12)

        Raises:
            PlantError: If plant name is empty or invalid
        """
        if not name or name.strip() == "":
            raise PlantError("Plant name cannot be empty!")

        self.plants[name] = {
            'water': water_need,
            'sun': sun_need,
            'healthy': True
        }
        print(f"Added {name} successfully")

    def water_plants(self):
        """
        Water all plants in the garden.

        Uses try/except/finally to ensure watering system is always closed.

        Raises:
            WaterError: If water tank is empty
        """
        if self.water_tank < 20:
            raise WaterError("Not enough water in tank")

        print("Opening watering system")

        try:
            for plant_name in self.plants.keys():
                print(f"Watering {plant_name} - success")
                self.water_tank -= 5
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name):
        """
        Check and display health status of a specific plant.

        Args:
            plant_name (str): Name of the plant to check

        Raises:
            PlantError: If plant doesn't exist
            ValueError: If plant parameters are invalid
        """
        if plant_name not in self.plants:
            raise PlantError(f"Plant '{plant_name}' not found in garden")

        plant = self.plants[plant_name]
        water = plant['water']
        sun = plant['sun']

        if water < 1 or water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")

        if sun < 2 or sun > 12:
            raise ValueError(f"Sunlight hours {sun} is invalid")

        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")

    def get_status(self):
        """
        Display current garden status.

        Returns:
            str: Status message with plant count and water level
        """
        return (f"Garden has {len(self.plants)} plants, "
                f"water tank: {self.water_tank}%")


def test_garden_management():
    """
    Test the complete garden management system.

    Demonstrates all error handling techniques working together:
    - Custom exceptions for domain-specific errors
    - Try/except for error recovery
    - Finally blocks for cleanup
    - Raising errors for validation
    - Continuing execution after errors
    """
    print("=== Garden Management System ===\n")

    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
    except PlantError as e:
        print(f"Error: {e}")

    try:
        garden.add_plant("lettuce", 7, 6)
    except PlantError as e:
        print(f"Error: {e}")

    try:
        garden.add_plant("", 5, 8)
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print()

    print("Watering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Error: {e}")
    print()

    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato")
    except (PlantError, ValueError) as e:
        print(f"Error: {e}")

    garden.plants["lettuce"]["water"] = 15

    try:
        garden.check_plant_health("lettuce")
    except (PlantError, ValueError) as e:
        print(f"Error checking lettuce: {e}")
    print()

    print("Testing error recovery...")
    garden.water_tank = 10
    try:
        garden.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
