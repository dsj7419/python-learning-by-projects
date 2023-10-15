import random  # Importing the module needed to make random choices

# A list of possible answers that the Magic 8-Ball can give
answers = [
    "Yes, definitely.", "Reply hazy, try again.",
    "Ask again later.", "Cannot predict now.",
    "Don't count on it.", "My sources say no.",
    "Outlook not so good.", "Very doubtful."
]

# Asking the user to input a question
user_question = input("Ask the Magic 8-Ball a question: ")

# Checking if the user's input ends with a question mark
if user_question.strip().endswith("?"):
    # If valid, randomly select an answer from the list
    selected_answer = random.choice(answers)
    # Display the chosen answer
    print("\nMagic 8-Ball says:", selected_answer)
else:
    # If invalid, display an error message
    print("\nPlease ask a valid question (ending with '?').")
