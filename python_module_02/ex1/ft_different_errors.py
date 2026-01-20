"""
Garden Guardian - Exercise 1: Different Types of Problems

This module demonstrates handling different types of errors that can occur
in garden operations: ValueError, ZeroDivisionError, FileNotFoundError,
and KeyError.

Functions:
    garden_operations(operation_type): Triggers different types of errors
                                       based on operation_type
    test_error_types(): Demonstrates catching and handling each error type

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-02-01)
"""


def garden_operations(operation_type):
    """
    Perform a garden operation that may trigger different types of errors.

    Args:
        operation_type (str): Type of operation to perform
                             ('value', 'division', 'file', 'key', 'multiple')

    Raises:
        ValueError: When invalid data is provided
        ZeroDivisionError: When division by zero is attempted
        FileNotFoundError: When a file doesn't exist
        KeyError: When a dictionary key is not found
    """
    garden_data = {
        "tomato": {"water": 5, "sunlight": 8},
        "lettuce": {"water": 7, "sunlight": 6},
        "carrots": {"water": 4, "sunlight": 9},
    }

    if operation_type == "value":
        temperature = int("abc")
        print(f"Temperature: {temperature}")

    elif operation_type == "division":
        plants_count = 10
        sections = 0
        plants_per_section = plants_count / sections
        print(f"Plants per section: {plants_per_section}")

    elif operation_type == "file":
        with open("missing.txt") as f:
            data = f.read()
            print(f"File data: {data}")

    elif operation_type == "key":
        plant_info = garden_data["missing_plant"]
        print(f"Plant info: {plant_info}")

    elif operation_type == "multiple":
        user_input = "invalid"
        value = int(user_input)
        print(f"Value: {value}")


def test_error_types():
    """
    Test and demonstrate handling of different error types.

    This function tests ValueError, ZeroDivisionError, FileNotFoundError,
    and KeyError, showing how to catch each individually and together.
    """
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("division")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()

    print("Testing multiple errors together...")
    error_types = ["value", "division", "file", "key"]

    for error_type in error_types:
        try:
            garden_operations(error_type)
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
