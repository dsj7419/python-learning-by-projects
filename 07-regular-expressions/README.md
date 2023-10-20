
# Chapter 7: Regular Expressions

Welcome to Chapter 7, where we explore Regular Expressions in Python! 🎯 In this chapter, we'll dive deep into pattern matching and data extraction using regular expressions, enhancing our ability to process textual data. Furthermore, we'll work on a project: Data Scraper, which will leverage our new skills to extract meaningful data from textual content.

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
  - [1. Basics of Regular Expressions](#1-basics-of-regular-expressions)
    - [Understanding the Need for Regex](#understanding-the-need-for-regex)
    - [Basic Regex Characters](#basic-regex-characters)
    - [Quantifiers in Regex](#quantifiers-in-regex)
    - [Key Takeaways](#key-takeaways)
  - [2. Advanced Regular Expressions](#2-advanced-regular-expressions)
    - [Lookaheads and Lookbehinds](#lookaheads-and-lookbehinds)
    - [Word Boundaries](#word-boundaries)
    - [Character Classes](#character-classes)
    - [Flags in Regex](#flags-in-regex)
    - [Key Takeaways](#key-takeaways)
  - [3. Practical Applications of Regex](#3-practical-applications-of-regex)
    - [Data Validation](#data-validation)
    - [Data Extraction and Grouping](#data-extraction-and-grouping)
    - [String Replacement](#string-replacement)
    - [Real-world Scenarios](#real-world-scenarios)
    - [Key Takeaways](#key-takeaways)
- [Mini-Example: Extracting Phone Numbers with Regex](#mini-example-extracting-phone-numbers-with-regex)
- [Project: Data Scraper](#project-data-scraper)
  - [Objective](#objective)
  - [Requirements](#requirements)
  - [Guidance](#guidance)
  - [Sample Interaction](#sample-interaction)
  - [Let's Get Coding!](#lets-get-coding)
  - [Tips](#tips)
  - [Closing Thoughts](#closing-thoughts)
- [Quiz](#quiz)
- [Next Steps](#next-steps)
- [Additional Resources](#additional-resources)

## Introduction

Regular expressions (regex or regexp) are incredibly powerful, and a bit daunting at first. They are a specialized language for specifying string patterns, providing a powerful way of searching, replacing, and parsing text with complex patterns of characters. In the context of our upcoming project, understanding regular expressions will empower us to create a Data Scraper that can extract meaningful data from raw text, revealing insights and information.

## Lesson Plan

### 1. Basics of Regular Expressions

#### Understanding the Need for Regex

In our digital age, we are surrounded by vast amounts of text data. This data can be anything - from log files and configurations to web pages and manuscripts. Extracting specific information from these vast datasets can be like finding a needle in a haystack. This is where Regular Expressions (regex) shine.

Regular expressions offer a concise and flexible means to "match" strings of text, such as particular characters, words, or patterns of characters. For example, imagine having a large text file with thousands of email addresses, and you only wanted to retrieve the Gmail addresses. Regex provides a way to describe and parse this information efficiently.

#### Basic Regex Characters

Before diving deep into complex patterns, let's understand some basic characters in regex:

- **Literals**: These are standard characters that match themselves exactly. For example, the regex `data` will match the string "data" in any given text.
- **Dot `.`**: Represents any character except for a newline. So, `d.t` will match "dot", "dat", "d3t", and so on.
- **Backslash `\`**: Used to escape a metacharacter. So, if you want to match a dot (.), you would use `\.` in your regex.
- **^ and $**: These symbols match the start and end of a line, respectively. For example, `^data` will match any line that starts with "data".

Here's a basic example to help clarify:

```python
import re

pattern = re.compile(r'^a.b$')  # Matches any three-character string that starts with 'a' and ends with 'b'
```

#### Quantifiers in Regex

Quantifiers determine how many instances of the preceding element in the regex pattern are a match.

- `*`: Matches zero or more repetitions of the preceding element. So, `ab*c` will match "ac", "abc", "abbc", and so on.
- `+`: Matches one or more repetitions. `ab+c` will match "abc", "abbc", but not "ac".
- `?`: Indicates zero or one repetition. `ab?c` will match "ac" and "abc", but not "abbc".
- `{m}`: Specifies exactly m repetitions. `a{3}` will match "aaa".
- `{m,n}`: Specifies between m and n repetitions. `a{2,3}` will match "aa" and "aaa".

```python
pattern = re.compile(r'ab{2,4}c')  # Matches 'abbc', 'abbbc', or 'abbbbc'
```

#### Key Takeaways

- Regular expressions provide a powerful way to find specific patterns in text.
- The basic characters in regex, like literals and metacharacters, form the foundation of pattern matching.
- Quantifiers allow for flexibility in defining how many times an element should be present for a match.

### 2. Advanced Regular Expressions

#### Lookaheads and Lookbehinds

These are specialized groups of characters in regex that allow you to match a pattern based on what comes before (lookbehind) or after (lookahead) a specific sequence.

- **Positive Lookahead (?=...)**: Specifies a group that can look ahead to see if an element exists.
  
  ```python
  pattern = re.compile(r'John(?= Smith)')  # Matches 'John' only if followed by ' Smith'
  ```

- **Negative Lookahead (?!...)**: Specifies a group that can look ahead to ensure an element doesn't exist.
  
  ```python
  pattern = re.compile(r'John(?! Doe)')  # Matches 'John' only if NOT followed by ' Doe'
  ```

- **Positive Lookbehind (?<=...)**: Specifies a group that can look behind to see if an element exists.
  
  ```python
  pattern = re.compile(r'(?<=Dr. )John')  # Matches 'John' only if preceded by 'Dr. '
  ```

- **Negative Lookbehind (?<!...)**: Specifies a group that can look behind to ensure an element doesn't exist.
  
  ```python
  pattern = re.compile(r'(?<!Mr. )John')  # Matches 'John' only if NOT preceded by 'Mr. '
  ```

#### Word Boundaries

Word boundaries `\b` are crucial when you want to ensure that a pattern represents a whole word. They match the position between a word character (as represented by `\w`) and a non-word character.

```python
pattern = re.compile(r'\bword\b')  # Matches 'word' but not 'swordfish' or 'password'
```

#### Character Classes

Character classes are used to match any one of a specific set of characters. They are defined by enclosing a character set in square brackets `[]`.

- `[abc]`: Matches any single character that is either 'a', 'b', or 'c'.
- `[^abc]`: Matches any single character that is NOT 'a', 'b', or 'c'.

Ranges can also be specified:

- `[a-z]`: Matches any lowercase alphabetical character.
- `[A-Z]`: Matches any uppercase alphabetical character.
- `[0-9]`: Matches any single digit.

```python
pattern = re.compile(r'gr[ae]y')  # Matches 'gray' or 'grey'
```

#### Flags in Regex

Regex flags modify how the matching operates.

- **re.IGNORECASE (or re.I)**: Makes the match case-insensitive.
  
  ```python
  pattern = re.compile(r'hello', re.I)  # Matches 'hello', 'Hello', 'HELLO', etc.
  ```

- **re.MULTILINE (or re.M)**: Modifies `^` and `$` to match the start and end of each line.
  
  ```python
  pattern = re.compile(r'^text', re.M)  # Matches 'text' at the beginning of any line in a multiline string
  ```

- **re.DOTALL (or re.S)**: Makes `.` match any character, including a newline.

#### Key Takeaways

- Lookaheads and lookbehinds enable more refined and specific pattern matching based on context.
- Word boundaries ensure that a pattern matches distinct words without being part of larger words.
- Character classes offer flexibility in matching specific sets or ranges of characters.
- Flags can modify the behavior of the regex engine for specific needs, such as case-insensitive matching or multiline mode.

### 3. Practical Applications of Regex

Regular expressions, with their flexibility and power, find their uses in various aspects of computing and data processing. In this section, we'll explore some common practical applications of regex.

#### Data Validation

One of the main uses of regex is to validate if data fits a certain pattern. This is commonly used in form validation.

- **Email Validation**:

  ```python
  pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
  ```

  This pattern ensures an input string roughly matches the structure of an email.

- **URL Validation**:

  ```python
  pattern = re.compile(r'^(http://|https://)?(www\.)?[\w-]+\.[\w]{2,}$')
  ```

  This pattern matches web URLs, whether they start with `http://`, `https://`, or simply `www.`.

#### Data Extraction and Grouping

Regex can be used to extract specific portions of data from a larger text.

- **Extract Date Components**:

  ```python
  pattern = re.compile(r'(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})')
  match = pattern.search('The date is 15/04/2020.')
  ```

  Here, the day, month, and year are extracted as separate named groups from a date string.

#### String Replacement

Using regex, you can find and replace patterns within strings.

- **Censoring Words**:

  ```python
  def censor(text):
      pattern = re.compile(r'\b(badword1|badword2|badword3)\b', re.I)
      return pattern.sub('****', text)
  ```

  This function replaces specified "bad words" in a text with asterisks, making the content family-friendly.

#### Real-world Scenarios

- **Log Analysis**: System administrators often use regex to parse logs, identifying anomalies or important events.
- **Web Scraping**: Developers can use regex to extract specific data from web pages.
- **Code Refactoring**: Programmers can use regex in IDEs to find and replace patterns in the code.
- **Search Engines**: Many search functionalities use regex under the hood to deliver accurate results based on complex search patterns.

#### Key Takeaways

- Regular expressions are not just academic constructs but have numerous practical applications in real-world scenarios.
- From validating user input to extracting specific data from large datasets, regex is a powerful tool in a developer's arsenal.
- While regex is powerful, it's important to use it judiciously, especially in situations where performance is a concern, as complex regex operations can be resource-intensive.

### Mini-Example: Extracting Phone Numbers with Regex

Imagine you're given a block of text with mixed content, and you want to extract all phone numbers from it. Regular expressions can be the perfect tool for this task. Let's see how:

```python
import re

# Sample text with phone numbers
text_content = """
John's contact: 123-456-7890
Office landline: (123) 456-7890
Jenny: 123.456.7890
Emergency: 987-654-3210
"""

# Regular expression pattern to extract phone numbers
pattern = re.compile(r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})')

# Extract phone numbers
phone_numbers = pattern.findall(text_content)

# Display the extracted phone numbers
for number in phone_numbers:
    print(number)
```

In the above example:
- We use the regex pattern `r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'` to match various phone number formats, such as `123-456-7890`, `(123) 456-7890`, and `123.456.7890`.
- The `findall()` function extracts all matched phone numbers from the sample text.
- The result would be a list of extracted phone numbers.

This simple yet effective example demonstrates the flexibility and power of regex in extracting specific patterns from textual data.

## Project: Data Scraper

### Objective

Develop a Data Scraper that can extract meaningful information, specifically email addresses and phone numbers, from raw textual data using regular expressions. This will give you practical experience in using regex for pattern matching and data extraction.

### Requirements

- **Data Source**: You will be given a block of text with mixed content.
- **Data Extraction**:
  - Extract all email addresses present in the text.
  - Extract all phone numbers present in the text.
- **Pattern Matching**: Utilize regular expressions to identify and extract the required data.
- **Data Presentation**: Display the extracted data in a user-friendly and structured format.

### Guidance

1. **Analyzing the Data**:
   - Familiarize yourself with the given textual data. Identify the patterns of email addresses and phone numbers.
   
2. **Crafting Regular Expressions**:
   - Develop a regex pattern that matches email addresses.
   - Develop a separate regex pattern that matches phone numbers.
   - Test both regex patterns with various samples to ensure they're accurate.

3. **Extracting Data**:
   - Use the `findall()` function to extract all email addresses and phone numbers matched by your regular expressions from the text.
   - Store the results in separate lists for further processing or presentation.

### Sample Interaction

Given a block of text, the Data Scraper should output:

\```
Extracted Email Addresses:
- support@example.com
- sales@example.org
- emergency@example.com

Extracted Phone Numbers:
- 555-1234
- 555-5678
- 555-9111
\```

### Let's Get Coding!

With the guidelines and requirements in mind, it's time to put theory into practice!

- **Starting Point:** Utilize the code skeleton in the chapter's [`/code/`](https://github.com/07-regular-expressions/code/) folder as a foundation for your Data Scraper.
- **Solution:** If you find yourself stuck or simply curious about one possible implementation, peek into the [`/code/answer/`](https://github.com/07-regular-expressions/code/answer/) folder. Remember, there are multiple ways to solve programming challenges, and the provided solution is just one of them.

### Tips

1. Start small. Initially, focus on extracting one type of data, either email or phone number.
2. Test your regex patterns using online platforms like [Regex101](https://regex101.com/).
3. Once you're confident about your regex patterns, integrate them into your Python script.
4. Always validate the output to ensure you're extracting data as expected.

### Closing Thoughts

Regular expressions are a powerful tool, especially when it comes to extracting specific patterns from large blocks of text. This project allows you to see the practical applications of regex. As you move forward, you'll find numerous scenarios where regex can be an invaluable tool in your programming toolkit.


## Quiz

Ready to test your knowledge? Take the Chapter 7 quiz [here](https://dsj7419.github.io/python-learning-by-projects/07-regular-expressions/quiz/).

## Next Steps

Congrats on completing the chapter on Regular Expressions! 🎉 With the power of regex, you've unlocked a sophisticated tool for text manipulation, search, and data extraction, allowing you to handle complex data processing tasks with ease.

In the [next chapter](08-exception-handling/README.md), we will delve into exception handling, equipping you with the skills to manage unexpected events and errors in your code gracefully.

## Additional Resources

- [Python Docs: Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [Regex101: Online Regex Tester and Debugger](https://regex101.com/)
- [Regexr: Learn, Build, & Test RegEx](https://regexr.com/)
- [W3Schools: Python RegEx](https://www.w3schools.com/python/python_regex.asp)
- [Real Python: Regular Expressions: Regex in Python](https://realpython.com/regex-python/)

Dive in and explore further. The world of regular expressions offers a plethora of patterns, techniques, and applications just waiting to be discovered!

---
Happy Coding! 🚀

[Back to Main](https://dsj7419.github.io/python-learning-by-projects/)