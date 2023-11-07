# Import required modules
import string
import secrets
import base64
import json
import os

# Define a function to generate a secure random password
def generate_password(length, use_digits=True, use_special_chars=True):
    """Generate a secure random password."""
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

# Define encryption and decryption functions
def encrypt_password(password, key):
    """Encrypt the password using base64 encoding."""
    # Create a bytes object from the password using UTF-8 encoding
    encoded_password = password.encode('utf-8')
    # Encrypt the bytes object using base64
    encrypted_password = base64.b64encode(encoded_password)
    # Return the encrypted password with the key prefix
    return key + encrypted_password.decode('utf-8')

def decrypt_password(encrypted_password, key):
    """Decrypt the encrypted password."""
    # Remove the key prefix from the encrypted password
    encrypted_password = encrypted_password.replace(key, '', 1)
    # Decode the base64 encoded password
    decrypted_password = base64.b64decode(encrypted_password)
    return decrypted_password.decode('utf-8')

# Function to save a password
def save_password(label, password, filename="passwords.json", key="secret"):
    """Save the password with a label."""
    # Check if passwords file already exists
    if os.path.exists(filename):
        # Read existing passwords
        with open(filename, 'r') as file:
            passwords = json.load(file)
    else:
        passwords = {}

    # Encrypt the password
    encrypted_password = encrypt_password(password, key)
    # Save or update the password for the label
    passwords[label] = encrypted_password

    # Write the updated passwords back to the file
    with open(filename, 'w') as file:
        json.dump(passwords, file)

# Function to retrieve a password
def retrieve_password(label, filename="passwords.json", key="secret"):
    """Retrieve the password for a given label."""
    try:
        # Read the passwords file
        with open(filename, 'r') as file:
            passwords = json.load(file)
        # Decrypt the password
        encrypted_password = passwords.get(label, None)
        if encrypted_password:
            return decrypt_password(encrypted_password, key)
        else:
            return "Password not found for this label."
    except FileNotFoundError:
        return "Password file not found. Please store a password first."

# Main function to handle user interaction
def main_menu():
    """The main menu for the password manager application."""
    while True:
        print("\nWelcome to the Password Manager")
        print("1. Generate a new password")
        print("2. Retrieve an existing password")
        print("3. Store a new password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Generate a new password
            length = int(input("Enter the desired password length: "))
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
            new_password = generate_password(length, use_digits, use_special_chars)
            print(f"\nGenerated Password: {new_password}")
            label = input("Please provide a label for this password: ")
            save_password(label, new_password)
            print("Password saved successfully.")
        elif choice == '2':
            # Retrieve an existing password
            label = input("Enter the label for the password you want to retrieve: ")
            password = retrieve_password(label)
            print(f"Password for '{label}': {password}")
        elif choice == '3':
            # Store a new password
            label = input("Enter a label for your password: ")
            password = input("Enter your password: ")
            save_password(label, password)
            print("Password stored successfully.")
        elif choice == '4':
            # Exit the program
            print("Thank you for using the Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
