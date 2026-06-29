import re

text = "contact me at 9847301111 or email me at bibekshah@gmail.com"
digit = re.findall(r"\d{10}", text)  # Find all 10-digit numbers
print(digit)  # Output: ['9847301111']
