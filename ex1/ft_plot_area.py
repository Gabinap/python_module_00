def ft_plot_area() -> None:
    """
    Calculate and display the area of a garden plot.

    Prompts user for length and width, validates input,
    and displays the calculated area.
    """
    def get_positive_int(prompt: str) -> int:
        """
        Get a positive integer from user input.

        Args:
            prompt: The message to display to the user

        Returns:
            A positive integer entered by the user
        """
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    print("Please enter a positive number")
                    continue
                return value
            except ValueError:
                print("Invalid input, please enter a number")
    x = get_positive_int("Enter length: ")
    y = get_positive_int("Enter width: ")
    print(f"Plot area: {x * y}")
