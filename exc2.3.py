#write a program to count the number of vowels in a given string

def count_vowels(text):
    # Define a set of vowels for easy lookup
    vowels = set("aeiouAEIOU")
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the text
    for char in text:
        if char in vowels:  # Check if the character is a vowel
            vowel_count += 1  # Increment the counter if it is a vowel
            
    return vowel_count  # Return the total count of vowels  