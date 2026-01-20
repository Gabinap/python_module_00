class Plant:
    """
    Represent a plant with its characteristics
    """

    def __init__(
        self, name: str, height: int, plant_age: int, grow_step: int = 1
    ) -> None:
        """
        Initialize a new plant

        Args:
            name: Name of the plant
            height: Height of the plant
            age: Age of the plant
            grow_step: how much a plant grow after 1 day (default: 1)
        """
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.grow_step = grow_step

    def grow(self):
        """
        make a plant growing
        """
        self.height += self.grow_step

    def age(self):
        """
        Add one day for a plant
        """
        self.plant_age += 1
        self.grow()

    def get_info(self):
        """
        show plant information
        """
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    """
    make a plant growth by 30 days
    """
    basic_height = 43
    bamboo = Plant("Bamboo", basic_height, 22, 5)
    print("=== Day 1 ===")
    bamboo.get_info()
    for _i in range(30):
        bamboo.age()
    print("=== Day 31 ===")
    bamboo.get_info()
    print(f"Growth this month: {bamboo.height - basic_height}")
