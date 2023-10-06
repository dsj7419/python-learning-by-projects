import sys

print("Welcome to the Adventure Game!")
print("You find yourself in a dark room with two doors.")
print("Choose wisely, for one door leads to safety, and the other to doom.\n")

# Main game loop
while True:
    # Choose a door
    door = ""
    while door.lower() not in ["1", "2"]:
        print("Do you go through door 1 or door 2?")
        door = input("> ")
        if door.lower() not in ["1", "2"]:
            print("Invalid choice. Please choose door 1 or door 2.\n")
    
    # Determine the outcome
    if door == "1":
        print("\nYou find yourself in a sunny meadow filled with flowers.")
        print("Congratulations! You found the way to safety.")
    else:
        print("\nYou are greeted by a hungry lion.")
        print("Sorry, you will not make it out alive.")
    
    # Play again?
    play_again_choice = ""
    while play_again_choice.lower() not in ["yes", "no"]:
        print("\nWould you like to play again? (yes/no)")
        play_again_choice = input("> ")
        if play_again_choice.lower() not in ["yes", "no"]:
            print("Invalid choice. Please answer with 'yes' or 'no'.")
    
    # Exit if the user doesn't want to play again
    if play_again_choice.lower() == "no":
        print("Thank you for playing! Goodbye.")
        sys.exit()  # Exits the program
