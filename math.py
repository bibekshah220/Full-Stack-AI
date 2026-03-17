# Build a Custom python module



def add (a, b):
    return a + b

def subtract (a, b):
    return a - b    

def multiply (a, b):
    return a * b  
  
def divide (a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
    

    #cresate a  module for string operations, including functions to reverse a string count vowels and check for palindeomes. import into a script and test the functions.
def reverse_string(s):
    return s[::-1]  

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
    