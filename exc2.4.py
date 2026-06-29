# create a program to find and replace all email address in a text using regex

import re

def replace_emails(text, replacement):
    # Define the regex pattern for email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # Replace all occurrences of the pattern with the replacement string
    return re.sub(email_pattern, replacement, text)

input_text = input("Enter a text with email addresses: ")
replacement_text = input("Enter the replacement text: ")
result = replace_emails(input_text, replacement_text)
print("Updated text:", result)
