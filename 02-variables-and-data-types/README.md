
# Chapter 2: Variables and Data Types

Welcome back to your Python learning journey! 🚀 In this chapter, we will explore some fundamental building blocks of Python programming: variables and data types. Let's dive into the exciting world of data management in Python and work on a delightful project together!

## Table of Contents

- [Introduction](#introduction)
- [Understanding Variables](#understanding-variables)
- [Exploring Data Types](#exploring-data-types)
- [Type Conversion](#type-conversion)
- [Lesson Plan](#lesson-plan)
  - [Variables](#1-variables-storing-and-using-data)
  - [Data Types](#2-data-types-structuring-your-data)
  - [Mathmatical Operations](#3-mathematical-operations)
  - [Type Conversion](#4-type-conversion-shifting-between-types)
- [Mini-Example: Simple Calculator](#mini-example-simple-calculator)
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

Variables in programming languages like Python serve as storage locations identified by a memory address and an associated symbolic name (an identifier). They are used to store information, which can be referenced and manipulated in a program. Here’s a more detailed breakdown:

#### Understanding Variables

In Python, variables are created the moment you first assign a value to them. You don’t need to declare them with any particular type and can even change type after they have been set.

\```python
x = 5  # An integer assignment
y = "John"  # A string assignment
\```

#### Variable Names

Variable names in Python can be any length and can consist of uppercase and lowercase letters (`A-Z, a-z`), digits (`0-9`), and the underscore character (`_`). However, they cannot start with a digit. Python variable names are case-sensitive, so `Var` and `var` are different variables.

#### Dynamic Typing

Python is dynamically typed, meaning that the Python interpreter infers the type of the variable at runtime. This is different from statically typed languages, which require the type of a variable to be declared upfront. 

\```python
x = 5  # x is of type int
x = "Hello"  # Now x is of type str
\```

#### Variable Assignment

Variables are assigned using the equal sign (`=`). The variable is on the left side, and the value you're assigning to the variable is on the right.

\```python
greeting = "Hello, World!"
\```

#### Using Variables

Once a variable has a value, you can use it elsewhere in your program. For instance, variables can be used in operations, printed, or utilized in logical comparisons.

\```python
name = "Python Learner"
print("Hello, " + name + "!")
\```

#### Variable Reassignment and Multiple Assignment

Variables can be reassigned as often as needed. Also, Python allows you to assign values to multiple variables in one line.

\```python
x = 1
x = 2
y, z = (3, 4)
\```

#### Constants

In Python, constants are typically declared and assigned on a module. By convention, constant variable names are written in uppercase, and their values are not meant to change during the program’s execution.

\```python
PI = 3.14
\```

#### Key Takeaways

- Variables allow for the storage and manipulation of data in the program.
- Python is dynamically typed, meaning the type of variable is determined at runtime.
- Variables can be reassigned and used in various operations throughout the code.
- Constants are used to store values that should not be changed.

With a solid understanding of variables, we can now store, manipulate, and utilize data in our Python programs effectively.


### 2. Data Types: Structuring Your Data

Understanding and utilizing various data types effectively is crucial for data management and operations in Python. Data types define the nature of data and determine what type of operations can be performed on them. Let's delve into the basic data types in Python.

#### Fundamental Data Types in Python

- **Integers**: Represented by `int`, integers are whole numbers without a fractional part. 
  ```python
  age = 30  # An example of an integer
  ```
  
- **Floating-Point**: Represented by `float`, these numbers have a decimal point or use an exponential (e) to define the number.
  ```python
  height = 1.75  # An example of a floating-point number
  ```
  
- **Strings**: Represented by `str`, strings are sequences of character data and are defined by enclosing text in single (`'`) or double (`"`) quotes.
  ```python
  name = "Python Learner"  # An example of a string
  ```
  
- **Boolean**: Represented by `bool`, boolean data type can hold one of the two values: `True` or `False`.
  ```python
  is_learning = True  # An example of a boolean
  ```

#### Operations on Data Types

Each data type allows various operations. For instance, integers and floating-point numbers support arithmetic operations.

```python
# Arithmetic operations with int and float
sum_result = age + height  # addition
difference = age - height  # subtraction
product = age * height  # multiplication
quotient = age / height  # division
```

Strings allow concatenation and repetition:

```python
# String operations
greeting = "Hello, " + name  # concatenation
cheer = "Hip, Hip, Hooray! " * 3  # repetition
```

#### Immutability of Basic Data Types

An essential characteristic to note about strings (and also applicable to numbers) is that they are immutable, meaning once they are created, they cannot be changed. Any operation that seems to change the value creates a new object instead.

```python
# Strings are immutable
original_string = "Python"
modified_string = original_string + " 3.8"  # Creates a new string
```

#### Summary

- Python provides various data types like `int`, `float`, `str`, and `bool` to work with different kinds of data.
- Each data type supports different operations and has its own methods for manipulation.
- Understanding the appropriate use of each data type is crucial for effective programming and data management.

Now, having understood the fundamental data types and their operations, let's explore how we can perform mathematical operations in the next section.


### 3. Mathematical Operations

Working with numbers is fundamental in programming. Python provides a variety of operations that allow you to perform mathematical calculations using both integers and floating-point numbers.

#### Basic Operations

- **Addition (`+`):** Adds values on either side of the operator.
  ```python
  sum_result = 7 + 3  # Result: 10
  ```
- **Subtraction (`-`):** Subtracts the right-hand operand from the left-hand operand.
  ```python
  difference = 10 - 3  # Result: 7
  ```
- **Multiplication (`*`):** Multiplies values on either side of the operator.
  ```python
  product = 4 * 3  # Result: 12
  ```
- **Division (`/`):** Divides the left-hand operand by the right-hand operand.
  ```python
  quotient = 8 / 2  # Result: 4.0
  ```

Note that division always results in a float, even if the mathematical result is a whole number.

#### Additional Operations

- **Modulus (`%`):** Divides left-hand operand by right-hand operand and returns the remainder.
  ```python
  remainder = 10 % 3  # Result: 1
  ```
- **Exponentiation (`**`):** Performs exponential (power) calculation on operators.
  ```python
  squared = 7 ** 2  # Result: 49
  ```
- **Floor Division (`//`):** The division of operands where the result is the quotient, and the digits after the decimal point are removed.
  ```python
  floor_division = 7 // 2  # Result: 3
  ```

#### Order of Operations

Python adheres to the PEMDAS order of operations: Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right). Utilize parentheses to ensure the desired order of operations:

```python
result = (5 + 3) * 2  # Result: 16
```

#### Combining Different Data Types

Be mindful of combining different data types in mathematical operations. Python allows operations between `int` and `float` seamlessly, but combining numbers (`int` or `float`) and strings will raise a `TypeError`:

```python
combined = 5 + 3.2  # Result: 8.2 (int + float = float)

invalid_combination = "5" + 3  # Raises TypeError
```

#### Rounding Numbers

Utilize the `round()` function to round floating-point numbers to the nearest integer, or to a specified number of decimal places:

```python
rounded_int = round(8.7)  # Result: 9
rounded_float = round(8.73, 1)  # Result: 8.7
```

Understanding and effectively utilizing mathematical operations allows you to create more dynamic and calculative programs, from simple arithmetic calculators to more complex scientific computations.


### 4. Type Conversion: Shifting Between Types

Data in Python can be converted from one type to another using type conversion (or type casting), enhancing flexibility in data manipulation. Type conversion is the process where you convert data of one type to another. This concept is critical when performing operations between different data types, ensuring data consistency and preventing type-related errors.

Python provides built-in functions for type conversion for its primitive data types:

#### - `int()`
Converts a value to an integer. If converting from a float, it truncates the decimal part.

```python
int_from_str = int("100")  # Converts string to integer: 100
int_from_float = int(9.8)  # Converts float to integer, truncating the decimal: 9
```

#### - `float()`
Converts a value to a floating-point number.

```python
float_from_str = float("7.2")  # Converts string to float: 7.2
float_from_int = float(5)       # Converts integer to float: 5.0
```

#### - `str()`
Converts a value to a string.

```python
str_from_int = str(30)        # Converts integer to string: "30"
str_from_float = str(12.3)    # Converts float to string: "12.3"
```

#### - `bool()`
Converts a value to boolean (`True` or `False`). By default, Python considers zero (in any numeric type) and empty sequences/collections as `False`. Non-empty strings and non-zero numbers are considered `True`.

```python
bool_from_int = bool(1)       # Converts integer to boolean: True
bool_from_empty_str = bool("")  # Converts empty string to boolean: False
```

#### Practical Applications of Type Conversion

##### - User Input
Often, data received from user input (using `input()`) is in string format. If you wish to perform arithmetic operations on this input, you need to convert it to an appropriate numeric data type.

```python
user_input = input("Enter a number: ")  # User input is always a string
number = int(user_input)  # Convert input string to integer
```

##### - Data Processing
When processing data, ensuring that it is in the correct type is crucial to prevent type-related errors and ensure accurate calculations.

```python
total = float("100.5") + 50  # Convert string to float and add a number
```

##### - Displaying Data
When displaying numerical data alongside strings, type conversion is necessary to concatenate them seamlessly.

```python
age = 30
print("I am " + str(age) + " years old.")  # Convert integer to string for concatenation
```

Remember to use type conversion judiciously to prevent data loss (such as loss of decimal points when converting from float to int) and always validate data before conversion to prevent type conversion errors.

In the initial code snippet:

```python
string_number = "10"
int_number = int(string_number)
```

The string "10" is seamlessly converted to an integer 10 using the `int()` function, demonstrating a simple instance of type conversion.

Understanding and implementing type conversion is pivotal in ensuring that your data is in the appropriate format for your operations and output, thereby enhancing your code's robustness and flexibility.

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
