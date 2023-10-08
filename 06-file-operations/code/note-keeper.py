# Constants for the file name and options
NOTES_FILE = "notes.txt"

while True:
    # Display available options and get user choice
    print("\nOptions:")
    print("1. Add a note")
    print("2. View notes")
    print("3. Delete a note")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # TODO: Add a new note
        # 1. Use input() to get the note from the user.
        # 2. Use open() in append mode ('a') to add the note to the file.

        pass  # This is a placeholder. Remove this line when you add your code.

    elif choice == "2":
        # TODO: View all notes
        # 1. Use open() in read mode ('r') to get the notes from the file.
        # 2. Use a loop to display each note.

        pass

    elif choice == "3":
        # TODO: Delete a note
        # 1. Use open() in read mode ('r') to get the notes from the file.
        # 2. Display each note with a number next to it.
        # 3. Use input() to get the number of the note to delete from the user.
        # 4. Use open() in write mode ('w') to save the notes back to the file, excluding the deleted one.

        pass

    elif choice == "4":
        # Exit
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
