#check if a string is a palindrome
def is_palindrome(text):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_text = ''.join(text.split()).lower()
    # Check if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')
    