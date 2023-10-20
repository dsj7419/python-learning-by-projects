
# Chapter 6: File Operations

Welcome to Chapter 6, where we delve into the world of file operations in Python! 📁 In this chapter, we'll explore various methods of file input/output (I/O) and path management. Additionally, we'll embark on a project to create our very own Note-Keeping App!

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
  - [1. File I/O](#1-file-io)
    - [Understanding File I/O](#understanding-file-io)
    - [Modes in File I/O](#modes-in-file-io)
    - [Reading from Files](#reading-from-files)
    - [Writing to Files](#writing-to-files)
    - [Safeguarding File Operations with Context Managers](#safeguarding-file-operations-with-context-managers)
    - [File I/O Key Takeaways](#file-io-key-takeaways)
  - [2. Working with Paths](#2-working-with-paths)
    - [Understanding Paths in Python](#understanding-paths-in-python)
    - [Common Path Operations](#common-path-operations)
    - [Real-world Application: Ensuring Robust File Operations](#real-world-application-ensuring-robust-file-operations)
    - [Paths Key Takeaways](#paths-key-takeaways)
  - [3. Advanced File Operations](#3-advanced-file-operations)
    - [File Encodings](#file-encodings)
    - [Handling Large Files](#handling-large-files)
    - [Temporary Files](#temporary-files)
    - [File Positioning](#file-positioning)
    - [Handling File Errors](#handling-file-errors)
    - [Binary Files](#binary-files)
    - [Advanced File Operations Key Takeaways](#advanced-file-operations-key-takeaways)
  - [4. File Metadata and Permissions](#4-file-metadata-and-permissions)
    - [File Metadata](#file-metadata)
    - [File Permissions](#file-permissions)
    - [Directory Operations](#directory-operations)
    - [File Compression](#file-compression)
    - [Metadata and Permissions Key Takeaways](#metadata-and-permissions-key-takeaways)
- [Mini-Example: Enhanced File Operations](#mini-example-enhanced-file-operations)
- [Project: Note-Keeping App](#project-note-keeping-app)
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

File operations are a crucial aspect of programming that allows us to interact with files, be it reading data from files or writing data to files. This capability significantly enhances the usability and functionality of our programs, enabling them to interact with persistent data. In the context of our upcoming project, understanding file I/O will empower us to create a Note-Keeping App that can read from and write to files, providing a persistent note-keeping functionality!

## Lesson Plan

### 1. File I/O

#### Understanding File I/O

File Input/Output (I/O) operations are fundamental to a multitude of programming tasks. These operations enable our applications to communicate with files stored on the system, ranging from basic text documents to intricate binary data. Python, being a versatile language, provides an extensive toolkit to handle this wide variety of file types.

Central to file operations in Python is the built-in `open()` function, our primary interface to file objects.

```python
file_object = open('filename', 'mode')
```

In this construct:
- `filename`: Represents the name of the file you're aiming to interact with.
- `mode`: Specifies the mode in which the file should be opened, determining the type of operations permissible on the file.

##### Modes in File I/O

Understanding the different modes is pivotal for effective file operations:

- `'r'`: Read mode. Primarily for reading data from a file. If the file doesn't exist, it raises a FileNotFoundError.
- `'w'`: Write mode. For writing data to a file. If the file exists, it truncates it (removes all its contents). If it doesn't, Python creates one.
- `'a'`: Append mode. Adds data to the end of the file without disturbing existing data. Useful for logs and any data that requires historical preservation.
- `'b'`: Binary mode. Essential for dealing with non-text files like images, audio, or executable files. It's often used in combination with other modes, like `'rb'` or `'wb'`.

##### Reading from Files

Reading files is an everyday operation, and Python offers multiple methods to retrieve file data, tailored to diverse needs:

- `read()`: Reads the entire content of the file into memory as a single string.
- `readline()`: Reads the next line from the file. Useful for reading files line by line without loading the entire file into memory.
- `readlines()`: Retrieves all lines from a file and returns them as a list of strings.

```python
# Example: Reading a file line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

The example above showcases the combination of the `open()` function with a `for` loop, efficiently reading a file line by line. The `strip()` method is used to remove any leading or trailing whitespace, including the newline character.

##### Writing to Files

Writing to files is as straightforward as reading:

- `write()`: Writes a string to the file.
- `writelines()`: Accepts a list of strings and writes them to the file. It's worth noting that this method does not add newline characters between list items, so you might need to add them manually.

```python
# Example: Writing multiple lines to a file
lines_to_write = ["First line", "Second line", "Third line"]
with open('data.txt', 'w') as file:
    for line in lines_to_write:
        file.write(line + '\n')
```

This example demonstrates writing multiple lines to a file. The `+ '\n'` is used to ensure each string from the list starts on a new line in the file.

##### Safeguarding File Operations with Context Managers

The `with` statement in Python is known as a context management protocol. It ensures resources, like files, are efficiently used and properly closed after operations, even if an error occurs within the block. This automatic resource management is not only efficient but also enhances code readability.

```python
with open('data.txt', 'r') as file:
    content = file.read()
# Here, the file is automatically closed, and `content` contains the entire content of 'data.txt'.
```

By consistently using context managers, you ensure that your file operations are not only efficient but also less prone to common pitfalls like file leaks.

##### File I/O Key Takeaways

- File I/O is a central aspect of programming, enabling data persistence and interaction.
- Always ensure you open files in the appropriate mode to avoid unintentional data loss or corruption.
- Using context managers, like the `with` statement, ensures efficient and safe file operations.
- Reading and writing operations should be done with consideration for memory usage, especially with large files.

### 2. Working with Paths

#### Understanding Paths in Python

In the world of programming, the ability to handle and manipulate file paths is indispensable. Paths serve as the addresses of files and directories in your computer's filesystem. When programming in Python, you'll often interact with these paths while performing file operations, making their understanding and management crucial.

Python's `os.path` module, a submodule of the `os` module, is your primary toolkit for path manipulations. This module presents a collection of functions to interact with the filesystem and is designed to be cross-platform, ensuring your code remains functional across various operating systems.

##### Absolute vs. Relative Paths

There are two primary ways to refer to a file or directory's location:

- **Absolute Path**: This refers to the complete detail needed to locate a file or folder, irrespective of the current working directory. It often starts from the root directory.
  - E.g., `/home/user/documents/report.txt` or `C:\user\documents\report.txt`

- **Relative Path**: This refers to a file or directory's location relative to the current working directory.
  - E.g., if the current directory is `/home/user/`, the relative path to the report would be `documents/report.txt`.

While absolute paths provide a clear and unambiguous location of a file or folder, relative paths are often shorter and can be more flexible, especially when moving a set of files that maintain their internal directory structure.

#### Common Path Operations

Using the `os.path` module, you can perform a plethora of operations related to paths. Here are some of the most commonly used ones:

- **Joining Paths**: Given that different operating systems have varied path-separation characters (`\` for Windows and `/` for Unix-like systems), `os.path.join()` provides a reliable method to concatenate paths.
  ```python
  import os
  full_path = os.path.join('folder', 'subfolder', 'file.txt')
  ```

- **Checking Path Existence**: Before performing any I/O operations, it's prudent to ascertain that the target path exists. The `os.path.exists()` function serves this purpose.
  ```python
  if os.path.exists(full_path):
      print("Path exists!")
  else:
      print("Path does not exist!")
  ```

- **Determining the Type of a Path**: Often, you might want to determine whether a path points to a regular file or a directory.
  - `os.path.isfile(path)`: Returns `True` if the path points to a regular file, otherwise `False`.
  - `os.path.isdir(path)`: Returns `True` if the path points to a directory, otherwise `False`.

- **Splitting Pathnames**: `os.path.split()` can separate a pathname into a pair `(head, tail)` where `tail` is the last pathname component, and `head` is everything leading up to that.
  ```python
  head, tail = os.path.split(full_path)
  ```

#### Real-world Application: Ensuring Robust File Operations

Consider an application where you need to write logs consistently. The last thing you'd want is for the program to crash because a directory in the log's path doesn't exist.

```python
def write_log(log, path='logs/log.txt'):
    dir = os.path.dirname(path)

    # If the directory doesn't exist, create it
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Now, write the log
    with open(path, 'a') as file:
        file.write(log + '\n')
```

In this example, before attempting to write the log, the program ensures that the directory exists. If not, it creates the necessary directories. This approach guarantees that the file operations are resilient and reduces the risk of runtime errors.

### Paths Key Takeaways

- Paths are fundamental to file operations in Python, allowing us to specify the locations of files and directories.
- The `os.path` module offers versatile tools to manipulate and query paths, ensuring cross-platform compatibility.
- Always verify the existence and type of a path before performing file operations to ensure robustness.

### 3. Advanced File Operations

#### File Encodings

In a world with diverse languages and scripts, not every file is encoded using ASCII. Many files, especially those containing non-English characters, are encoded using different standards, such as UTF-8, UTF-16, or ISO-8859-1. Python's `open` function allows you to specify an encoding using the `encoding` parameter. By default, Python uses the system's encoding.

```python
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
```

If you try to read a file without specifying the correct encoding, you might encounter errors or incorrect data retrieval.

#### Handling Large Files

For extremely large files, reading the entire file into memory using `read()` can be inefficient and could lead to memory issues. Instead, you can read the file line-by-line or in chunks.

- Reading a large file line-by-line:

```python
with open('large_file.txt', 'r') as file:
    for line in file:
        process(line)
```

Here, each line is read and processed one by one, without loading the entire file into memory.

- Reading a file in chunks:

```python
chunk_size = 1024  # 1KB
with open('large_file.txt', 'r') as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        process(chunk)
```

This reads the file 1KB at a time and processes each chunk. You can adjust the `chunk_size` as needed.

#### Temporary Files

For operations where you need to store data temporarily (e.g., intermediate processing results), Python provides the `tempfile` module. This allows you to create temporary files and directories that can be automatically deleted when they are no longer needed.

- Creating a temporary file:

```python
import tempfile

with tempfile.TemporaryFile(mode='w+t') as tfile:
    tfile.write('Temporary data')
    tfile.seek(0)
    print(tfile.read())
```

This creates a temporary file, writes data to it, reads it back, and then automatically deletes the file when the context block exits.

#### File Positioning

When working with files, especially larger ones, you might want to jump to specific positions or navigate through the file in non-sequential ways. The methods `seek()` and `tell()` allow for just this.

- **`tell()` Method**: This method returns the current file position. It doesn't take any parameters and returns an integer representing the byte position in the file.

```python
with open('example.txt', 'r') as file:
    file.read(5)
    position = file.tell()
    print(f"Current file position: {position}")
```

- **`seek(offset[, whence])` Method**: This is used to change the file position. The `offset` indicates the number of bytes to be moved, and `whence` can take values:
    - `0`: The beginning of the file (default).
    - `1`: The current file position.
    - `2`: The end of the file.

```python
with open('example.txt', 'r') as file:
    file.seek(5)
    content = file.read(10)
    print(content)
```

#### Handling File Errors

Errors can happen when you're working with files—maybe the file doesn't exist, you don't have permission, or there's a reading/writing issue. It's essential to handle these errors gracefully:

```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("Error occurred while reading the file.")
```

#### Binary Files

Unlike text files that store data as readable characters, binary files store data in the format used by the computer's memory. Examples include images, audio files, and executables.

Reading and writing binary files requires an additional `'b'` mode:

```python
# Writing binary data
with open('binaryfile.bin', 'wb') as bin_file:
    bin_file.write(b'Some binary data')
```

```python
# Reading binary data
with open('binaryfile.bin', 'rb') as bin_file:
    data = bin_file.read()
    print(data)
```

#### Advanced File Operations Key Takeaways

- Always consider the encoding of a file, especially when working with non-ASCII characters.
- For large files, consider reading the file line-by-line or in chunks to avoid memory issues.
- Use the `tempfile` module to handle temporary files efficiently.
- File positioning methods like `seek()` and `tell()` provide control over file navigation.
- Handling file errors gracefully ensures your program doesn't crash unexpectedly.
- Understand the difference between text and binary files and handle them accordingly.

### 4. File Metadata and Permissions

#### File Metadata

Every file has metadata associated with it, which provides information about the file's attributes, such as its creation date, modification date, size, and more. The `os` module in Python provides functionalities to retrieve and modify this metadata.

- **Getting File Metadata with `os.stat()`:**
  
  This function returns a named tuple representing the status of a file. The attributes of this tuple can give you information about a file's size, its inode number, its creation date, etc.

```python
import os

file_stats = os.stat('example.txt')
print(f"File Size: {file_stats.st_size}")
print(f"File Modified Time: {time.ctime(file_stats.st_mtime)}")
```

- **Checking File Age:**
  
  For applications where you may want to process or delete old files, you can use the modification time to determine a file's age.

```python
import time

file_age = time.time() - file_stats.st_mtime
if file_age > 7 * 24 * 60 * 60:  # older than a week
    print("The file is older than one week.")
```

#### File Permissions

Ensuring the right file permissions is crucial for security. Python provides tools to check and modify file permissions.

- **Checking File Permissions:**

  You can use `os.access()` to check for file permissions.

```python
if os.access('example.txt', os.R_OK):
    print("The file is readable.")
if os.access('example.txt', os.W_OK):
    print("The file is writable.")
```

- **Changing File Permissions:**

  The `os.chmod()` method allows you to set the permissions for a file.

```python
os.chmod('example.txt', 0o644)  # sets read and write permissions for the owner and read for others
```

#### Directory Operations

While we have primarily discussed file operations, directories (or folders) also play a crucial role in file management. Let's discuss some common directory operations:

- **Listing Directory Contents:**
  
  The `os.listdir()` method returns a list of names in a directory.

```python
for filename in os.listdir('.'):
    print(filename)
```

- **Creating Directories:**

  To create a new directory, use `os.mkdir()`. For nested directories, `os.makedirs()` can be handy.

```python
os.mkdir('new_directory')
os.makedirs('nested_directory/sub_directory')
```

- **Renaming Files or Directories:**

  The `os.rename()` method can rename files or directories.

```python
os.rename('old_name.txt', 'new_name.txt')
```

- **Deleting Files and Directories:**

  Use `os.remove()` to delete files and `os.rmdir()` to remove empty directories. For directories with content, `shutil.rmtree()` can be used.

```python
os.remove('file_to_delete.txt')
os.rmdir('empty_directory')
import shutil
shutil.rmtree('directory_with_contents')
```

#### File Compression

There are times when you may want to compress files to save space or bundle multiple files together. Python provides the `zipfile` module for working with zip files.

- **Writing to a Zip File:**

```python
import zipfile

with zipfile.ZipFile('files.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')
```

- **Extracting from a Zip File:**

```python
with zipfile.ZipFile('files.zip', 'r') as zipf:
    zipf.extractall('extracted_files')
```

#### Metadata and Permissions Key Takeaways

- File metadata provides a wealth of information about a file's attributes.
- Proper file permissions are essential for security.
- Directory operations are crucial for managing and organizing files.
- File compression helps in bundling files and saving space.

### Mini-Example: Enhanced File Operations

Imagine we are creating a more advanced logging system for our calculator application. Beyond basic file I/O operations, we'll also demonstrate directory operations and touch on file metadata. Our aim is to store calculations in a designated directory, `calc_logs`, in a file named `calculations.txt`.

#### Setup: Directory Creation

Before diving into file operations, it's always a good practice to ensure the right directory structure exists.

```python
import os

dir_name = 'calc_logs'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
```

This code ensures that a directory named `calc_logs` exists for our log files. It's a simple yet effective way to organize our data.

#### Writing Calculations to a File

With our directory ready, let's proceed to log some calculations.

```python
# Designating our file path within the directory
file_path = os.path.join(dir_name, 'calculations.txt')

# Writing to the file
with open(file_path, 'a') as file:
    while True:
        # Getting user input
        calculation = input("Enter a calculation or 'exit' to stop: ")
        
        # Conditional check to break the loop
        if calculation.lower() == 'exit':
            break
        
        # Writing the calculation to the file
        file.write(calculation + "\n")
```

Here:
- `os.path.join(dir_name, 'calculations.txt')` constructs a file path that's OS-independent. This is a safer practice than hardcoding file paths.
- The rest of the logic remains consistent with our original example, focusing on writing user input to a file.

#### Reading Calculations from a File

Let's retrieve and display our logged calculations.

```python
# Reading from the file
with open(file_path, 'r') as file:
    print("Stored Calculations:")
    for line in file.readlines():
        print(line.strip())
```

The logic here remains unchanged from our original example, focusing on reading each line from the file and displaying it.

#### File Metadata: An Insight

It's sometimes useful to have insights into the data we're working with. Let's print some metadata about our log file.

```python
file_size = os.path.getsize(file_path)
print(f"\nThe size of the calculations file is: {file_size} bytes.")
```

This little addition gives us an idea about the size of our log file. Such metadata can be crucial in real-world applications for monitoring and optimization.

This enhanced mini-example not only showcases basic file I/O operations but also introduces directory operations and file metadata. As always, there's room for further exploration and experimentation!


## Project: Note-Keeping App

### Objective

Your task is to develop a Note-Keeping App that enables users to manage their notes effectively and persistently across sessions. The application should provide functionalities for users to:

1. Add new notes.
2. View all existing notes.
3. Delete specific notes.

All notes should be stored in such a way that they remain available even after the application is closed and reopened.

### Requirements

- **Persistent Storage**: Utilize file I/O operations to ensure that the notes are stored persistently. Notes should be retrievable across different sessions of the application.
- **User Interaction**: Implement a user-friendly interface using `input()` to navigate through the application. Users should receive clear instructions on how to add, view, and delete notes.
- **Error Handling**: Incorporate error handling mechanisms to handle potential issues, such as attempting to delete a non-existent note. Ensure that the application does not terminate unexpectedly due to unhandled errors.

### Detailed Guidance

1. **Directory Structure**: Before jumping into file operations, ensure that the right directory structure exists. You may want to organize your notes in a specific directory for better management.

2. **Adding New Notes**: 
   - Provide an option for users to input a new note.
   - Save each note persistently so that it can be accessed later.

3. **Viewing All Notes**: 
   - Display all the saved notes in a structured manner.
   - You may want to number each note for easier reference, especially when deleting.

4. **Deleting Notes**:
   - Offer a mechanism for users to specify and delete particular notes.
   - Ensure that deleted notes are removed from storage as well.

5. **User Interface**:
   - Keep the interface simple and intuitive.
   - At each step, inform the user of the possible actions they can take.
   - Provide feedback after every operation, so the user knows if their action was successful or not.

6. **Testing Your Application**: 
   - Regularly test the application to ensure all functionalities work as expected.
   - Ensure that after adding notes, they are stored persistently and can be accessed even after restarting the application.

### Sample Interaction

Upon running the application, a possible interaction could be:

```
Welcome to the Note-Keeping App!

Options:
1. Add a new note
2. View all notes
3. Delete a note
4. Exit

Choose an option: 1
Enter your note: Buy groceries.
Note added successfully!

Options:
1. Add a new note
2. View all notes
3. Delete a note
4. Exit

Choose an option: 2

Notes:
1. Buy groceries.

Options:
1. Add a new note
2. View all notes
3. Delete a note
4. Exit

Choose an option: 3
Enter the number of the note to delete: 1
Note deleted!

Options:
1. Add a new note
2. View all notes
3. Delete a note
4. Exit

Choose an option: 4
Goodbye!
```

This interaction showcases the basic functionalities of the Note-Keeping App, from adding a note, viewing it, to deleting it, and finally exiting the application.

### Let's Get Coding!

With the guidelines and requirements in mind, it's time to put theory into practice!

- **Starting Point:** Utilize the code skeleton in the chapter's [`/code/`](https://github.com/06-file-operations/code/) folder as a foundation for your Note-Keeping App.
- **Solution:** If you find yourself stuck or simply curious about one possible implementation, peek into the [`/code/answer/`](https://github.com/06-file-operations/code/answer/) folder. Remember, there are multiple ways to solve programming challenges, and the provided solution is just one of them.

### Tips

- Ensure your file operations account for potential errors, like trying to delete a note that doesn't exist.
- Implement user-friendly prompts and feedback. An intuitive interface greatly improves user experience.
- While this project primarily focuses on file operations, don't forget the best practices you've learned in previous chapters. Modular code, appropriate variable naming, and commenting can make a significant difference in code readability and maintainability.
- Think about potential extensions. How might you categorize notes? Could you implement a search feature?

### Closing Thoughts

With this project, you've taken another leap in your Python learning journey. Combining file operations with user interaction showcases how Python's versatility can create practical applications. As you continue to explore, think about how these foundational skills can be the building blocks for more complex projects. Whether it's data analysis, web development, or any other domain, the ability to read, process, and store information is fundamental. Happy coding!

## Quiz

Ready to test your knowledge? Take the Chapter 6 quiz [here](https://dsj7419.github.io/python-learning-by-projects/06-file-operations/quiz/).

## Next Steps

Congratulations on concluding Chapter 6! 🎉 Dive into the [next chapter](../07-regular-expressions/README.md) to further broaden your Python expertise.

## Additional Resources

- [Python Official Documentation on File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Working with Paths in Python](https://realpython.com/working-with-files-in-python/)
- [Python Official Documentation on Modules](https://docs.python.org/3/tutorial/modules.html)
- [Real Python: Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/)
- [Geeks for Geeks: Python Modules](https://www.geeksforgeeks.org/python-modules/)
- [Programiz: Python Modular Programming](https://www.programiz.com/python-programming/modules)

---

Happy Coding! 🚀

[Back to Main](https://dsj7419.github.io/python-learning-by-projects/)
