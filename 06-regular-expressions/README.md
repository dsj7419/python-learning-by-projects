
# Chapter 6: Regular Expressions

Welcome to Chapter 6, where we explore Regular Expressions in Python! 🎯 In this chapter, we'll dive deep into pattern matching and data extraction using regular expressions, enhancing our ability to process textual data. Furthermore, we'll work on a project: Data Scraper, which will leverage our new skills to extract meaningful data from textual content.

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
    - [Pattern Matching](#pattern-matching)
- [Mini-Example: Basic Pattern Matching](#mini-example-basic-pattern-matching)
- [Project: Data Scraper](#project-data-scraper)
    - [Objective](#objective)
    - [Requirements](#requirements)
    - [Guidance](#guidance)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

Regular expressions (regex or regexp) are incredibly powerful, and a bit daunting at first. They are a specialized language for specifying string patterns, providing a powerful way of searching, replacing, and parsing text with complex patterns of characters. In the context of our upcoming project, understanding regular expressions will empower us to create a Data Scraper that can extract meaningful data from raw text, revealing insights and information.

## Lesson Plan

### 1. Pattern Matching

#### Understanding Regular Expressions

A regular expression is a special sequence of characters that forms a search pattern. It can be used for everything from looking for specific patterns in a block of text to validating the format of email addresses or passwords.

Here's a quick breakdown of some of the basic elements in a regular expression:

- **Literals**: Regular characters that match themselves (e.g., `a`, `1`).
- **Metacharacters**: Characters that have a special meaning (e.g., `\d`, `\w`, `\s`, `.`).
- **Quantifiers**: Specify the quantity of characters to match (e.g., `*`, `+`, `?`, `{m,n}`).

##### Basic Syntax

In Python, the `re` module provides support for regular expressions. Here’s a quick example to get us started:

```python
import re

pattern = re.compile(r'\d{3}-\d{2}-\d{4}')  # A pattern for social security numbers
match = pattern.match('123-45-6789')

if match:
    print('Pattern found:', match.group())
else:
    print('Pattern not found')
```

Here:
- `re.compile(r'\d{3}-\d{2}-\d{4}')`: Compiles a regular expression pattern into a regex object.
- `.match('123-45-6789')`: Tries to apply the pattern at the start of the string.
- `match.group()`: Returns the string matched by the re.

#### Utilizing Regex Functions

- **`match()`**: Determine if the RE matches at the beginning of the string.
- **`search()`**: Scan through a string, looking for any location where the RE matches.
- **`findall()`**: Find all substrings where the RE matches, and returns them as a list.
- **`finditer()`**: Find all substrings where the RE matches, and returns them as an iterator.

```python
import re

pattern = re.compile(r'\b\w{4}\b')  # Words of 4 letters
matches = pattern.findall('This is a regular expression test.')

for match in matches:
    print(match)
```

In the code snippet above:
- `re.compile(r'\b\w{4}\b')`: Looks for words of exactly 4 letters.
- `.findall('This is a regular expression test.')`: Returns all matches in the string as a list.
- `for match in matches:`: Iterates over the matches, printing each one.

### Key Takeaways

- Regular expressions provide a powerful mechanism for pattern matching and data extraction in textual data.
- The `re` module in Python provides a rich and efficient way to work with regular expressions.
- Utilize various regex functions like `match()`, `search()`, `findall()`, and `finditer()` to apply regular expressions in different contexts.

### 2. Data Extraction

#### Understanding Data Extraction

Data extraction is the process of retrieving specific information from data sources, such as text files, web pages, or other forms of data storage. With regular expressions, you can define patterns to find specific strings or pieces of data amidst large amounts of text, enabling you to extract valuable information efficiently.

##### Utilizing Groups

- **Capturing Groups**: Enclosing a part of your regex in parentheses `()` allows you to extract specific parts of a matched string.

  ```python
  import re
  
  pattern = re.compile(r"(\d{3})-(\d{3}-\d{4})")
  match = pattern.search("My number is 555-123-4567")
  area_code = match.group(1)
  main_number = match.group(2)
  ```

  In this example, `area_code` will hold `"555"` and `main_number` will hold `"123-4567"`.

- **Non-Capturing Groups**: Use `(?: ... )` to define a group that should not capture the matched substring.

  ```python
  pattern = re.compile(r"(?:\d{3}-)?\d{3}-\d{4}")
  ```

  This pattern will match phone numbers with or without an area code, but it will not capture the area code.

- **Named Groups**: You can name your groups for easier reference using `(?P<name> ... )`.

  ```python
  pattern = re.compile(r"(?P<areacode>\d{3})-(?P<mainnumber>\d{3}-\d{4})")
  match = pattern.search("My number is 555-123-4567")
  area_code = match.group("areacode")
  main_number = match.group("mainnumber")
  ```

#### Practical Application

Imagine creating a system that extracts email addresses from a document. With regex, you can define a pattern that matches most email formats, enabling you to extract all email addresses present in a text.

```python
import re

def extract_emails(text):
    pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    return pattern.findall(text)

document = "Contact us at support@example.com or help@mysite.org"
emails = extract_emails(document)
```

In the function `extract_emails(text)`, `findall` returns all non-overlapping matches of pattern in string, as a list of strings. In this case, it would return `['support@example.com', 'help@mysite.org']`.

### 3. Regex in Python

#### Utilizing the `re` Module

Python's `re` module offers a set of functions that allows us to search text for particular patterns, providing the functionality we need to work with regex:

- **`re.search(pattern, string)`**: Scans through the string, looking for any location where this regex pattern produces a match.

- **`re.match(pattern, string)`**: Determines if the regex matches at the beginning of the string.

- **`re.findall(pattern, string)`**: Finds all the occurrences of the pattern in the given string.

- **`re.sub(pattern, repl, string)`**: Replaces occurrences of the pattern with a replacement string.

##### Flags

Flags help you to control the behavior of the regex parser. Some of the commonly used flags are:

- **`re.IGNORECASE` or `re.I`**: Ignore case while matching.
- **`re.MULTILINE` or `re.M`**: Treats the input as a multiline string.

#### Practical Application

Consider a scenario where you want to replace all occurrences of certain words in a text with synonyms. Using `re.sub()`, you can efficiently achieve this with regex.

```python
import re

def replace_synonyms(text):
    synonyms = {
        r"\bquick\b": "fast",
        r"\bbrown\b": "chocolate",
        r"\bfox\b": "wolf"
    }
    for word, synonym in synonyms.items():
        text = re.sub(word, synonym, text, flags=re.IGNORECASE)
    return text

text = "The quick brown fox"
new_text = replace_synonyms(text)
```

In the function `replace_synonyms(text)`, `re.sub()` is utilized to find occurrences of each word defined in the `synonyms` dictionary and replace them with the corresponding synonym, returning a text with the replaced words.

#### Key Takeaways

- Regular expressions are a powerful tool for pattern matching and data extraction.
- Utilizing groups, you can extract specific segments of your matched data for further use.
- Python’s `re` module provides a host of functions to work with regular expressions, enabling search, match, find, and substitution operations within text.
- Be mindful of the complexity and readability of your regex patterns, ensuring maintainability and efficiency.

Feel free to experiment by creating your own patterns and trying to extract data from sample texts!

### Mini-Example: Validating Email Addresses

Consider a scenario where we're validating email addresses. A basic, yet not fully RFC-compliant, regex pattern for email validation might look like this:

```python
import re

# A basic pattern for email validation
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# Test strings
emails = ['test.email@test.com', 'username@domain.com', 'invalid-email']

# Validate emails
for email in emails:
    if pattern.match(email):
        print(f'Valid:   {email}')
    else:
        print(f'Invalid: {email}')
```

In the above example, `pattern.match(email)` is utilized to validate email addresses against a specified pattern, providing a simple mechanism for basic email validation.

Feel free to experiment by modifying the pattern to make it more robust or trying to validate different types of data!

## Project: Data Scraper

### Objective

Develop a Data Scraper that can extract meaningful information from raw textual data using regular expressions, demonstrating the practical application of pattern matching and data extraction.

### Requirements

- **Data Extraction**: Extract specific pieces of information from a block of text.
- **Pattern Matching**: Utilize regular expressions to identify and extract the required data.
- **Data Presentation**: Display the extracted data in a user-friendly and structured format.

### Guidance

1. **Identifying Patterns**:
   - Analyze the text from which you need to extract data, identifying consistent patterns that can be targeted with regular expressions.
   
2. **Crafting Regular Expressions**:
   - Develop regular expressions that accurately match the patterns identified in the text.
   - Ensure to test your regular expressions with various samples of text to ensure accuracy and reliability.

3. **Extracting Data**:
   - Utilize `findall()` or `finditer()` to extract the data matched by your regular expressions from the text.
   - Ensure to manage the extracted data in a manner that facilitates easy and meaningful presentation.

Feel free to refer to the code skeleton provided in the chapter's `/code/` folder to get started! An example solution is also provided in the `/code/answer/` folder to reference once you have attempted the project.

## Quiz

Stay tuned! A quiz will be added here to assess your understanding of the concepts introduced in this chapter.

## Next Steps

Congrats on completing the chapter on Regular Expressions! 🎉 You've armed yourself with a powerful tool to manage and extract data from text, opening up vast possibilities in data processing and analysis.

In the [next chapter](07-exception-handling/README.md), we’ll dive into Object-Oriented Programming, exploring concepts like classes, objects, inheritance, and more, that will elevate your programming capabilities, enabling you to design robust and scalable software.

## Additional Resources

- [Python Docs: Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [Regex101: Online Regex Tester and Debugger](https://regex101.com/)
- [Regexr: Learn, Build, & Test RegEx](https://regexr.com/)
- [W3Schools: Python RegEx](https://www.w3schools.com/python/python_regex.asp)
- [Real Python: Regular Expressions: Regex in Python](https://realpython.com/regex-python/)

Feel free to explore and dive deep - regular expressions are a vast topic and there's always more to learn!

Happy Coding! 🚀