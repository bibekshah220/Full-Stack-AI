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


