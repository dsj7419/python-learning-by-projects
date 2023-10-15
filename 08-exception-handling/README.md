
# Chapter 8: Exception Handling

Welcome to Chapter 8, where we dive deep into Exception Handling in Python! 🚑 In this chapter, we'll explore how Python deals with unexpected events—exceptions. By learning about exception handling, you will be able to create robust programs that can gracefully handle unexpected events without crashing. We'll also work on a project that requires a robust data entry system, ensuring data integrity and reliability.

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
    - [Try/Except](#tryexcept)
    - [Raising Exceptions](#raising-exceptions)
- [Mini-Example: Basic Exception Handling](#mini-example-basic-exception-handling)
- [Project: Robust Data Entry System](#project-robust-data-entry-system)
    - [Objective](#objective)
    - [Requirements](#requirements)
    - [Guidance](#guidance)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

In programming, things don't always go as planned. Files you expect to exist may be missing, data may not be in the format you expect, or the network connection may be down when you try to fetch a webpage. These are examples of exceptions—events that disrupt the normal flow of your program. Properly handling exceptions is essential for creating reliable and user-friendly programs. Exception handling in Python is done through the use of try/except statements, which allow the programmer to control the program's flow even when an exception occurs. This knowledge will be crucial for our project to create a Robust Data Entry System that can handle unexpected inputs without crashing.

## Lesson Plan

### 1. Try/Except

#### Understanding Try/Except

Exception handling in Python is implemented through the use of `try`/`except` blocks. A `try` block contains the code that might raise an exception, and the `except` block contains the code that is executed if an exception does occur.

Here's the basic syntax:

```python
try:
    # Code that might raise an exception
    pass  # Replace this with your code
except ExceptionType:  # Replace ExceptionType with the type of exception you want to handle
    # Code to handle the exception
    pass  # Replace this with your code
```

##### Understanding Exception Types

- **`Exception`**: A built-in base class for all built-in exceptions. This can catch most exception types.
- **`ArithmeticError`**: Raised for various arithmetic errors, like division by zero.
- **`FileNotFoundError`**: Raised when trying to open a non-existent file.
- **`ValueError`**: Raised when a function receives an argument of the correct type but inappropriate value.

Here's a basic example:

```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")
```

In the above code, attempting to divide by zero raises a `ZeroDivisionError`, which is caught by the `except` block, preventing the program from crashing and providing a friendly error message instead.

##### Handling Multiple Exceptions

You can handle different types of exceptions with multiple `except` blocks. This allows you to respond appropriately to various kinds of error situations.

```python
try:
    # Code that might raise multiple types of exceptions
    pass  # Replace this with your code
except (TypeError, ValueError):
    # Code to handle TypeError or ValueError
    pass  # Replace this with your code
except ZeroDivisionError:
    # Code to handle ZeroDivisionError
    pass  # Replace this with your code
```

##### Using Else and Finally

- **`else`**: The code in the `else` block is executed if the `try` block does not raise an exception.
- **`finally`**: The `finally` block is always executed, whether an exception was raised or not. It’s commonly used for cleanup actions, such as closing files.

```python
try:
    # Code that might raise an exception
    pass  # Replace this with your code
except SomeExceptionType:
    # Code to handle the exception
    pass  # Replace this with your code
else:
    # Code to run if no exception was raised
    pass  # Replace this with your code
finally:
    # Code that is always run
    pass  # Replace this with your code
```

#### Practical Application

Let’s consider a situation where we're creating a calculator application. If the user tries to divide by zero, instead of crashing, we can provide a friendly error message, guiding them to input valid data.

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Sorry, you can't divide by zero!")
        return None
```

In the function `safe_divide(a, b)`, if `b` is zero, a `ZeroDivisionError` will be raised, and the code in the `except` block will be executed, providing a friendly message instead of allowing the program to crash.

### Key Takeaways

- Exception handling allows your program to respond gracefully to unexpected events.
- Use `try`/`except` blocks to catch and handle exceptions in a user-friendly manner.
- Be mindful of the types of exceptions your code might raise and handle them appropriately.
- Utilize `else` and `finally` to manage code execution whether exceptions occur or not.

### 2. Raising Exceptions

#### Understanding Raising Exceptions

In Python, you can **raise** exceptions deliberately using the `raise` statement, enabling you to trigger exceptions under specific conditions to enforce certain behaviors or requirements in your code.

```python
raise ExceptionType("Error message")
```

Here, `ExceptionType` refers to the type of exception you want to raise, and "Error message" is the message that you want to deliver when the exception is raised.

##### Basic Usage of Raising Exceptions

- **Enforcing Requirements:**
  By raising exceptions, you can ensure that certain conditions or requirements are met before proceeding with the execution of your code.

  ```python
  def set_age(age):
      if age <= 0:
          raise ValueError("Age must be a positive number")
      # Additional code to set age...
  ```

  In this example, a `ValueError` is raised if an invalid age is provided, safeguarding against invalid data.

- **Signaling Issues:**
  Raising exceptions can be used to signal that a problem or abnormality has been encountered, halting the normal flow of execution to be caught by an exception handler.

  ```python
  def find_item(item, item_list):
      if item not in item_list:
          raise LookupError(f"{item} not found in list")
      # Additional code to handle item...
  ```

##### Utilizing Custom Exceptions

You can define custom exceptions to create meaningful error types for your application, enhancing clarity and debuggability. Custom exceptions are created by defining new classes derived from Python’s built-in `BaseException` class or one of its derived classes.

```python
class InvalidAgeError(ValueError):
    pass

def set_age(age):
    if age <= 0:
        raise InvalidAgeError("Age must be a positive number")
```

In this example, `InvalidAgeError` is a custom exception derived from `ValueError`, providing additional specificity to the type of error encountered.

##### Importance of Meaningful Error Messages

- **User Guidance:** Clear and descriptive error messages guide users by providing insight into the cause of the issue and potentially how to resolve it.
- **Debugging:** For developers, meaningful messages can be crucial in identifying, understanding, and resolving issues during debugging.

#### Practical Application

Imagine creating a user registration system where you require the age of the user to be above a certain value. By using raised exceptions, you can enforce these requirements, ensuring data integrity and aiding in maintaining a smooth user experience.

```python
def register_user(username, age):
    if age < 13:
        raise InvalidAgeError("Users must be 13 years or older to register")
    # Additional code to register the user...
```

By strategically raising exceptions, you not only preserve data integrity but also safeguard the user experience by providing clear and actionable error messages.

#### Key Takeaways

- Raising exceptions allows you to deliberately trigger exceptions when certain conditions are met.
- Custom exceptions provide additional specificity and clarity to your error handling mechanism.
- Meaningful error messages are crucial for guiding users and aiding developers during debugging.

Feel free to experiment by creating your own custom exceptions and utilizing raised exceptions to enforce requirements in a small sample program or function!


### Mini-Example: Handling Exceptions in a Calculator

Consider a simple calculator application that takes two numbers as input, performs an operation (addition, subtraction, multiplication, or division), and outputs the result. Exception handling plays a pivotal role in managing scenarios where unintended inputs (like dividing by zero or providing a string instead of a number) might occur.

Here’s a small snippet of how exception handling can be integrated:

```python
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation. Please choose between +, -, *, /.")
    
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

In this snippet:

- The `try` block encapsulates the code that might raise exceptions, safeguarding the application from abrupt termination.
- Multiple `except` blocks catch and handle various exceptions, providing feedback and preventing the application from crashing.
- `ZeroDivisionError` and `ValueError` are specific exceptions that handle divided by zero and invalid number input scenarios, respectively.
- The generic `Exception` catches any other exceptions, with `str(e)` being used to display the exception message.

This example demonstrates the application of exception handling to manage user input effectively and ensure a smooth user experience despite erroneous inputs.

## Project: Basic Data Entry System

### Objective

Develop a robust data entry system that allows users to input various types of data (like names, ages, and email addresses) into the system, ensuring that the data adheres to specific formats and criteria, and utilizing exception handling to manage invalid inputs gracefully.

### Requirements

- **Data Entry**: Allow users to enter data, such as name, age, and email.
- **Data Validation**: Ensure that the data entered adheres to specific formats or criteria (e.g., age must be a positive integer, email must be in a valid format).
- **Exception Handling**: Utilize exception handling to manage invalid inputs, ensuring that the application provides feedback and does not crash due to erroneous data.

### Guidance

1. **Data Entry and Validation**:
   - Implement mechanisms to capture user inputs via `input()`.
   - Validate the data to ensure adherence to predefined formats or criteria, e.g., utilizing regular expressions to validate email formats.
   
2. **Exception Handling**:
   - Implement `try/except` blocks to catch exceptions that may occur during data validation or entry, such as `ValueError` when converting strings to integers.
   - Provide user feedback through `print()` statements within `except` blocks to inform them of invalid inputs and guide them towards providing correct data.

3. **User Interaction**:
   - Create a user-friendly interface that guides the user through the data entry process, providing clear instructions and feedback.
   - Ensure that the user is informed of the data formats and criteria expected to prevent common input errors.

4. **Testing**:
   - Ensure that the data entry system handles various edge cases and invalid inputs gracefully, providing feedback and preventing crashes.
   - Test the system with various data types and formats to ensure robustness.

Feel free to refer to the code skeleton provided in the chapter's `/code/` folder to get started! An example solution is also provided in the `/code/answer/` folder to reference once you have attempted the project.

## Quiz

Stay tuned! A quiz will be added here to assess your understanding of the concepts introduced in this chapter.

## Next Steps

Congratulations on completing Chapter 6! In the [next chapter](09-object-oriented-programming/README.md), we’ll dive into Object-Oriented Programming, exploring concepts like classes, objects, inheritance, and more, that will elevate your programming capabilities, enabling you to design robust and scalable software.

## Additional Resources

- [Python Docs: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Exception Handling](https://realpython.com/python-exceptions/)

---
Happy Coding! 🚀

[Back to Main](https://dsj7419.github.io/python-learning-by-projects/)
