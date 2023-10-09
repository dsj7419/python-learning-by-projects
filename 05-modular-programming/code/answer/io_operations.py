def get_number(prompt):
    """
    Get a number input from the user.

    Parameters:
        prompt (str): The message displayed to the user.

    Returns:
        float: The number input by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operator():
    """
    Get an arithmetic operator from the user.

    Returns:
        str: The operator input by the user.
    """
    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        if operator in ["+", "-", "*", "/"]:
            return operator
        else:
            print("Invalid operator. Please enter +, -, *, or /.")

def display_result(result):
    """
    Display the result of the calculation to the user.

    Parameters:
        result (float or str): The result to be displayed.
    """
    print(f"Result: {result}")
