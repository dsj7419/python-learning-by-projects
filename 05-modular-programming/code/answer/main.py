import calculator
import io_operations

def main():
    """
    Main function to execute the calculator application.
    """
    print("Welcome to the Modular Calculator!")
    while True:
        # Get user inputs
        num1 = io_operations.get_number("Enter the first number: ")
        operator = io_operations.get_operator()
        num2 = io_operations.get_number("Enter the second number: ")
        
        # Perform calculation
        if operator == "+":
            result = calculator.add(num1, num2)
        elif operator == "-":
            result = calculator.subtract(num1, num2)
        elif operator == "*":
            result = calculator.multiply(num1, num2)
        elif operator == "/":
            # Handle division by zero
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = calculator.divide(num1, num2)
        
        # Display result
        io_operations.display_result(result)
        
        # Check if user wants to perform another calculation
        another = input("Do you want to perform another calculation? (yes/no): ")
        if another.lower() != "yes":
            print("Thank you for using the Modular Calculator!")
            break

if __name__ == "__main__":
    main()
