
# Chapter 1: Getting Started with Python

Welcome to the exciting journey of learning Python through hands-on projects! 🚀 In this initial chapter, we'll set up our Python development environment, write our first Python script, and dive into our first mini-project!

## Table of Contents

- [Introduction](#introduction)
- [Environment Setup](#environment-setup)
  - [Installing Python](#installing-python)
  - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Installing an IDE](#installing-an-ide)
- [Your First Python Script: Hello, World!](#your-first-python-script-hello-world)
- [Project: Magic 8-Ball Simulator](#project-magic-8-ball-simulator)
  - [Objective](#objective)
  - [Requirements](#requirements)
  - [Guidance](#guidance)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

In this chapter, we'll begin by ensuring our Python development environment is set up correctly by writing a classic "Hello, World!" script. After that, we'll embark on a fun project to create our own Magic 8-Ball simulator!

## Environment Setup

### Installing Python

1. **Download Python:** Visit the [official Python website](https://www.python.org/downloads/) and download the latest version of Python.
2. **Install Python:**
   - **Windows/Mac:** Open the installer and ensure that you select the “Add Python to PATH” option before installing.
   - **Linux:** Use your package manager. For Ubuntu, you can use: `sudo apt-get update && sudo apt-get install python3`.

### Setting Up a Virtual Environment

Virtual environments are a best practice for Python development, allowing you to create isolated spaces for your project’s dependencies, avoiding conflicts between projects and system-wide packages.

1. **Install virtualenv:**
   ```bash
   pip install virtualenv
   ```
2. **Create a Virtual Environment:**
   Navigate to your project directory and run:
   ```bash
   python -m venv myenv
   ```
   Replace `myenv` with your preferred environment name.
3. **Activate the Virtual Environment:**
   - **Windows:** `myenv\Scripts\activate`
   - **Mac/Linux:** `source myenv/bin/activate`

### Installing an IDE

We recommend using Visual Studio Code (VSCode) for Python development:

1. **Download and Install:** Visit the [VSCode website](https://code.visualstudio.com/download) to download and install it.
2. **Install Python Extension:** Open VSCode, visit the Extensions view (`Ctrl+Shift+X`), search for "Python", and install it.

## Your First Python Script: Hello, World!

1. **Create a File:** In your project directory, create a new file named `hello_world.py`.
2. **Write Code:** Open `hello_world.py` in your IDE and write the following code:
   ```python
   print("Hello, World!")
   ```
3. **Save the File:** Ensure that your script is saved.
4. **Run the Script:** Open your terminal, navigate to the script’s directory, and run:
   ```bash
   python hello_world.py
   ```
   You should see `Hello, World!` printed in the terminal.

## Project: Magic 8-Ball Simulator (WORK IN PROGRESS)

### Objective

Create a simple Python script that simulates a Magic 8-Ball. The user will ask a yes-or-no question, and the program will respond with a random answer.

### Requirements

- Prompt the user for input.
- Ensure the input ends with a question mark.
- Randomly select an answer from a predefined list.
- Display the answer.

### Guidance

1. **User Input:** Utilize `input()` to get the user's question.
2. **Random Selection:** Use the `random` module to randomly select an answer.
3. **Output:** Utilize `print()` to display the selected answer.
4. **Validation:** Ensure the input is a question.

Feel free to refer to the code skeleton provided in the chapter's `/code/` folder to get started! (WORK IN PROGRESS)

## Quiz

Stay tuned! We'll be adding a quiz here to test your knowledge and understanding of the concepts learned in this chapter.

## Next Steps

Congratulations on completing your first chapter and project! 🎉 Navigate to the [next chapter](../02-Variables_and_Data_Types/README.md) to continue your Python journey.

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [VSCode Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python Virtual Environments Tutorial](https://realpython.com/python-virtual-environments-a-primer/)

Happy Coding! 🚀
