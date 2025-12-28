def ft_harvest_total() -> None:
    """
    Calculate and display the total harvest over three days.

    Prompts user for harvest amounts for days 1, 2, and 3,
    validates input, and displays the total.
    """
    def ask(nb: int) -> int:
        """
        Ask for harvest amount for a specific day.

        Args:
            nb: The day number

        Returns:
            The harvest amount entered by the user
        """
        while True:
            try:
                picked = int(input(f"Day {nb} harvest: "))
                if picked < 0:
                    print("Please enter a positive value.")
                    continue
                return picked
            except ValueError:
                print("Invalid input, please enter a number.")

    first = ask(1)
    second = ask(2)
    third = ask(3)
    print(f"Total harvest: {first + second + third}")
