import re

# Example text for scraping
example_text = """
Hello,

You can reach out to us at [email] or call us at [phone number]. Alternatively, you can contact our sales team at [email] or on their direct line [phone number]. 

In case of urgent inquiries during non-working hours, please contact [email] or call [phone number].

Thank you,
Your Example Team
"""

# HINT: Define a regular expression pattern to extract email addresses.
# Regular expression for extracting email addresses
# email_pattern = re.compile(r"...")

# HINT: Define a regular expression pattern to extract phone numbers. Remember to consider optional periods at the end.
# Regular expression for extracting phone numbers
# phone_pattern = re.compile(r"...")

# HINT: Use findall() or finditer() to extract email addresses and phone numbers from the text.
# Extracting data using findall
# emails = email_pattern.findall(example_text)
# phone_numbers = phone_pattern.findall(example_text)

# Displaying extracted data
print("Extracted Email Addresses:")
# HINT: Iterate through the extracted emails and print them. Consider using a loop.

print("\nExtracted Phone Numbers:")
# HINT: Iterate through the extracted phone numbers and print them. Consider using a loop, and ensure that the extracted data is displayed in a readable format.
