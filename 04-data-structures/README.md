# Chapter 4: Data Structures

Welcome to Chapter 4, where we delve into the world of data structures! 📚 In this segment, we'll explore key Python data structures like lists, dictionaries, and sets. Additionally, we'll employ these concepts to build a functional and practical To-Do List Application as our project!

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
  - [Lists](#1-lists)
  - [Dictionaries](#2-dictionaries)
  - [Sets](#3-sets)
- [Mini-Example: ](#mini-example-bringing-it-all-together)
- [Project: To-Do List Application](#project-to-do-list-application)
  - [Objective](#objective)
  - [Requirements](#requirements)
  - [Guidance](#guidance)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

Data structures provide a means to organize and store data, allowing us to perform various operations efficiently. In this chapter, we will explore some fundamental data structures in Python and learn how to manipulate them, followed by a project that leverages these concepts to create a To-Do List Application.

## Lesson Plan

### 1. Lists
#### Understanding Lists
In Python, a list is a mutable, ordered collection of items, meaning that we can modify its content without changing its identity. It allows the organization and storage of data in a structured manner. Items in a list can be of any data type—integers, strings, booleans, or even other lists, which provides a versatile way to keep data together.

```python
my_list = [1, 2, 3, "Python", True]
```

#### Key Operations on Lists
- **Indexing:** Retrieve an item from the list by referring to its position. Python lists are zero-indexed, so the first item is accessed using `my_list[0]`.
- **Slicing:** Obtain a subset of the list by specifying a range of indices. The resultant list includes the start index and excludes the end index: `my_list[start:end]`.
- **Concatenating:** Combine two lists into a new list using the `+` operator.

```python
# Indexing
first_item = my_list[0]  # Output: 1

# Slicing
subset = my_list[1:4]  # Output: [2, 3, "Python"]

# Concatenating
new_list = my_list + ["Programming", 101]
```

#### Manipulating Lists
Manipulating lists involves various operations, such as adding, removing, and modifying items. Here are some fundamental list manipulations:

- **Adding Items:** Use `append(item)` to add a single item to the end of the list or `extend([item1, item2])` to add multiple items.
- **Removing Items:** Use `remove(item)` to remove an item by value or `pop(index)` to remove an item by index. If `pop()` is used without an index, it removes and returns the last item.
- **Modifying Items:** Assign a new value to an item by referring to its index: `my_list[index] = new_item`.

```python
# Adding Items
my_list.append("Learning")  # Adds "Learning" to the end of the list
my_list.extend([4, 5, 6])  # Adds 4, 5, and 6 to the end of the list

# Removing Items
my_list.remove("Python")  # Removes "Python" from the list
my_list.pop(0)  # Removes 1 from the list

# Modifying Items
my_list[0] = "Changed Item"  # Changes the first item (2) to "Changed Item"
```

Lists in Python provide a robust way to manage and organize data in your programs, enabling operations on ordered collections of items. Understanding how to create, access, modify, and manipulate lists is crucial in managing data effectively in Python programming.

### 2. Dictionaries
#### Understanding Dictionaries
Dictionaries in Python are an invaluable data structure that store data as key-value pairs, where each unique key is an index and each value is the data related to that key.

```python
my_dict = {"name": "Python", "type": "programming language"}
```

Dictionaries can store a variety of data types, including strings, integers, lists, and even other dictionaries. They provide a way to manage data efficiently compared to lists, especially when dealing with large data sets and lookup operations.

#### Accessing and Manipulating Dictionaries
- **Accessing Items:** To access a value, reference its key using square bracket notation.
  
  ```python
  language_name = my_dict["name"]
  ```
  This will assign the string "Python" to the variable `language_name`.

- **Modifying Items:** You can change the value associated with a specific key.

  ```python
  my_dict["name"] = "Python 3"
  ```
  Now, `my_dict` is `{"name": "Python 3", "type": "programming language"}`.

- **Adding Items:** Add new key-value pairs simply by assigning a value to a new key.

  ```python
  my_dict["year"] = 1991
  ```
  Now, `my_dict` includes the year item: `{"name": "Python 3", "type": "programming language", "year": 1991}`.

- **Removing Items:** Use the `pop()` method or `del` keyword to remove items by key.

  ```python
  my_dict.pop("year")
  ```
  Or:
  ```python
  del my_dict["year"]
  ```

- **Iterating through Dictionaries:** Use `keys()`, `values()`, and `items()` methods for iteration.

  ```python
  for key, value in my_dict.items():
      print(f"Key: {key}, Value: {value}")
  ```

#### Practical Applications of Dictionaries
- **Data Storage:** Store data retrieved from files or APIs and easily access them with keys.
- **Frequency Counting:** Count occurrences of words or items in a dataset.
- **Building Graphs:** Use dictionaries of lists to represent graphs.

### 3. Sets
#### Comprehending Sets
Sets in Python provide a collection type that stores multiple items in a single variable. What makes sets unique is that they automatically remove duplicate values, ensuring that every item is unique. Sets are defined by enclosing the elements in curly braces `{}`.

```python
my_set = {1, 2, 3, 4, 3}
```

Notice in the above example, even though the number `3` appears twice, when the set is created, it will only contain one instance of `3`.

#### Set Operations
- **Adding Items:** The `add()` method allows you to add a single item to the set.

  ```python
  my_set.add(5)
  ```

  Now, `my_set` will be `{1, 2, 3, 4, 5}`.

- **Removing Items:** Use the `remove()` method to remove a specified item from the set. Be cautious when using this method as it will raise a KeyError if the item does not exist in the set.

  ```python
  my_set.remove(3)
  ```

  Now, `my_set` will be `{1, 2, 4, 5}`.

- **Discarding Items:** An alternative to `remove()` is `discard()`, which also removes an item from the set but does not raise an error if the item does not exist.

  ```python
  my_set.discard(3)  # This will not raise an error
  ```

- **Union of Sets:** The `union()` method or `|` operator can be used to get all unique items from two sets.

  ```python
  another_set = {4, 5, 6}
  union_set = my_set | another_set
  ```

- **Intersection of Sets:** The `intersection()` method or `&` operator gives you a set containing common items from two sets.

  ```python
  common_set = my_set & another_set
  ```

#### Practical Applications of Sets
- **Removing Duplicates:** Since sets automatically discard duplicate items, they can be effectively used to remove duplicates from a list.

  ```python
  my_list = [1, 2, 2, 3, 4, 4, 4, 5]
  no_duplicates = list(set(my_list))
  ```

- **Membership Testing:** Sets can be used to quickly check if an item exists within it because they are implemented as hash tables.

  ```python
  is_member = 3 in my_set
  ```

In the context of programming, sets can be incredibly useful for operations that require the elimination of duplicate entries, and for algorithms that need to check if an item is a member of a collection efficiently, among other use-cases.

### Mini-Example: Bringing It All Together

In this illustrative example, we will craft a straightforward contact book application that integrates lists, dictionaries, and the foundational concepts from chapters 1, 2, and 3. This application will allow us to manage a list of contacts, each with a name and phone number.

```python
# Initializing a list with dictionaries as elements
contacts = [{"name": "Alice", "number": "123-456"}, {"name": "Bob", "number": "789-012"}]

# Creating a new contact as a dictionary
new_contact = {"name": "Charlie", "number": "345-678"}

# Adding the new contact to our list using append()
contacts.append(new_contact)

# Displaying all contacts
print("Contact Book:")
for contact in contacts:
    print(f"Name: {contact['name']}, Number: {contact['number']}")
```

#### Understanding the Code

1. **Initializing Contacts:**  
   We begin by initializing a list named `contacts`, which contains dictionaries. Each dictionary holds a name and a phone number, represented as key-value pairs.
   ```python
   contacts = [{"name": "Alice", "number": "123-456"}, {"name": "Bob", "number": "789-012"}]
   ```
   
2. **Creating a New Contact:**  
   We define a new contact using a dictionary, employing key-value pairs to store the name and number.
   ```python
   new_contact = {"name": "Charlie", "number": "345-678"}
   ```
   
3. **Adding to the Contact List:**  
   We utilize `append()` to add the new contact (a dictionary) to our contact list (a list). This demonstrates the use of lists and their methods, which allow dynamic data management.
   ```python
   contacts.append(new_contact)
   ```

4. **Displaying Contacts:**  
   We employ a for loop to iterate through each contact in the `contacts` list. Within the loop, we use `print()` to display the name and number of each contact. This showcases looping through a list of dictionaries, and extracting data by using keys.
   ```python
   print("Contact Book:")
   for contact in contacts:
       print(f"Name: {contact['name']}, Number: {contact['number']}")
   ```

#### Tie-Ins to Previous Lessons:

- **User Input and Displaying Output:**  
  The use of `print()` echoes back to Chapter 1, where we learned how to display output to the user. To further enhance this application, you might incorporate `input()` to dynamically add new contacts based on user input.

- **Loops and Conditionals:**  
  In Chapter 3, we learned about controlling program flow using loops and conditionals. Our use of a for loop to display each contact is a practical application of this concept. You might extend this by adding conditionals to check for duplicate contacts or validate phone numbers.

- **Data Management:**  
  Managing contacts in a list of dictionaries is a straightforward application of the data structures learned in this chapter. This application could be expanded by implementing further data manipulation features, such as deleting or updating contacts, by employing other methods and constructs associated with lists and dictionaries.

This simplified contact book example elegantly blends various foundational concepts, providing a solid base upon which you can build more complex and feature-rich applications as you continue your Python learning journey.

## Project: To-Do List Application

### Objective

In this project, we aim to consolidate our understanding of Python data structures by developing a comprehensive To-Do List Application. The application will not only allow users to keep track of their tasks but also interactively add new tasks, mark existing ones as complete, and visualize their entire to-do list with the status of each task.

### Requirements

- **Task Addition:** Users should be able to dynamically add new tasks to their to-do list.
- **Task Completion:** Users should have the capability to mark specific tasks as complete.
- **Task Visualization:** Users should be able to view all their tasks along with their completion status.

### Detailed Guidance

1. **Managing Tasks:**
   - **Data Structure:** Utilize appropriate data structures (like lists and dictionaries) to effectively manage tasks and their statuses.
   - **Task Representation:** Ensure that each task is represented in a manner that allows the storage of its name and completion status.
   - **Example:**
     ```python
     tasks = [{"name": "Task 1", "completed": False}]
     ```
   Insights: Consider how you will identify tasks uniquely and how the status of each task will be stored and updated.

2. **User Interaction:**
   - **Adding Tasks:** Implement functionality using `input()` to capture the details of new tasks from the user.
   - **Marking Completion:** Allow users to specify which task they'd like to mark as complete and update the data structure accordingly.
   - **Example:**
     ```python
     new_task_name = input("Enter the new task: ")
     ```
   Reflections: Think about how you will ensure that user inputs are captured accurately and integrated into your data management logic.

3. **Displaying Tasks:**
   - **Visual Feedback:** Employ `print()` to showcase the entire task list and each task's status to the user in a readable format.
   - **Status Indication:** Clearly indicate which tasks are completed and which are pending.
   - **Example:**
     ```python
     for task in tasks:
         print(f"{task['name']} - {'Completed' if task['completed'] else 'Pending'}")
     ```
   Considerations: Consider how you will iterate through your data structure to display each task and its status in an organized manner.

### Let's Get Coding!

- **Starting Point:** Refer to the code skeleton provided in the chapter's `/code/starter/` folder to embark on this project with a structured approach. The skeleton code provides a framework that you'll build upon to create your To-Do List Application.
- **Solution:** If you're curious about one of the possible solutions or need some inspiration, feel free to peek into the `/code/answer/` folder after giving it a good go yourself!

### Tips

- Keep the user experience in mind, ensuring the user interactions are intuitive and the displayed information is clear.
- Test your application thoroughly to ensure that all functionalities (add, mark complete, view) work seamlessly together.

Embark on this journey with curiosity and creativity, and build an application that not only adheres to the requirements but also showcases your unique problem-solving approach.


## Quiz

Stay tuned! We'll be adding a quiz here to test your knowledge and understanding of the concepts learned in this chapter.

## Next Steps

Congratulations on completing Chapter 4 and building your To-Do List Application! 🎉 Navigate to the [next chapter](../05-modular-programming/README.md) to explore how to keep organized by using modular programming.

## Additional Resources

- [Python Official Documentation - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [W3Schools - Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [Geeks for Geeks - Python Sets](https://www.geeksforgeeks.org/sets-in-python/)

---
Happy Coding! 🚀

[Back to Main](../README.md)
