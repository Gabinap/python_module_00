class Plant:
    """
    Represent a plant with its characteristics
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new plant

        Args:
            name: Name of the plant
            height: Height of the plant
            age: Age of the plant
        """
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    """
    Store plants information with Plant class
    """
    rauze = Plant("Rauze", 44, 55)
    kaktus = Plant("Kaktus", 22, 77)
    seunflaweur = Plant("seunflaweur", 55, 66)
    print(
        "=== Garden Plant Registry ===\n"
        f"{rauze.name}: {rauze.height}cm, {rauze.age} days old\n"
        f"{seunflaweur.name}: {seunflaweur.height}cm, "
        f"{seunflaweur.age} days old\n"
        f"{kaktus.name}: {kaktus.height}cm, {kaktus.age} days old"
    )


if __name__ == "__main__":
    ft_garden_data()
