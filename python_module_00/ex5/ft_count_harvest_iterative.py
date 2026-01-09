def ft_count_harvest_iterative() -> None:
    """
    Count down days until harvest using iteration.

    Prompts user for number of days until harvest and
    displays a countdown using a for loop.
    """
    while True:
        try:
            days = int(input("Days until harvest: "))
            if days < 0:
                print("Please enter a positive value")
                continue
            break
        except ValueError:
            print("Value error, please enter a positive number.")

    for i in range(days):
        print(f"Day {i + 1}")
    print("Harvest time!")

if __name__ == "__main__":
    ft_count_harvest_iterative()
