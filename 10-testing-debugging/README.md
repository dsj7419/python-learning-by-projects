
# Chapter 10: Testing and Debugging

Welcome to Chapter 10 of our Python Learning Journey!

In this exciting chapter, we will unravel the mysteries behind Testing and Debugging in Python. Every developer, whether a novice or a seasoned expert, encounters bugs and unexpected behaviors in their code. Therefore, acquiring skills to systematically identify, diagnose, and fix these issues is paramount to ensuring our applications run smoothly and reliably.

🔍 We'll explore various testing strategies and debugging techniques that will empower you to build resilient and robust Python applications. So, buckle up as we dive into a world where we scrutinize our code, squash bugs, and enhance its reliability!

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
    - [Unit Tests](#unit-tests)
    - [Debugging Techniques](#debugging-techniques)
- [Mini-Example: Debugging a Simple Function](#mini-example-debugging-a-simple-function)
- [Project: Testing a Shopping Cart System](#project-testing-a-shopping-cart-system)
    - [Objective](#objective)
    - [Requirements](#requirements)
    - [Guidance](#guidance)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

Welcome to a pivotal point in your Python learning journey! 🐞🛠️

Developing software isn’t just about writing code. Equally crucial is ensuring that the code **works correctly**, **handles unexpected situations gracefully**, and **performs efficiently** in all scenarios. This is where the skills of **Testing** and **Debugging** come into play, and in this chapter, we will dive deep into these vital aspects of software development.

### Why is Testing Crucial? 🧪

Testing is the methodology used to ensure that your code behaves as expected, providing a safety net that enables developers to make changes without fear of unintentionally introducing bugs. Through systematic testing, we can:
- 🏗️ **Build Robust Systems**: Ensuring they work smoothly even under unforeseen circumstances.
- 🛡️ **Defend Against Bugs**: Catching them early before they creep into the production environment.
- 🔄 **Facilitate Continuous Development**: Enabling safe code changes and adaptations.

### The Art of Debugging 🕵️‍♀️

Debugging, on the other hand, is the detective work that comes into play when things don’t go as planned. It involves:
- 🚦 **Identifying**: Spotting where things are going wrong.
- 🧐 **Investigating**: Understanding why they’re going wrong.
- 🛠️ **Fixing**: Correcting the issues to make things right.

### Journey Ahead 🚀

In this chapter, we'll delve into various **testing methodologies** and **debugging techniques**. We will learn how to write tests to validate our code and explore strategies to debug effectively when issues arise. Through hands-on examples and a real-world project, we’ll apply these concepts to gain practical experience.

As we traverse through this chapter, remember that testing and debugging are not merely steps in the development process. They are integral to creating reliable, efficient, and high-quality software that not only meets but exceeds user expectations.

Let's dive in and explore the world where we ensure our code not only runs but runs flawlessly in every scenario!

## Lesson Plan

### Unit Tests

Unit tests are a critical part of writing robust, reliable software. They are designed to test the smallest testable parts of your application in isolation, which are often functions or methods. Unit tests ensure that various sections of code are performing as expected under various circumstances. At its core, a unit test is a piece of code that invokes another piece of code (the unit), and checks the output or behavior to validate whether it performs as intended.

#### Importance of Unit Tests

1. **Ensure Code Quality**: Unit tests help validate that every part of the software performs as it should, safeguarding against bugs and regression issues.
2. **Simplify Debugging**: When a test fails, it indicates precisely where the code has issues that need to be addressed, making the debugging process more efficient.
3. **Facilitate Code Refactoring**: Unit tests provide a safety net, allowing developers to make changes to the codebase while ensuring existing functionality remains intact.
4. **Enhance Collaboration**: They provide a form of documentation, allowing others on a team to understand how different code units should behave.

#### Writing Unit Tests in Python with `unittest`

Python’s `unittest` module, sometimes referred to as 'PyUnit', is based on the XUnit framework design pattern which is a part of the Python Standard Library. It provides a test discovery mechanism that can manage and run tests across multiple test modules.

##### Basic Example

Here’s a basic example to illustrate how `unittest` works:

```python
import unittest

def add(a, b):
    return a + b

class TestAdditionFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertNotEqual(add(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
```

In this example:
- A simple function `add` is defined to add two numbers.
- A test case `TestAdditionFunction` is created by subclassing `unittest.TestCase`.
- The test case includes a single test method `test_addition`, which checks if the `add` function provides the expected output.
- `assertEqual` and `assertNotEqual` are assertion methods provided by `unittest` to check if the obtained value equals the expected value.

#### Executing Unit Tests

The tests can be run using the command-line interface. When a test fails, `unittest` will provide detailed information about the failure. Otherwise, it remains silent to avoid cluttering the output.

```shell
python -m unittest test_module.py
```

In professional development environments, tests are often automated using continuous integration/continuous deployment (CI/CD) systems to ensure that code changes do not introduce errors.

#### Best Practices

1. **Keep Tests Isolated**: Ensure each test is independent and doesn’t affect others.
2. **Use Descriptive Test Names**: Ensure test method names are descriptive and convey the intent of the test.
3. **Mock External Services**: Use mocking to simulate external services and focus tests on the unit’s logic.
4. **Test Different Scenarios**: Ensure to cover various input scenarios, including edge cases and invalid inputs.

Remember, writing tests might seem laborious, but the investment significantly pays off in the long run, reducing debugging time and enhancing code quality.

### Debugging Techniques

Debugging is a systematic process of identifying and fixing issues in software. It's an inevitable and crucial aspect of software development, as it ensures the functionality of code aligns with expected outcomes. Debugging techniques can be straightforward, like inserting print statements to observe the flow and outcomes of a code, or more advanced, utilizing specialized tools to inspect various states (like variables, memory usage, CPU processes, etc.) of a program during runtime.

#### Common Debugging Techniques

- **Print Statement Debugging**: This is probably the simplest form of debugging. Developers insert print statements at various points in a code to output the values of variables and the flow of execution. While it's not the most efficient method for large projects, it can be quite effective for small scripts and debugging logic issues.

- **Automated Testing**: Using unit tests and other testing frameworks to automatically check that individual components of your application are working as expected.

- **Code Linters and Formatters**: Utilizing tools that analyze code for potential errors and enforce a coding standard can help catch errors and ensure consistency.

- **Manual Testing**: Manually interacting with the application to identify unexpected behavior or outcomes.

#### Using Debuggers

Debuggers allow developers to pause execution (also known as a breakpoint), step through code one line at a time, and inspect the state (like local variables and the call stack). Python provides a built-in interactive debugger known as PDB (Python Debugger). Here's a brief usage example:

```python
import pdb

def calculate_factorial(n):
    pdb.set_trace()  # This sets a breakpoint
    if n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

# Use this function call to initiate debugging
calculate_factorial(5)
```

When the code execution reaches the `pdb.set_trace()` statement, it will pause, allowing you to inspect the current state of the program. You can use various commands like `n` (run the next line), `c` (continue till the next breakpoint), `q` (quit debugger), `p` (print variable), and many others to navigate and inspect your code during runtime.

#### Utilizing Python's Debugging Tools

When it comes to debugging in Python, especially considering the tools and environments we've explored so far, two notable aspects stand out: using the debugger in Visual Studio Code and leveraging Python's built-in logging module.

- **Visual Studio Code Debugger**:
    Visual Studio Code (VSCode) offers a rich environment for debugging Python code with a user-friendly interface. To utilize the debugging features in VSCode, ensure you have the Python extension installed. Here’s a basic guide on how to use it:
    - **Setting Breakpoints**: Click on the left margin of the code line number where you want to pause execution.
    - **Starting the Debugger**: Use the Run and Debug option or press F5 to start debugging. Ensure you select or create a suitable configuration if prompted.
    - **Inspecting Variables**: Once a breakpoint is hit, the debugger will pause, and you can inspect variables, view call stack, and navigate through the code.
    - **Control Execution**: Use the provided controls to continue, step over, step into, or restart the debugging session.
    - **Interactive Debug Console**: Use the debug console to execute arbitrary Python code in the context of the breakpoint, which can be invaluable to understand the current state.
    
    ```python
    # Example: A simple Python code snippet
    def calculate_area(radius):
        area = 3.14 * (radius ** 2)  # You might set a breakpoint here to inspect variables
        return area
    ```

- **Logging**:
    Utilizing Python's logging module can be a game-changer for tracking code execution and identifying issues, especially when dealing with larger codebases or applications running in production. Instead of using print statements, which might be tempting during development, adopting logging early in your coding journey can provide scalable and configurable verbosity in your output.

    ```python
    # Example: Basic usage of the logging module
    import logging
    
    # Configure logging level, format, and optionally, an output file
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def calculate_area(radius):
        logging.debug(f"Calculating area with radius: {radius}")
        if radius < 0:
            logging.warning(f"Received negative radius: {radius}")
            return None
        area = 3.14 * (radius ** 2)
        logging.info(f"Calculated area: {area}")
        return area
    
    calculate_area(5)
    calculate_area(-3)  # This will generate a warning log message
    ```
    In the above code snippet, `logging.debug()` and `logging.info()` are used to log messages that might help trace the flow and state during execution, while `logging.warning()` is utilized to highlight unexpected or potentially erroneous situations. Remember that the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) set in `basicConfig` determines the minimum level that will be logged.

Remember, the best debugging tool is often a well-structured, clean, and commented codebase. Ensuring that your code is readable and maintainable means that bugs will be easier to understand and resolve!


## Mini-Example: Debugging a Simple Function

In this mini-example, we will explore a simple function that contains a bug and walk through the debugging process using Visual Studio Code's debugging tools and Python's logging.

Consider the following Python function intended to calculate the factorial of a given number:

```python
def factorial(n):
    fact = 1
    for i in range(1, n):
        fact *= i
    return fact
```

If you run this function with `factorial(5)`, you might expect to get `120` as the result, since \(5! = 5 	imes 4 	imes 3 	imes 2 	imes 1 = 120\). However, the function returns `24`, which indicates that there is a bug in the code.

### Step-by-Step Debugging with Visual Studio Code

Let's walk through how you might debug this using Visual Studio Code's debugging tools:

1. **Set a Breakpoint**: Click on the left margin next to the line number `4` in your code within Visual Studio Code to set a breakpoint. This will pause the execution of your code at this line, allowing you to inspect the variables and flow of execution.

2. **Start the Debugger**: Click on the "Run" icon on the left sidebar, and then click "Start Debugging" (or press F5). Ensure that you have configured the debugger to run the current Python file.

3. **Inspect Variables**: Once the debugger hits your breakpoint, you can hover over variables in your code to inspect their current values. In this case, inspecting the `fact` variable after a few loops might give you an insight into what's going wrong.

4. **Step Through Execution**: Use the debugging controls to step through your code line by line, observing how each line alters your variables and program state.

5. **Fix the Bug**: Based on your observations, you may find that the loop does not include `n` in its iterations. Adjust the loop to iterate up to and including `n`.

```python
for i in range(1, n + 1):
```

### Logging

Alternatively, or in addition, using Python's logging module could provide insights without pausing the code execution:

1. **Import the Logging Module**: At the beginning of your script, import the logging module.

```python
import logging
```

2. **Configure Logging**: Set up logging to output messages to a file with a level of `DEBUG`.

```python
logging.basicConfig(filename='factorial_debug.log', level=logging.DEBUG)
```

3. **Add Logging Statements**: Add statements in your code to output variable values and flow information to your log.

```python
logging.debug(f"Iteration: {i}, Fact: {fact}")
```

4. **Run and Inspect the Log**: Execute your code and then inspect the `factorial_debug.log` file to review the logged information.

Using these debugging and logging techniques, you can systematically inspect, identify, and resolve issues in your code, enhancing its reliability and correctness.


## Project: Testing a Shopping Cart System

### Objective

The main objective of this project is to construct a Shopping Cart system that allows users to add items, remove items, and checkout, while implementing robust unit tests to ensure its functionality is reliable and error-free. This project will provide you with practical experience in building and testing a system, handling potential issues and edge cases that may arise within the context of a virtual shopping environment.

### Requirements

- **Add Items**: Implement a feature that allows users to add items to their cart.
- **Remove Items**: Enable users to remove items from the cart.
- **Checkout**: Allow users to finalize their items and proceed to a checkout, providing a total price.
- **Unit Tests**: Create comprehensive unit tests for all implemented functionalities.
- **Logging**: Implement logging to keep track of user interactions within the system.

### Guidance

1. **Implementing the Cart System**:
   - Develop a class or set of functions that allow users to interact with the shopping cart, adding and removing items, and calculating the total price.
   - Ensure to handle potential issues, such as trying to remove an item that isn’t in the cart, or handling quantities of items.

2. **Creating Unit Tests**:
   - Using Python’s `unittest` module, create tests that validate the functionality of your shopping cart system.
   - Ensure to test various scenarios and edge cases, such as adding/removing multiple items, checking the total price calculation, and dealing with invalid inputs.

3. **Implementing Logging**:
   - Utilize Python’s logging module to keep a record of interactions within the cart, such as adding/removing items and checkout processes.
   - Ensure that the logs are clear, concise, and informative, providing insights into the operations taking place within the cart system.

4. **Testing and Debugging**:
   - Test your system thoroughly, ensuring that all functionalities work as expected and that your unit tests pass successfully.
   - Use debugging tools and logs to identify and rectify any issues that arise during testing, ensuring the reliability of the system.

Feel free to refer to the code skeleton provided in the chapter's `/code/` folder to get started! An example solution is also provided in the `/code/answer/` folder to reference once you have attempted the project.


## Quiz

Quizzes will be added at a later date.

## Next Steps

Congratulations on completing this chapter! In the next chapter, we will explore... [Go to Chapter 11](11-version-control/README.md).

## Additional Resources

- [Python Unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Python Debugging (pdb)](https://docs.python.org/3/library/pdb.html)

---
Happy Coding! 🚀

[Back to Main](../README.md)