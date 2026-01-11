class Plant:
    """
    Represents a plant with secured data validation.

    Protects plant data from corruption by validating all inputs
    and rejecting negative values for height and age.
    """
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """
        Initialize a new secure plant with validated data.

        Args:
            name: Name of the plant
            height: Initial height in cm (defaults to 0)
            age: Initial age in days (defaults to 0)
        """
        self.name = name
        self.height = height if height >= 0 else 0
        self.age = age if age >= 0 else 0

    def set_height(self, height: int) -> None:
        """
        Set the plant's height with validation.

        Args:
            height: New height value in cm

        Note:
            Rejects negative values and prints an error message
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, age: int) -> None:
        """
        Set the plant's age with validation.

        Args:
            age: New age value in days

        Note:
            Rejects negative values and prints an error message
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {self.age} days [OK]")

    def get_data(self) -> None:
        """
        Display complete plant information.

        Prints the plant's name, height, and age in a formatted string.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def get_height(self) -> int:
        """Get the plant's current height."""
        return self.height

    def get_age(self) -> int:
        """Get the plant's current age."""
        return self.age


class Flower(Plant):
    """
    A flower with color and blooming capability.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a flower with Plant attributes and color.

        Args:
            name: Name of the flower
            height: Height in cm
            age: Age in days
            color: Color of the flower
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        Make the flower bloom.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_data(self) -> None:
        """
        Display complete flower information including color.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old, "
              f"{self.color} color")


class Tree(Plant):
    """
    A tree with trunk diameter and shade production capability.
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Initialize a tree with Plant attributes and trunk diameter.

        Args:
            name: Name of the tree
            height: Height in cm
            age: Age in days
            trunk_diameter: Diameter of the trunk in cm
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculate and display the shade produced by the tree.
        """
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def get_data(self) -> None:
        """
        Display complete tree information including trunk diameter.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old, "
              f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    A vegetable with harvest season and nutritional value.
    """

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Initialize a vegetable with Plant attributes and nutrition info.

        Args:
            name: Name of the vegetable
            height: Height in cm
            age: Age in days
            harvest_season: Season for harvesting
            nutritional_value: Main nutritional benefit
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition_info(self) -> None:
        """
        Display nutritional information.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_data(self) -> None:
        """
        Display complete vegetable information.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old, "
              f"{self.harvest_season}")


if __name__ == "__main__":
    """
    several tests
    """
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    rose.get_data()
    rose.bloom()
    print()

    tulip = Flower("Plum blossom", 56, 706, "pink")
    tulip.get_data()
    tulip.bloom()
    print()

    oak = Tree("Oak", 500, 1825, 50)
    oak.get_data()
    oak.produce_shade()
    print()

    bamboo = Tree("Bamboo", 80, 77, 5)
    bamboo.get_data()
    bamboo.produce_shade()
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    tomato.get_data()
    tomato.get_nutrition_info()
    print()

    lettuce = Vegetable("Lettuce", 10, 30, "spring harvest", "fiber")
    lettuce.get_data()
    lettuce.get_nutrition_info()
