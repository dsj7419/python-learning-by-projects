# Importing regular expression library
import re

# Defining a flag for the while loop
data_entry_complete = False

# Main loop for data entry system
while not data_entry_complete:
    # Try block to catch exceptions
    try:
        # User input: Name
        name = input("Enter your name: ")
        if not re.match("^[a-zA-Z\s]*$", name):
            raise ValueError("Name must contain only letters and spaces.")
        
        # User input: Age
        age = input("Enter your age: ")
        # Check if the age is a positive integer
        if not age.isdigit() or int(age) <= 0:
            raise ValueError("Age must be a positive integer.")
        
        # User input: Email
        email = input("Enter your email: ")
        # Check if the email is in a valid format
        if not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            raise ValueError("Email must be in a valid format.")
        
        # If all inputs are valid, exit the loop
        data_entry_complete = True

    # Except block to handle invalid inputs
    except ValueError as e:
        print(f"Invalid input: {str(e)}")
        print("Please enter the data again.\n")

# Displaying entered data
print("\nData Entry Complete!")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")
