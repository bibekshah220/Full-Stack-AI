import re

text = "contact me at 9847301111 or email me at bibekshah@gmail.com"
digit = re.findall(r"\d{10}", text)  # Find all 10-digit numbers
print(digit)  # Output: ['9847301111']

updated_text = re.sub(r"\d{10}", "XXXXXXXXXX", text)  # Replace all 10-digit numbers with XXXXXXXXXX
print(updated_text)  # Output: contact me at XXXXXXXXXX or email me at bib