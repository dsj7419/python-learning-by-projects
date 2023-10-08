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
        # Add a new note
        note = input("Enter your note: ")
        with open(NOTES_FILE, "a") as file:
            file.write(note + "\n")
        print("Note added!")

    elif choice == "2":
        # View all notes
        try:
            with open(NOTES_FILE, "r") as file:
                notes = file.readlines()
                if not notes:
                    print("No notes available.")
                else:
                    print("\nNotes:")
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note.strip()}")
        except FileNotFoundError:
            print("No notes available.")

    elif choice == "3":
        # Delete a note
        try:
            with open(NOTES_FILE, "r") as file:
                notes = file.readlines()
                if not notes:
                    print("No notes available.")
                else:
                    print("\nNotes:")
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note.strip()}")
                    note_num = int(input("Enter the number of the note to delete: "))
                    if 0 < note_num <= len(notes):
                        del notes[note_num - 1]
                        with open(NOTES_FILE, "w") as file:
                            file.writelines(notes)
                        print("Note deleted!")
                    else:
                        print("Invalid note number.")
        except FileNotFoundError:
            print("No notes available.")

    elif choice == "4":
        # Exit
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
