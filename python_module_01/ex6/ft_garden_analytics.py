"""
Module docstring.
Classes:
    Plant: Base plant class
    FloweringPlant: Plant with flowers
    PrizeFlower: Competition flower
    Garden: Individual garden manager
    GardenManager: Multi-garden system
Functions:
    main(): Demonstration program
Constants:
    DEFAULT_GROWTH_RATE: 1cm per day
Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-01)
"""


class Plant:
    """
    Represents a plant with basic attributes.
    Base class for all plant types in the garden system.
    """

    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """
        Initialize a new plant.
        Args:
            name: Name of the plant
            height: Initial height in cm (defaults to 0)
            age: Initial age in days (defaults to 0)
        """
        self.name = name
        self.height = height if height >= 0 else 0
        self.age = age if age >= 0 else 0

    def grow(self) -> None:
        """Make the plant grow by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_data(self) -> None:
        """Display complete plant information."""
        print(f"- {self.name}: {self.height}cm {self.age} days")


class FloweringPlant(Plant):
    """
    A flowering plant with color and blooming capability.
    Inherits from Plant and adds flower-specific features.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a flowering plant.
        Args:
            name: Name of the flower
            height: Height in cm
            age: Age in days
            color: Color of the flower
        """
        super().__init__(name, height, age)
        self.color = color
        self.blooming = True

    def bloom(self) -> None:
        """Make the flower bloom."""
        self.blooming = True
        print(f"{self.name} is blooming beautifully!")

    def unbloom(self) -> None:
        """Make the flower unbloom."""
        self.blooming = False
        print(f"{self.name} don't bloom anymore.")

    def get_data(self) -> None:
        """Display complete flower information including color."""
        status = "blooming" if self.blooming else "not blooming"
        print(
            f"- {self.name}: {self.height}cm, {self.age} days, {self.color} "
            f"flowers ({status})"
        )


class PrizeFlower(FloweringPlant):
    """
    A prize-winning flower with competition points.
    Inherits from FloweringPlant and adds exhibition features.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize_points: int = 0,
    ) -> None:
        """
        Initialize a prize flower.
        Args:
            name: Name of the flower
            height: Height in cm
            age: Age in days
            color: Color of the flower
            prize_points: Initial prize points (defaults to 0)
        """
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
        self.awards = []

    def earn_prize_points(
        self, points: int, reason: str = "exhibition"
    ) -> None:
        """
        Award competition points to the flower.
        Args:
            points: Number of points to award
            reason: Reason for the award (defaults to "exhibition")
        """
        self.prize_points += points
        self.awards.append(reason)
        print(f"{self.name} earned {points} prize points for {reason}!")

    def get_exhibition_info(self) -> str:
        """
        Get exhibition information string.
        Returns:
            Formatted string with flower exhibition details
        """
        status = "blooming" if self.blooming else "not blooming"
        return (
            f"- {self.name}: {self.height}cm, {self.color} "
            f"flowers ({status}), Prize points: {self.prize_points}"
        )

    def is_prize_worthy(self) -> bool:
        """
        Determine if flower deserves a prize.
        Returns:
            True if flower has 10+ points and is blooming
        """
        return self.prize_points >= 10 and self.blooming

    def get_data(self) -> None:
        """Display complete prize flower information."""
        print(self.get_exhibition_info())


class Garden:
    """
    Represents an individual garden with plants.
    Manages a collection of plants and tracks garden statistics.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a new garden.
        Args:
            name: Name of the garden owner
        """
        self.name = name
        self.plants = []
        self.total_growth = 0
        self.plants_added = 0

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden.
        Args:
            plant: Plant instance to add
        """
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all_plants(self) -> None:
        """Make all plants in the garden grow."""
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            initial_height = plant.height
            plant.grow()
            self.total_growth += plant.height - initial_height

    def calculate_score(self) -> int:
        """
        Calculate total garden score based on plant heights.
        Returns:
            Sum of all plant heights
        """
        return sum(plant.height for plant in self.plants)

    def get_plant_types_count(self) -> dict:
        """
        Count different types of plants in the garden.
        Returns:
            Dictionary with counts for regular, flowering,
            and prize plants
        """
        counts = {"regular": 0, "flowering": 0, "prize": 0}
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                counts["prize"] += 1
            elif isinstance(plant, FloweringPlant):
                counts["flowering"] += 1
            else:
                counts["regular"] += 1
        return counts

    def display_report(self) -> None:
        """Display complete garden report with all statistics."""
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_data()
        counts = self.get_plant_types_count()
        print(
            f"\nPlants added: {self.plants_added}, "
            f"Total growth: {self.total_growth}cm"
        )
        print(
            f"Plant types: {counts['regular']} regular, "
            f"{counts['flowering']} flowering, "
            f"{counts['prize']} prize flowers"
        )


class GardenManager:
    """
    Manages multiple gardens with analytics capabilities.
    Provides class-level and static utility methods for
    garden management.
    """

    total_gardens_created = 0

    class GardenStats:
        """
        Nested class for calculating garden statistics.
        Provides analytical functions for garden data.
        """

        def __init__(self, gardens: dict) -> None:
            """
            Initialize statistics calculator.
            Args:
                gardens: Dictionary of gardens to analyze
            """
            self.gardens = gardens

        def get_all_scores(self) -> dict:
            """
            Calculate scores for all gardens.
            Returns:
                Dictionary mapping garden names to scores
            """
            scores = {}
            for name, garden in self.gardens.items():
                scores[name] = garden.calculate_score()
            return scores

        def get_total_plants(self) -> int:
            """
            Count total plants across all gardens.
            Returns:
                Total number of plants in all gardens
            """
            total = 0
            for garden in self.gardens.values():
                total += len(garden.plants)
            return total

        @staticmethod
        def calculate_average(values: list) -> float:
            """
            Calculate average of a list of values.
            Args:
                values: List of numeric values
            Returns:
                Average value, or 0.0 if list is empty
            """
            if not values:
                return 0.0
            return sum(values) / len(values)

    def __init__(self) -> None:
        """Initialize a new garden manager."""
        self.gardens = {}
        GardenManager.total_gardens_created += 1

    def create_garden(self, garden_name: str) -> Garden:
        """
        Create a new garden.
        Args:
            garden_name: Name for the new garden
        Returns:
            The created Garden instance
        """
        garden = Garden(garden_name)
        self.gardens[garden_name] = garden
        return garden

    def add_plant_to_garden(self, garden_name: str, plant: Plant) -> None:
        """
        Add a plant to a specific garden.
        Args:
            garden_name: Name of the target garden
            plant: Plant instance to add
        """
        if garden_name not in self.gardens:
            self.create_garden(garden_name)
        self.gardens[garden_name].add_plant(plant)

    def display_all_scores(self) -> None:
        """Display scores for all managed gardens."""
        stats = self.GardenStats(self.gardens)
        scores = stats.get_all_scores()
        score_items = [f"{name}: {score}" for name, score in scores.items()]
        score_str = ", ".join(score_items)
        print(f"Garden scores - {score_str}")

    def display_summary(self) -> None:
        """Display summary of the garden management system."""
        print(f"Total gardens managed: {len(self.gardens)}")

    @classmethod
    def create_garden_network(cls, num_gardens: int = 2):
        """
        Class method to create a network of gardens.
        Args:
            num_gardens: Number of gardens to create (defaults to 2)
        Returns:
            New GardenManager instance with created gardens
        """
        network = cls()
        default_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        for i in range(min(num_gardens, len(default_names))):
            network.create_garden(default_names[i])
        print(f"Created garden network with {num_gardens} gardens")
        return network

    @staticmethod
    def validate_height(height: int) -> bool:
        """
        Validate that a height value is acceptable.
        Args:
            height: Height value to validate
        Returns:
            True if height is valid (positive and reasonable)
        """
        return height > 0 and height < 10000

    @staticmethod
    def is_valid_plant_name(name: str) -> bool:
        """
        Validate that a plant name is acceptable.
        Args:
            name: Plant name to validate
        Returns:
            True if name is valid (non-empty and reasonable length)
        """
        return len(name) > 0 and len(name) < 50


if __name__ == "__main__":
    print("=== Exotic Garden Management System Demo ===\n")

    # Create garden manager
    manager = GardenManager()

    # Kenji's Japanese Zen Garden
    kenji_garden = manager.create_garden("Kenji")
    # Ancient Japanese Maple bonsai
    japanese_maple = Plant("Acer palmatum 'Dissectum'", 45, 7300)
    kenji_garden.add_plant(japanese_maple)
    # Sacred lotus flower
    sacred_lotus = FloweringPlant("Nelumbo nucifera", 120, 90, "pink")
    kenji_garden.add_plant(sacred_lotus)
    # Prize-winning Black Pine bonsai
    kuromatsu = PrizeFlower("Pinus thunbergii", 60, 10950, "emerald", 25)
    kuromatsu.earn_prize_points(10, "Tokyo Bonsai Exhibition")
    kenji_garden.add_plant(kuromatsu)

    print()

    # Mariana's Tropical Paradise
    mariana_garden = manager.create_garden("Mariana")
    # Exotic pitcher plant
    nepenthes = Plant("Nepenthes rajah", 35, 547)
    mariana_garden.add_plant(nepenthes)
    # Bird of Paradise
    strelitzia = FloweringPlant("Strelitzia reginae", 150, 730, "orange")
    mariana_garden.add_plant(strelitzia)
    # Award-winning Blue Orchid
    blue_orchid = PrizeFlower("Vanda coerulea", 85, 1095, "azure", 18)
    blue_orchid.earn_prize_points(8, "International Orchid Show")
    mariana_garden.add_plant(blue_orchid)

    # Desert Mirage Conservatory
    desert_garden = manager.create_garden("Rashid")
    # Ancient Saguaro cactus
    saguaro = Plant("Carnegiea gigantea", 450, 36500)
    desert_garden.add_plant(saguaro)
    # Night-blooming Cereus
    cereus = FloweringPlant("Selenicereus grandiflorus", 200, 365, "white")
    desert_garden.add_plant(cereus)
    # Championship Lithops (living stones)
    lithops = PrizeFlower("Lithops karasmontana", 3, 1460, "grey-pink", 30)
    lithops.earn_prize_points(15, "Succulent World Championship")
    desert_garden.add_plant(lithops)

    print()

    # Grow plants in selected gardens
    print("=== Cultivation Cycle ===")
    kenji_garden.grow_all_plants()
    print()
    mariana_garden.grow_all_plants()

    # Display detailed reports
    kenji_garden.display_report()
    mariana_garden.display_report()
    desert_garden.display_report()

    # Test static methods
    print("\n=== Validation Tests ===")
    print(f"Height 450cm valid: {GardenManager.validate_height(450)}")
    print(
        f"Name 'Nepenthes rajah' valid: "
        f"{GardenManager.is_valid_plant_name('Nepenthes rajah')}"
    )

    # Display analytics
    print("\n=== Global Analytics ===")
    manager.display_all_scores()
    manager.display_summary()

    # Demonstrate class method
    print("\n=== Garden Network Creation ===")
    network = GardenManager.create_garden_network(3)
    network.display_summary()
