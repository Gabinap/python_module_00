def ft_water_reminder() -> None:
    """
    Remind user to water plants based on days since last watering.

    Prompts user for number of days since last watering and
    displays appropriate message (> 2 days: water needed).
    """
    while True:
        try:
            days = int(input("Days since last watering: "))
            if days < 0:
                print("Please enter a positive value")
                continue
            if days > 2:
                print("Water the plants!")
                return
            print("Plants are fine")
            return
        except ValueError:
            print("Input error, please enter a positive number.")
