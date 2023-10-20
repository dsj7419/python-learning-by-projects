
# Chapter 7: Regular Expressions

Welcome to Chapter 7, where we explore Regular Expressions in Python! 🎯 In this chapter, we'll dive deep into pattern matching and data extraction using regular expressions, enhancing our ability to process textual data. Furthermore, we'll work on a project: Data Scraper, which will leverage our new skills to extract meaningful data from textual content.

## Table of Contents

- [Introduction](#introduction)
- [Lesson Plan](#lesson-plan)
  - [1. Basics of Regular Expressions](#1-basics-of-regular-expressions)
    - [Understanding the Need for Regex](#understanding-the-need-for-regex)
    - [Basic Regex Characters](#basic-regex-characters)
    - [Quantifiers in Regex](#quantifiers-in-regex)
    - [Basics Key Takeaways](#basics-key-takeaways)
  - [2. Advanced Regular Expressions](#2-advanced-regular-expressions)
    - [Lookaheads and Lookbehinds](#lookaheads-and-lookbehinds)
    - [Word Boundaries](#word-boundaries)
    - [Character Classes](#character-classes)
    - [Flags in Regex](#flags-in-regex)
    - [Advanced Key Takeaways](#advanced-key-takeaways)
  - [3. Practical Applications of Regex](#3-practical-applications-of-regex)
    - [Data Validation](#data-validation)
    - [Data Extraction and Grouping](#data-extraction-and-grouping)
    - [String Replacement](#string-replacement)
    - [Real-world Scenarios](#real-world-scenarios)
    - [Applications Key Takeaways](#applications-key-takeaways)
- [Mini-Example: Extracting Phone Numbers with Regex](#mini-example-extracting-phone-numbers-with-regex)
- [Project: Data Scraper](#project-data-scraper)
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

#### Basics Key Takeaways

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

#### Advanced Key Takeaways

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

#### Applications Key Takeaways

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

In today's interconnected world, data is abundant, often in unstructured formats. This project challenges you to create a data scraper capable of extracting specific information, such as email addresses and phone numbers, from a block of raw textual data. By leveraging the power of regular expressions, you'll hone your skills in pattern recognition and data extraction.

### Requirements

- **Data Source**: Work with a textual block containing mixed content.
- **Data Extraction**:
  - Extract all email addresses embedded in the text.
  - Extract all phone numbers interspersed within the text.
- **Pattern Matching**: Harness the strength of regular expressions to detect and extract the targeted data.
- **Data Presentation**: Ensure the extracted data is displayed in an organized and user-friendly manner.

### Detailed Guidance

1. **Data Analysis**:
   - Start by examining the provided text block, discerning the patterns characterizing email addresses and phone numbers.
   
2. **Constructing Regular Expressions**:
   - Formulate a regex pattern adept at capturing email addresses.
   - Conceive a distinct regex pattern for pinpointing phone numbers.
   - Validate both regex patterns using diverse sample inputs to ascertain their accuracy.

3. **Data Extraction**:
   - Deploy the `findall()` method to mine all email addresses and phone numbers that your regex patterns can match from the text.
   - Catalog the results in distinct lists for subsequent processing or display.

### Sample Interaction

```
Given the following text:

"Hello,

You can reach out to us at support@example.com or call us at 555-1234. Alternatively, you can contact our sales team at sales@example.org or on their direct line 555-5678.

In case of urgent inquiries during non-working hours, please contact emergency@example.com or call 555-9111.

Thank you,
Your Example Team"

The Data Scraper should deduce:

Extracted Email Addresses:
- support@example.com
- sales@example.org
- emergency@example.com

Extracted Phone Numbers:
- 555-1234
- 555-5678
- 555-9111
```

### Let's Get Coding!

Equipped with the guidelines and stipulated requirements, it's coding time!

- **Starting Point**: Dive into the chapter's [`/code/`](https://github.com/07-regular-expressions/code/) directory and leverage the furnished code skeleton as a base for your Data Scraper.
- **Solution**: If you hit a roadblock or are intrigued about a potential solution, you can glance at the [`/code/answer/`](https://github.com/07-regular-expressions/code/answer/) directory. Yet, keep in mind that multiple paths lead to the solution in programming, and the proffered solution is merely one route among many.

### Tips

1. Initiate with modest goals. First, concentrate on extracting one type of data, be it an email or phone number.
2. Evaluate your regex patterns on platforms like [Regex101](https://regex101.com/) to confirm their efficacy.
3. Upon attaining confidence in your regex patterns, incorporate them into your Python script.
4. Always cross-check the output to ascertain correct data extraction.

### Closing Thoughts

Regular expressions, while intricate, present a formidable technique for pattern detection and data extraction in vast text chunks. This endeavor immerses you in the practical utility of regex. As you forge ahead, numerous situations will arise where regex emerges as a quintessential instrument in your developer's arsenal.

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