import random  # Importing the random module

# Predefined list of possible answers
answers = [
    "Yes, definitely.", "Reply hazy, try again.",
    "Ask again later.", "Cannot predict now.",
    "Don't count on it.", "My sources say no.",
    "Outlook not so good.", "Very doubtful."
]

# Prompt the user for input
user_question = input("Ask the Magic 8-Ball a question: ")

# Validate the input: Ensure it ends with a question mark
if user_question.strip().endswith("?"):
    # Randomly select an answer
    selected_answer = random.choice(answers)
    # Display the answer
    print("\\nMagic 8-Ball says:", selected_answer)
else:
    print("\\nPlease ask a valid question (ending with '?').")
