# Personalized Greeting Card Generator

# Get user's name
name = input("Enter your name: ")

# Get user's age and validate the input
age_str = input("Enter your age: ")

# Basic Input Validation: Ensure age is a digit
while not age_str.isdigit():
    print("Invalid input. Please enter a number.")
    age_str = input("Enter your age: ")

# Type Conversion: Convert age to integer
age = int(age_str)

# Generate a personalized greeting card
print("\n🎉 Happy Birthday, " + name + "! 🎉")
print("Congratulations on turning", age, "years old!")
print("May your year be filled with joy, adventures, and splendid memories!")

# Additional message based on age
if age < 18:
    print("Enjoy your youth and every little discovery that comes your way!")
elif age < 30:
    print("Embrace the vigor of your 20s and make the most out of it!")
elif age < 50:
    print("Keep exploring, learning, and enjoying every moment!")
else:
    print("May you continue to inspire others with your wisdom and experiences!")

# Closing message
print("\nWishing you a day as wonderful as you are!")
