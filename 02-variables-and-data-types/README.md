
# Chapter 2: Variables and Data Types

Welcome back to your Python learning journey! 🚀 In this chapter, we will explore some fundamental building blocks of Python programming: variables and data types. Let's dive into the exciting world of data management in Python and work on a delightful project together!

## Table of Contents

- [Introduction](#introduction)
- [Understanding Variables](#understanding-variables)
- [Exploring Data Types](#exploring-data-types)
- [Type Conversion](#type-conversion)
- [Lesson Plan](#lesson-plan)
- [Project: Personalized Greeting Card Generator](#project-personalized-greeting-card-generator)
  - [Objective](#objective)
  - [Requirements](#requirements)
  - [Guidance](#guidance)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

In this chapter, we will delve into variables, which allow us to store and manipulate data, and explore different data types available in Python. We'll utilize these concepts in a project that creates a personalized greeting card!

## Understanding Variables

Variables in Python are used to store data values. Creating a variable involves providing a name and assigning it a value using the equal sign `=`.

```python
name = "Python Learner"
```

## Exploring Data Types

Python supports several basic data types, including:
- **int:** Integer numbers (e.g., `5`)
- **float:** Decimal numbers (e.g., `5.0`)
- **str:** Text strings (e.g., `"Hello"`)
- **bool:** Boolean values (`True` or `False`)

```python
age = 20  # int
height = 5.9  # float
greeting = "Hello"  # str
is_happy = True  # bool
```

## Type Conversion

Converting data from one type to another is possible using type conversion functions:
- `int()`
- `float()`
- `str()`
- `bool()`

```python
number_str = "100"
number_int = int(number_str)  # Converts string to integer
```

## Lesson Plan

In this lesson, we will explore variables, understand different data types, and learn about type conversion in Python.

### 1. Variables: Storing and Using Data
Variables enable us to label and store data in memory.

```python
my_var = "Store me!"
```

### 2. Data Types: Structuring Your Data
Understanding data types helps ensure data is stored and manipulated correctly.

```python
integer_example = 5
string_example = "Python"
```

### 3. Mathematical Operations
Python supports basic mathematical operations like addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).

```python
result = 5 + 3  # Addition
```

### 4. Type Conversion: Shifting Between Types
Converting between types allows for more flexible data manipulation.

```python
string_number = "10"
int_number = int(string_number)
```

### Mini-Example: Simple Calculator
Let's build a mini-program that asks the user for two numbers and prints their sum.

```python
# Get numbers from the user
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert strings to integers
num1 = int(num1_str)
num2 = int(num2_str)

# Calculate and display the sum
total = num1 + num2
print("The sum is:", total)
```

## Project: Personalized Greeting Card Generator

### Objective

Create a Python script that generates a personalized greeting card. The user will input their name and age, and the program will generate a card with a customized message.

### Requirements

- Prompt the user for their name and age.
- Generate a greeting card with a message using the provided details.
- Ensure that the age input is a valid number.

### Guidance

1. **User Input:** Use `input()` to obtain name and age.
2. **Data Validation:** Ensure age is a valid number.
3. **String Concatenation:** Combine strings to create a personalized message.
4. **Output:** Display the greeting card using `print()`.

Feel free to peek into the chapter's `/code/` folder if you need some inspiration! (WORK IN PROGRESS)

## Quiz

Stay tuned! We'll be adding a quiz here to test your knowledge and understanding of the concepts learned in this chapter.

## Next Steps

Kudos on completing Chapter 2 and creating your personalized greeting card! 🎉 Move on to the [next chapter](../03-control-flow/README.md) to explore the control flow in Python.

## Additional Resources

- [Python Official Documentation: Data Types](https://docs.python.org/3/library/datatypes.html)
- [W3Schools Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Real Python: Python Variables](https://realpython.com/python-variables/)

---
Happy Coding! 🚀

[Back to Main](../README.md)
