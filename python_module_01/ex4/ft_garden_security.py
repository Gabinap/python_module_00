class SecurePlant:
    """
    Represents a plant with secured data validation.

    Protects plant data from corruption by validating all inputs
    and rejecting negative values for height and age.
    """

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """
        Initialize SecurePlant with validated name, height and age.

        Negative values for height and age are converted to 0.
        """
        self.name = name
        self.height = height if height >= 0 else 0
        self.age = age if age >= 0 else 0

    def set_height(self, height: int) -> None:
        """
        Initialize a new secure plant with validated data.

        Args:
            name: Name of the plant
            height: Initial height in cm (defaults to 0). Negative values
                are set to 0.
        """
        if height < 0:
            print(f"Invalid operation attempted {height} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height update: {self.height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Set the plant's age with validation.

        Args:
            age: New age value in days

        Note:
            Rejects negative values and prints an error message
        """
        if age < 0:
            print(f"Invalid operation attempted {age} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age update: {self.age} days [OK]")

    def get_plant(self) -> None:
        """
        Display complete plant information.

        Prints the plant's name, height, and age in a formatted string.
        """
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")

    def get_height(self) -> None:
        """
        Display the plant's current height.
        """
        print(f"Plant height: {self.height}")

    def get_age(self) -> None:
        """
        Display the plant's current age.
        """
        print(f"Plant age: {self.age}")


if __name__ == "__main__":
    """
    several tests
    """
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print(f"Plant created: {plant.name}")
    plant.set_height(35)
    plant.set_age(77)
    print("\n")
    plant.set_height(-2)
    plant.set_age(-88)
    print("\n")
    plant.get_plant()
