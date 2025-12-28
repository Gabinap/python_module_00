def ft_plant_age() -> None:
    """
    Check if a plant is ready to harvest based on its age.

    Prompts user for plant age in days and indicates whether
    the plant is ready to harvest (> 60 days) or needs more time.
    """
    while True:
        try:
            age = int(input("Enter plant age in days: "))
            if age < 0:
                print("Please enter a positive value.")
                continue
            if age > 60:
                print("Plant is ready to harvest!")
                return
            print("Plant needs more time to grow.")
            return
        except ValueError:
            print("Input error, please enter a positive number.")
