import math_operations as mo

num1 = 10
num2 = 5
print(f"Addition: {mo.add(num1, num2)}")
print(f"Subtraction: {mo.subtract(num1, num2)}")    
print(f"Multiplication: {mo.multiply(num1, num2)}")
print(f"Division: {mo.divide(num1, num2)}")

import string_operations as so
s = "Hello World"
print(f"Reversed String: {so.reverse_string(s)}")
print(f"Vowel Count: {so.count_vowels(s)}")
print(f"Is Palindrome: {so.is_palindrome(s)}")