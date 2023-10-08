
# Chapter 8: Object-Oriented Programming

Welcome to Chapter 8, where we delve into Object-Oriented Programming (OOP) in Python! 🚀 OOP is a programming paradigm that uses objects and classes, enabling a structured approach to simplify complex program structures. In this chapter, we’ll unravel the concepts of classes, objects, inheritance, and more, while also applying these concepts in a hands-on project: Library Management System.

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
    - [Understanding Classes and Objects](#understanding-classes-and-objects)
    - [Methods and Attributes](#methods-and-attributes)
    - [Inheritance and Polymorphism](#inheritance-and-polymorphism)
    - [Encapsulation and Abstraction](#encapsulation-and-abstraction)
    - [Interfaces in Object-Oriented Programming](#5-interfaces-in-object-oriented-programming)
    - [Object-Oriented Design Principles](#6-object-oriented-design-principles)
- [Mini-Example: Creating a Simple Class](#mini-example-creating-a-simple-class)
- [Project: Library Management System](#project-library-management-system)
    - [Objective](#objective)
    - [Requirements](#requirements)
    - [Guidance](#guidance)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which encapsulates data and functions that operate on the data. Python, being a multi-paradigm programming language, provides full-fledged support for OOP, enabling us to define classes, create objects, and work with inheritance and polymorphism.

In this chapter, we'll explore:
- **Classes and Objects**: The fundamental building blocks of OOP.
- **Methods**: Functions defined within a class, which can access and modify class data.
- **Inheritance**: A mechanism where a new class adopts properties from an existing class.
- **Polymorphism**: The ability of different classes to be used interchangeably through inheritance.
- **Encapsulation**: Restricting access to certain details of an object.
- **Abstraction**: Simplifying complex reality while modeling classes.

Let's embark on this journey by understanding the foundational concepts of OOP and gradually build upon them to create a Library Management System in our project section.

## Lesson Plan

### 1. Understanding Classes and Objects

### What is a Class?

A class can be thought of as a blueprint for creating objects. It defines a datatype by bundling data and methods that work on that data into one single unit. The data items and methods associated with the class are called attributes and methods, respectively.

Consider an example where `Car` is a class that has attributes like `make`, `model`, and `year`, and methods like `start_engine()`, and `stop_engine()`. 

### What is an Object?

An object is an instance of a class. When a class is defined, it merely describes what an object will be, but it is not an object itself. To use the functionalities provided by a class, you need to instantiate it. 

Using the `Car` class example, a specific car object would be:
```python
my_car = Car(make="Toyota", model="Corolla", year=2022)
```

### Defining and Instantiating a Class

Here's a basic example of how to define a class and instantiate it:

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Instantiating the class
my_car = Car("Toyota", "Corolla", 2022)

# Accessing method
my_car.display_info()
```

In this example:
- `__init__(self, make, model, year)`: A special method called a constructor that is used to initialize the object. The `self` parameter refers to the instance of the object itself.
- `display_info(self)`: A method to display car information.
- `my_car = Car("Toyota", "Corolla", 2022)`: Instantiates the `Car` class, creating a new object `my_car`.
- `my_car.display_info()`: Calls the `display_info` method to print out the car’s information.

### Class and Instance Variables

- **Class Variables**: Shared by all instances of a class. They are defined within a class but outside any of the class’s methods.
- **Instance Variables**: Data that belongs to an instance, and for that instance only.

```python
class Car:
    # Class Variable
    car_type = "Sedan"  

    def __init__(self, make, model, year):
        # Instance Variables
        self.make = make  
        self.model = model
        self.year = year
```

In the example above, `car_type` is a class variable, while `make`, `model`, and `year` are instance variables.

### Key Takeaways

- **Class**: A blueprint for creating objects, bundling together data (attributes) and methods.
- **Object**: An instance of a class.
- **Instantiation**: Creating an object from a class.

### 2. Methods and Attributes

In the realm of Object-Oriented Programming, methods and attributes play a crucial role in managing object states and behaviors. Let's delve deeper into these concepts to understand their significance and implementation in Python classes.

#### What are Attributes?

Attributes in classes are variables where data is stored. They represent the state or quality of an object. In Python, you have:

- **Instance Attributes**: These are associated with object instances. Each object has its own copy of the instance attribute.
- **Class Attributes**: These are shared among all instances of a class. They are set by prefixing the variable with the class name.

**Example**:

```python
class Car:
    # Class Attribute
    wheels = 4  

    def __init__(self, make, model):
        # Instance Attributes
        self.make = make  
        self.model = model
```

In the `Car` class above, `wheels` is a class attribute, while `make` and `model` are instance attributes.

#### What are Methods?

Methods are functions defined inside a class and are used to perform operations that sometimes utilize the attributes of the object they are called on. We categorize them as:

- **Instance Methods**: These are the most common type of methods which are called on an object and have access to instance attributes and other methods.
- **Class Methods**: These methods are bound to the class and not the object instance. They can alter the class state that applies across all instances of the class.
- **Static Methods**: These methods do not have access to the instance or class variables and are self-contained.

**Example**:

```python
class Car:
    # Class Attribute
    wheels = 4  

    def __init__(self, make, model):
        # Instance Attributes
        self.make = make  
        self.model = model

    # Instance Method
    def display_info(self):
        return f"{self.make} {self.model}"

    # Class Method
    @classmethod
    def update_wheels(cls, new_value):
        cls.wheels = new_value

    # Static Method
    @staticmethod
    def is_motor_vehicle():
        return True
```

In the `Car` class above, `display_info` is an instance method, `update_wheels` is a class method, and `is_motor_vehicle` is a static method.

#### Key Takeaways:

- **Attributes** hold data for the object, and they can be specific to each object (instance attributes) or shared among all instances (class attributes).
- **Methods** define actions that can be performed by the object, and they can be instance, class, or static methods, each with different levels of access to class and instance variables.

Understanding methods and attributes is fundamental to implementing encapsulation and abstraction, which we will explore in the subsequent sections. Try defining your own classes with various methods and attributes and observe their behavior to solidify your understanding!

## 3. Inheritance and Polymorphism

### A. Inheritance

Inheritance, a core concept of Object-Oriented Programming, allows a class (called a subclass) to utilize methods and attributes from another class (the superclass or base class). It provides a mechanism to promote code reuse and establish a hierarchical relationship between classes.

Let's consider a general class, `Vehicle`, which has attributes and methods that are common to all vehicles. Another class, `Car`, can inherit from `Vehicle`, thereby gaining access to its methods and attributes while also being able to introduce its own specific methods and attributes.

#### Basic Syntax for Inheritance

```python
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass
```
In this syntax, `DerivedClass` inherits from `BaseClass`, meaning all the methods and attributes of `BaseClass` are accessible by `DerivedClass`.

### B. Polymorphism

Polymorphism allows objects of different types to be treated as objects of a common super type. It enables using a single interface to represent different types of objects. More specifically, polymorphism allows a method to do different things based on the object it is acting upon, even though the method name remains the same.

#### Example of Polymorphism

```python
class Vehicle:
    def description(self):
        print("This is a generic vehicle")

class Car(Vehicle):
    def description(self):
        print("This is a car")
```

In the example above, `Car` is a derived class that inherits from `Vehicle` and also changes the behavior of the `description` method.

### Key Concepts and Takeaways

- **Inheritance** enables a class to utilize methods and attributes from another class, promoting reusability and establishing a logical and hierarchical relationship between classes.
- **Polymorphism** allows methods to do different things based on the object it is acting upon, promoting flexibility and cleaner code.

In the next sections, we will delve deeper into encapsulation and abstraction, which are crucial for managing the data within our classes and for simplifying complex systems by modeling classes in a more user-friendly manner.

### 4. Encapsulation and Abstraction

#### Understanding Encapsulation

Encapsulation is one of the fundamental concepts in OOP. It refers to the bundling of data (attributes) and the methods (functions) that manipulate the data into a single unit or class. Moreover, it restricts direct access to some of the object's components and can prevent the accidental modification of data.

In Python, encapsulation is achieved through private and protected access modifiers.

- **Private attributes or methods**: They are denoted by a double underscore `__` before the attribute or method name and cannot be accessed or modified directly. However, they can be accessed through methods within the class.
- **Protected attributes or methods**: Denoted by a single underscore `_`, they can be accessed by subclasses.

##### Practical Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self.__age = age  # private attribute
    
    def get_age(self):  # public method to access private attribute
        return self.__age
```

In the above `Person` class, `name` is a public attribute, while `__age` is private. To access or modify `__age`, methods like `get_age()` should be utilized.

#### Understanding Abstraction

Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. In OOP, abstraction allows you to focus on a simplified view of the problem and ignore complex details.

In Python, abstraction can be achieved through abstract classes and methods.

- **Abstract Class**: A class which cannot be instantiated. It allows you to create a set of methods that must be created within any child classes built from the abstract class.
- **Abstract Method**: A method that has no implementation in the abstract class and must be implemented in any subclass.

##### Practical Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
```

Here, `Shape` is an abstract class with an abstract method `area()`. Any subclass like `Circle` must provide an implementation for `area()`.

### Key Takeaways

- **Encapsulation** allows you to hide the internal workings of an object and only expose what is necessary.
- **Abstraction** enables focusing on the essential qualities of an object while ignoring the complex background details.

Feel free to create your own classes and experiment with encapsulation and abstraction in Python to get a better understanding of these concepts!

### 5. Interfaces in Object-Oriented Programming

#### Understanding Interfaces

In object-oriented programming (OOP), an interface defines a contract for a subclass and ensures that it implements a specific set of methods. The interface does not contain any logic but declares the methods that must be implemented within any child classes. In Python, interfaces are created using abstract classes and abstract methods.

##### Practical Example

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        return f"Paid {amount} using Credit Card."

class MobileWalletPayment(Payment):
    def make_payment(self, amount):
        return f"Paid {amount} using Mobile Wallet."
```

In the example above, `Payment` is an interface that defines a contract `make_payment` for its subclasses `CreditCardPayment` and `MobileWalletPayment`. The `@abstractmethod` decorator indicates that the method `make_payment` must be implemented within any child classes derived from the `Payment` interface. This ensures that all the subclasses follow the same API structure.

#### Key Takeaways

- **Interfaces** ensure that certain methods are implemented within any child classes, providing a consistent API and enabling polymorphism.
- Interfaces enhance maintainability and scalability in software design by providing a standardized approach to method implementation.

Feel free to create your own interfaces and implement them in Python to gain a deeper understanding of this concept!


### 6. Object-Oriented Design Principles

#### SOLID Principles

The SOLID principles are a set of design principles in object-oriented programming that, when combined together, make it more likely that a developer will create a system that is easy to maintain and scale over time. They are:

1. **S** - Single Responsibility Principle
2. **O** - Open/Closed Principle
3. **L** - Liskov Substitution Principle
4. **I** - Interface Segregation Principle
5. **D** - Dependency Inversion Principle

#### Object-Oriented Design Considerations

- **Cohesion**: The degree to which elements inside a module/class belong together. In general, you should aim for high cohesion, meaning that a class should represent a single concept.
- **Coupling**: The degree to which one class knows about another class. If you change one class, how likely is it that you’ll have to change another class too? You should aim for low coupling.

### Key Takeaways

- The **SOLID principles** guide the creation of stable, scalable, and robust systems through object-oriented design.
- Maintaining a balance in **cohesion** and **coupling** ensures a robust architecture, facilitating easier management and scalability.

Feel free to explore and implement the SOLID principles and consider cohesion and coupling while designing your classes and objects in Python!

### Mini-Example: Implementing a Basic Shape Calculator

Consider a scenario where we want to calculate areas of different shapes. Utilizing classes, inheritance, and polymorphism, you can create a simple shape calculator as follows:

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"A {shape.__class__.__name__} has an area of: {shape.area()}")
```

In the above example, `Shape` acts as a base class, and `Circle` and `Square` are subclasses implementing the `area` method in their own way. The objects `Circle(5)` and `Square(4)` are treated polymorphically as they are used through their superclass interface `Shape`.

Feel free to modify the example, add more shapes, and try to implement the concepts learned in this chapter!

## Project: Library Management System

### Objective

Create a robust, scalable, and user-friendly library management system that effectively manages books, patrons, and library staff, ensuring efficient operation and data integrity using the principles and concepts learned in object-oriented programming.

### Requirements

#### A. Book Class
Create a class to manage book entities with attributes and methods including but not limited to:

- **Attributes**: Title, Author, ISBN Number, Publication Year, and Status (Available, Checked Out, Reserved, etc.)
- **Methods**: Check Availability, Update Status, Display Book Information.

#### B. Patron Class
Develop a class to manage patrons with attributes and methods to:

- **Attributes**: Name, Member ID, Borrowed Books.
- **Methods**: Borrow Book, Return Book, View Borrowed Books, Reserve Book.

#### C. Library Staff Class
Implement a class for library staff members that includes attributes and methods to:

- **Attributes**: Name, Employee ID.
- **Methods**: Add or Remove Books, Check Book Status, Manage Patron Accounts, View Borrowed Books.

#### D. Library Class
Create a class that encapsulates the entire library system, managing the interactions between books, patrons, and staff with methods for:

- Checking In and Checking Out Books.
- Reserving Books.
- Adding New Patrons.
- Managing Staff.
- Displaying Library Catalog.
- Displaying Borrowed Books.

### Guidance

#### 1. Data Management
- Ensure data consistency for all entities, implementing encapsulation and abstraction to safeguard data integrity.
- Utilize file I/O operations or a database system to persistently store and manage library data across sessions.

#### 2. User Interaction
- Implement a user-friendly interface through which users (patrons and staff) can interact with the system, ensuring that users can perform necessary operations with ease and clarity.
- Provide clear feedback and instructions to the users to prevent input errors and guide them through processes like book borrowing, returning, and reservation.

#### 3. OOP Principles
- Leverage inheritance and polymorphism to minimize code redundancy, enhance code reusability, and simplify the codebase.
- Ensure that your classes adhere to the SOLID principles to promote maintainability, scalability, and robustness of the system.

#### 4. Testing
- Thoroughly test each class and method to ensure they perform as expected, paying special attention to edge cases and invalid inputs.
- Consider utilizing unit tests to automate the testing of your classes and methods, ensuring that future changes do not unintentionally introduce bugs.

#### 5. Documentation
- Ensure that your code is well-documented, providing comments and docstrings to explain the purpose and functionality of classes and methods.
- Include a README file to guide users and developers in setting up, using, and contributing to the project.

### Example Implementation

Feel free to refer to the code skeleton provided in the chapter's `/code/` folder to get started! An example solution will be provided in the `/code/answer/` folder to reference once you have attempted the project. Ensure to experiment, explore, and potentially introduce additional features to enhance your project further!

## Quiz

*Note: This section will be updated with a quiz to test your understanding of object-oriented programming concepts.*

## Next Steps

1. **Implement the Project**: Leverage the concepts learned to implement the library management system. Pay attention to the requirements and try to implement as many features as possible. 
2. **Explore Advanced OOP Concepts**: Dive deeper into OOP concepts like meta-classes, decorators, and context managers to enhance your OOP skills in Python.
3. **Join a Developer Community**: Engage with a developer community to discuss and explore more about OOP, seek guidance, and participate in relevant discussions.

## Additional Resources

1. **Books**:
   - "Python 3 Object-Oriented Programming" by Dusty Phillips.
   - "Object-Oriented Thought Process" by Matt Weisfeld.

2. **Online Courses**:
   - [Coursera: Object Oriented Programming in Python](https://www.coursera.org/specializations/python-3-programming)
   - [edX: Introduction to Computer Science and Programming Using Python](https://www.edx.org/course/introduction-to-computer-science-and-programming-7)

3. **Websites**:
   - [Real Python](https://realpython.com/): Offers numerous tutorials and articles related to Python and OOP.
   - [Geeks for Geeks Python Programming Language](https://www.geeksforgeeks.org/python-programming-language/): Provides a wide range of examples and articles explaining Python concepts, including OOP.

4. **Forums**:
   - [Stack Overflow](https://stackoverflow.com/): A vast community of developers where you can ask questions and share your knowledge about Python and OOP.
   - [Reddit’s r/learnpython](https://www.reddit.com/r/learnpython/): A subreddit dedicated to learning Python where you can seek advice and help.

Remember to continually practice and implement the knowledge gained to become proficient in object-oriented programming in Python.

---
Happy Coding! 🚀

[Back to Main](../README.md)

