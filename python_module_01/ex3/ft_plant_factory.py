class Plant:
    """
    Represent a plant with its characteristics
    """

    def __init__(
        self,
        name: str,
        height: int = 0,
        plant_age: int = 0,
        grow_step: int = 1,
    ) -> None:
        """
        Initialize a new plant

        Args:
            name: Name of the plant
            height: Height of the plant (default: 0)
            age: Age of the plant (default: 0)
            grow_step: how much a plant grow after 1 day (default: 1)
        """

        self.name = name
        self.height = height
        self.plant_age = plant_age
        if grow_step < 0.001:
            self.grow_step = 1
        else:
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
    create and display 5 differents plants
    """

    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 9, 30, 1)
    print(f"Created: {rose.name} ({rose.height}cm, {rose.plant_age} days)")

    bamboo = Plant("Wallah", 89, 3000, 3000000)
    print(
        f"Created: {bamboo.name} ({bamboo.height}cm, {bamboo.plant_age} days)"
    )

    orange = Plant("feliation")
    print(
        f"Created: {orange.name} ({orange.height}cm, {orange.plant_age} days)"
    )

    poire = Plant("Rose")
    print(f"Created: {poire.name} ({poire.height}cm, {poire.plant_age} days)")

    poire = Plant("Amandier", 2, 44)
    print(f"Created: {poire.name} ({poire.height}cm, {poire.plant_age} days)")

    print("Total plant created: 5")
