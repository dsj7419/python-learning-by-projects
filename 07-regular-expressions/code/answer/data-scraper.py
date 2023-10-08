import re

# Example text for scraping
example_text = """
Hello,

You can reach out to us at support@example.com or call us at 555-1234. Alternatively, you can contact our sales team at sales@example.org or on their direct line 555-5678. 

In case of urgent inquiries during non-working hours, please contact emergency@example.com or call 555-9111.

Thank you,
Your Example Team
"""

# Regular expression for extracting email addresses
email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
# Regular expression for extracting phone numbers
phone_pattern = re.compile(r"(\b\d{3}-\d{4}\b)(?:\.)?")

# Extracting data using findall
emails = email_pattern.findall(example_text)
phone_numbers = phone_pattern.findall(example_text)

# Displaying extracted data
print("Extracted Email Addresses:")
for email in emails:
    print(f"- {email}")

print("\nExtracted Phone Numbers:")
for match in phone_pattern.finditer(example_text):
    print('-', match.group(1))