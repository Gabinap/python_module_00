def ft_count_harvest_recursive() -> None:
    """
    Count down days until harvest using recursion.

    Prompts user for number of days until harvest and
    displays a countdown using a recursive function.
    """
    while True:
        try:
            days = int(input("Days until harvest: "))
            if days < 0:
                print("Please enter a positive value.")
                continue
            break
        except ValueError:
            print("Value error, please enter a positive number.")

    def recursive(days: int) -> None:
        """
        Recursively print countdown days.

        Args:
            days: Number of days remaining
        """
        if days > 0:
            recursive(days - 1)
            print(f"Day {days}")

    recursive(days)
    print("Harvest time!")
