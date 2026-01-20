def ft_garden_summary() -> None:
    """
    Display a summary of garden information.

    Prompts user for garden name and number of plants,
    validates input, and displays a formatted summary.
    """
    while True:
        try:
            name = input("Enter garden name: ")
            if name == "":
                print("Please enter a name.")
                continue
            break
        except Exception as e:
            print(f"Error: {e}")

    while True:
        try:
            plants = int(input("Enter number of plants: "))
            if plants < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Value error, please enter a positive number.")

    print(f"Garden: {name}\nPlants: {plants}\nStatus: Growing well!")
