# Chapter 4: Data Structures

Welcome to Chapter 4, where we delve into the world of data structures! 📚 In this segment, we'll explore key Python data structures like lists, dictionaries, and sets. Additionally, we'll employ these concepts to build a functional and practical To-Do List Application as our project!

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
  - [Lists](#1-lists)
    - [Understanding Lists](#understanding-lists)
    - [Key Operations on Lists](#key-operations-on-lists)
    - [Manipulating Lists](#manipulating-lists)
    - [Advanced List Methods](#advanced-list-methods)
  - [Dictionaries](#2-dictionaries)
    - [Understanding Dictionaries](#understanding-dictionaries)
    - [Accessing and Manipulating Dictionaries](#accessing-and-manipulating-dictionaries)
    - [Advanced Dictionary Methods](#advanced-dictionary-methods)
    - [Practical Applications of Dictionaries](#practical-applications-of-dictionaries)
  - [Sets](#3-sets)
    - [Introduction to Sets](#introduction-to-sets)
    - [Operations on Sets](#operations-on-sets)
    - [Advanced Set Techniques](#advanced-set-techniques)
    - [Practical Uses of Sets](#practical-uses-of-sets)
- [Mini-Example: Bringing It All Together](#mini-example-bringing-it-all-together)
- [Project: To-Do List Application](#project-to-do-list-application)
  - [Objective](#objective)
  - [Requirements](#requirements)
  - [Detailed Guidance](#detailed-guidance)
  - [Sample Interaction](#sample-interaction)
  - [Let's Get Coding!](#lets-get-coding)
  - [Tips](#tips)
- [Closing Thoughts](#closing-thoughts)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

Data structures provide a means to organize and store data, allowing us to perform various operations efficiently. In this chapter, we will explore some fundamental data structures in Python and learn how to manipulate them, followed by a project that leverages these concepts to create a To-Do List Application.

## Lesson Plan

### 1. Lists

#### Understanding Lists

In Python, a list is a dynamic and ordered collection of items. Due to its mutable nature, you can alter its content without altering its identity. It serves as a versatile tool for organizing and storing data in a structured way, capable of holding items of any data type—be it integers, strings, booleans, or even other lists.

```python
my_list = [1, 2, 3, "Python", True]
```

#### Key Operations on Lists

- **Indexing:** Lists in Python use zero-based indexing, enabling you to retrieve items based on their position. The first item, for instance, can be accessed using `my_list[0]`.
- **Slicing:** Through slicing, you can obtain a subset of the list by specifying a range of indices. It's worth noting that while the start index is inclusive, the end index isn't: `my_list[start:end]`.
- **Concatenating:** Two lists can be merged into one using the `+` operator.

```python
# Indexing
first_item = my_list[0]  # Output: 1

# Slicing
subset = my_list[1:4]  # Output: [2, 3, "Python"]

# Concatenating
new_list = my_list + ["Programming", 101]
```

#### Manipulating Lists

Lists offer a wide range of methods for data manipulation:

- **Adding Items:** 
  - `append(item)`: Adds a single item to the list's end.
  - `extend([item1, item2])`: Appends multiple items.

- **Removing Items:** 
  - `remove(item)`: Deletes an item based on its value.
  - `pop(index)`: Removes an item by its index. Without specifying an index, it targets the last item.

- **Modifying Items:** 
  Assign a new value to an item via its index: `my_list[index] = new_item`.

```python
# Adding Items
my_list.append("Learning")  # Output: [1, 2, 3, "Python", True, "Learning"]
my_list.extend([4, 5, 6])  # Output: [1, 2, 3, "Python", True, "Learning", 4, 5, 6]

# Removing Items
my_list.remove("Python")  # Output: [1, 2, 3, True, "Learning", 4, 5, 6]
my_list.pop(0)  # Output: [2, 3, True, "Learning", 4, 5, 6]

# Modifying Items
my_list[0] = "Changed Item"  # Output: ["Changed Item", 3, True, "Learning", 4, 5, 6]
```

#### Advanced List Methods

Python lists come with an array of advanced methods that cater to more intricate operations:

- **Sorting Lists:** 
  The `sort()` method allows for in-place sorting of items. For strings, the order is alphabetical, while for numbers, it's numerical.
  
- **Reversing Lists:** 
  The `reverse()` method reverses the order of items.

- **Counting Occurrences:** 
  The `count()` method returns the count of a particular item in the list.

- **Searching for an Element:** 
  The `index()` method reveals the index of a specified value's first occurrence. However, if the value isn't present, an error will be raised.

- **Copying Lists:** 
  While the assignment (`=`) creates a new reference to the same list, to clone a list, use the `copy()` method.

Lists remain an integral part of Python, offering a flexible and potent means to manage and organize data. Grasping the creation, access, modification, and manipulation of lists is pivotal for efficient data management in Python programming.

### 2. Dictionaries

#### Understanding Dictionaries

Dictionaries, often referred to as "dicts" in Python, are dynamic collections of key-value pairs. Each key is unique and maps to a specific value, making dictionaries particularly effective for tasks like data retrieval. Unlike lists, which are ordered collections, dictionaries are unordered, meaning the sequence of items is not fixed.

```python
my_dict = {"name": "Python", "type": "programming language"}
```

Dictionaries are versatile and can house various data types, such as strings, integers, lists, and even other dictionaries. When dealing with extensive data sets or when efficient lookup operations are required, dictionaries often outperform lists.

#### Accessing and Manipulating Dictionaries

- **Accessing Items:** Use the key inside square brackets to fetch its corresponding value. If a key doesn't exist, Python will raise a KeyError.

  ```python
  language_name = my_dict["name"]  # Output: "Python"
  ```

- **Modifying Items:** Directly assign a new value to a key to update its content.

  ```python
  my_dict["name"] = "Python 3"  # Output: {"name": "Python 3", "type": "programming language"}
  ```

- **Adding Items:** Insert new key-value pairs by simply assigning a value to a fresh key.

  ```python
  my_dict["version"] = 3.9  # Adds a new key-value pair: "version": 3.9
  ```

- **Removing Items:** Employ methods like `pop()` to remove an item by its key. Alternatively, the `del` keyword can also be used.

  ```python
  my_dict.pop("version")  # Removes the key "version" and its associated value
  del my_dict["type"]  # Removes the key "type" and its associated value
  ```

- **Iterating through Dictionaries:** Use methods like `keys()`, `values()`, and `items()` to loop through dictionaries.

  ```python
  for key, value in my_dict.items():
      print(f"Key: {key}, Value: {value}")
  ```

#### Advanced Dictionary Methods

- **Checking Existence:** The `in` keyword can be used to check if a key exists within the dictionary.

  ```python
  if "name" in my_dict:
      print("Name key exists in the dictionary!")
  ```

- **Getting Value with Default:** The `get()` method fetches the value for a given key if it exists, or returns a default value otherwise.

  ```python
  version = my_dict.get("version", "Not Specified")  # Returns "Not Specified" since "version" key doesn't exist.
  ```

- **Merging Dictionaries:** The `update()` method or the `**` unpacking operator can be used to merge two dictionaries.

  ```python
  extra_info = {"creator": "Guido van Rossum", "year": 1991}
  my_dict.update(extra_info)  # Merges extra_info into my_dict
  ```

#### Practical Applications of Dictionaries

- **Data Storage:** Efficiently store and retrieve data such as configurations, application settings, or user profiles.
- **Frequency Counting:** Easily count occurrences, be it words in a text or votes in a poll.
- **Caching:** Store results of expensive function calls and return the cached result when the same inputs occur again.
- **Graph Representation:** Represent graphs as adjacency lists where each node's neighbors are stored as lists or sets.

Dictionaries in Python are powerful and provide a flexible way to structure and access data. Familiarity with dictionaries is essential for any Python developer given their widespread use in various applications.

### 3. Sets

#### Introduction to Sets

Sets, in Python, offer a collection type that is both unordered and unindexed. The most distinguishing feature of sets is their inherent property of containing unique elements. This means that duplicates are automatically filtered out.

```python
my_set = {1, 2, 3, 4, 3}
```

In the example above, even though `3` is added twice, the set will only store a single instance of it, illustrating the automatic removal of duplicates.

#### Operations on Sets

- **Adding Elements:** The `add()` method facilitates the insertion of individual items to a set.

  ```python
  my_set.add(5)  # my_set now becomes {1, 2, 3, 4, 5}
  ```

- **Removing Elements:** The `remove()` method deletes a specified item from the set. However, it will raise a KeyError if the item is not found.

  ```python
  my_set.remove(3)  # my_set is now {1, 2, 4, 5}
  ```

- **Safely Discarding Elements:** The `discard()` method also removes an item, but it won't raise an error if the item doesn't exist in the set.

  ```python
  my_set.discard(3)  # No error, even if 3 isn't in my_set
  ```

- **Union Operation:** Use the `union()` method or the `|` operator to obtain a set containing all unique items from two sets.

  ```python
  another_set = {5, 6, 7}
  union_set = my_set | another_set
  ```

- **Intersection Operation:** The `intersection()` method or the `&` operator retrieves a set with items common to both sets.

  ```python
  common_set = my_set & another_set
  ```

#### Advanced Set Techniques

- **Difference Between Sets:** The `difference()` method or `-` operator can be used to get items present in the first set and not in the second.

  ```python
  diff_set = my_set - another_set
  ```

- **Symmetric Difference:** The `symmetric_difference()` method or `^` operator gives you a set containing items that are unique to each set.

  ```python
  sym_diff_set = my_set ^ another_set
  ```

- **Subset and Superset Checking:** The `issubset()` and `issuperset()` methods help in checking if a set is a subset or superset of another set, respectively.

  ```python
  small_set = {1, 2}
  is_subset = small_set.issubset(my_set)  # Returns True if small_set is a subset of my_set
  ```

#### Practical Uses of Sets

- **De-duplication:** Convert lists or other collections to sets to instantly remove any duplicate values.

  ```python
  my_list = [1, 2, 2, 3, 3, 3, 4]
  unique_list = list(set(my_list))
  ```

- **Quick Membership Tests:** As sets are implemented as hash tables, checking if an item exists within a set is usually faster than with lists.

  ```python
  is_present = 3 in my_set
  ```

- **Mathematical Operations:** Utilize sets for mathematical set operations like union, intersection, difference, etc., especially when working with groups of items.

Sets in Python are a potent tool for a plethora of operations, especially those necessitating unique items or efficient membership tests. Their various methods and operators offer a flexible approach to handling collections of items in your programming tasks.

### Mini-Example: Bringing It All Together

In this illustrative example, we integrate lists, dictionaries, and foundational concepts from lessons 1, 2, and 3 to create a basic contact book application. This application will allow users to manage a list of contacts, each with a name and phone number.

```python
# Initializing a list with dictionaries as elements
contacts = [{"name": "Alice", "number": "123-456"}, {"name": "Bob", "number": "789-012"}]

# A simple menu system
while True:
    print("\n1: Add Contact")
    print("2: Display Contacts")
    print("3: Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        # Taking user input for name and number
        name = input("Enter the name: ")
        number = input("Enter the phone number: ")

        # Basic input validation
        if not name or not number.isdigit():
            print("Invalid input. Please try again.")
            continue

        # Creating a new contact as a dictionary
        new_contact = {"name": name, "number": number}

        # Adding the new contact to our list using append()
        contacts.append(new_contact)

    elif choice == "2":
        # Displaying all contacts
        print("\nContact Book:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Number: {contact['number']}")

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please select from the menu.")
```

#### Understanding the Code

1. **Initializing Contacts:**  
   The list named `contacts` contains dictionaries. Each dictionary represents a contact with a name and phone number.
   
2. **User Input and Basic Validation:**  
   We've integrated a simple menu system where the user can add contacts or display all contacts. When adding a contact, we ensure the user provides valid data.

3. **Creating a New Contact:**  
   Contacts are represented as dictionaries, and new contacts are added to the `contacts` list dynamically based on user input.

4. **Displaying Contacts:**  
   We iterate through the `contacts` list using a for loop to display each contact.

#### Tie-Ins to Previous Lessons:

- **User Input and Displaying Output:**  
  We've integrated the use of `input()` and `print()` from Lesson 1. The user can dynamically add new contacts or choose to display all contacts.

- **Loops and Conditionals:**  
  The menu system uses a while loop and if-elif-else conditionals, showcasing concepts from Lesson 3.

- **Data Management:**  
  The application uses lists and dictionaries from Lesson 2 to manage and display contacts.

This example provides a practical demonstration of various foundational concepts, laying the groundwork for more intricate applications as one progresses in their Python journey.

## Project: To-Do List Application

### Objective

In this project, we aim to consolidate our understanding of Python data structures by developing a comprehensive To-Do List Application. The application will not only allow users to keep track of their tasks but also interactively add new tasks, mark existing ones as complete, and visualize their entire to-do list with the status of each task.

### Requirements

- **Task Addition:** Users should be able to dynamically add new tasks to their to-do list.
- **Task Completion:** Users should have the capability to mark specific tasks as complete.
- **Task Visualization:** Users should be able to view all their tasks along with their completion status.

### Detailed Guidance

1. **Managing Tasks:**
   - **Data Structure:** Utilize appropriate data structures (like lists and dictionaries) to manage tasks and their statuses effectively.
   - **Task Representation:** Each task should be represented in a manner that allows storing its name and completion status.
   - **Example:**
     ```python
     tasks = [{"name": "Task 1", "completed": False}]
     ```
   Insights: Consider how tasks will be identified uniquely and how each task's status will be stored and updated.

2. **User Interaction:**
   - **Adding Tasks:** Use `input()` to get the details of new tasks from the user.
   - **Marking Completion:** Allow users to specify which task they'd like to mark as complete and update the data structure accordingly.
   - **Example:**
     ```python
     new_task_name = input("Enter the new task: ")
     ```
   Reflections: Think about how user inputs will be captured and integrated into your data management logic.

3. **Displaying Tasks:**
   - **Visual Feedback:** Use `print()` to display the entire task list and each task's status to the user.
   - **Status Indication:** Clearly indicate which tasks are completed and which are pending.
   - **Example:**
     ```python
     for task in tasks:
         print(f"{task['name']} - {'Completed' if task['completed'] else 'Pending'}")
     ```
   Considerations: Think about how you will iterate through the data structure to display each task and its status.

### Sample Interaction

Imagine a user's interaction with your To-Do List Application:

```
Menu:
1. Add a task
2. Complete a task
3. View tasks
4. Exit
Choose an option: 1

Enter task name: Buy groceries
Task 'Buy groceries' added!

Menu:
1. Add a task
2. Complete a task
3. View tasks
4. Exit
Choose an option: 3

Tasks:
- Buy groceries (Pending)

Menu:
1. Add a task
2. Complete a task
3. View tasks
4. Exit
Choose an option: 2

Select a task to mark as complete:
1. Buy groceries
Task number: 1
Task 'Buy groceries' marked as complete!

Menu:
1. Add a task
2. Complete a task
3. View tasks
4. Exit
Choose an option: 3

Tasks:
- Buy groceries (Completed)
```

### Let's Get Coding!

- **Starting Point:** Refer to the code skeleton provided in the chapter's `/code/` folder.
- **Solution:** If curious or stuck, peek into the `/code/answer/` folder.

### Tips

- Prioritize the user experience, ensuring interactions are intuitive and displayed information is clear.
- Test the application to ensure all functionalities work seamlessly.

Embark on this journey with curiosity and creativity, and build an application that provides a solid base for further exploration in Python.

### Closing Thoughts

Mastering data structures is a significant milestone in any programmer's journey. By understanding how to efficiently organize, store, and access data, you're laying the foundation for more complex algorithms and applications in the future. Reflect on the different structures you've encountered - lists, dictionaries, sets - and consider how each has its unique strengths and applications. As you continue your Python journey, you'll find these structures becoming second nature, enabling you to tackle even more advanced challenges with confidence and finesse. Remember, programming isn't just about writing code; it's about problem-solving and crafting efficient solutions. And with the knowledge of data structures, you're well-equipped to do just that. Onwards and upwards!

## Quiz

Ready to test your knowledge? Take the Chapter 4 quiz [here](https://dsj7419.github.io/python-learning-by-projects/04-data-structures/quiz/).

## Next Steps

Congratulations on wrapping up Chapter 4 and crafting your own To-Do List Application! 🎉 Dive into the [next chapter](../05-modular-programming/README.md) to delve deeper into the world of Python by exploring modular programming techniques.

## Additional Resources

- [Python Official Documentation - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [W3Schools - Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [Geeks for Geeks - Python Sets](https://www.geeksforgeeks.org/sets-in-python/)

---
Happy Coding! 🚀

[Back to Main](https://dsj7419.github.io/python-learning-by-projects/)
