# 
first = "bibek"
last = "shah"
full = first + " " + last
# print(full)

text = "Hello, World!"
print(text[0])  # Output: 'H'
print(text[7])  # Output: 'W'

#formatting strings
name = "bibek"
age = 25
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is bibek and I am 25 years old.
print(f"My name is {name} and I am {age} years old.")  #Output: My name is bibek and I am 25 years old.

#commom string methods
text = "Hello, World!"
split_text = text.split(",")  # splits the string into a list of substrings based on the comma delimiter
print(split_text)  # Output: ['Hello', ' World!']

joined_text = " ".join(split_text)  # joins the list of substrings into a single string with a space as the delimiter
print(joined_text)  # Output: 'Hello World!'

replaced_text = text.replace("World", "Python")  # replaces the substring "World" with "Python"
print(replaced_text)  # Output: 'Hello, Python!'

stripped_text = text.strip("!")  # removes the exclamation mark from the end of the string
print(stripped_text)  # Output: 'Hello, World'

# Regular expressions for pattern matching
# what are regular expressions?
""" Regular expressions (regex) are a powerful tool for pattern matching and text manipulation. They allow you to search for specific patterns in strings, extract information, and perform complex text transformations. Regular expressions are widely used in programming, data analysis, and text processing tasks. """  
# using the re module in Python, you can work with regular expressions to perform tasks such as searching for patterns, validating input, and extracting data from text. Regular expressions use a combination of special characters and syntax to define patterns that can match specific sequences of characters in strings.


import re

# common functions in the re module

# re.search() - Searches the entire string for the first occurrence
# of a pattern and returns a Match object if found. If the pattern
# is not found, it returns None.

text = "Python was released in 1991."

match = re.search(r"\d{4}", text)  # Search for a 4-digit number

if match:
    print(match.group())   # Output: 1991
    print(match.start())   # Output: 23
    print(match.end())     # Output: 27
    print(match.span())    # Output: (23, 27)
else:
    print("No match found.")

    