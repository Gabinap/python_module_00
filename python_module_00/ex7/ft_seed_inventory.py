def ft_seed_inventory(plant: str, number: int, unit_type: str) -> None:
    """
    Display seed inventory information.

    Args:
        plant: Name of the plant
        number: Quantity of seeds
        unit_type: Type of unit (packets/grams/area/other)
    """
    messages = {
        "packets": f"{plant.capitalize()} seeds: {number} packets available",
        "grams": f"{plant.capitalize()} seeds: {number} grams total",
        "area": f"{plant.capitalize()} seeds: covers {number} square meters",
    }

    message = messages.get(unit_type, "Unknown unit type")

    print(message)
