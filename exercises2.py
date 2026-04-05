# word ferquency counter
sentence = input("Enter a sentence: ")

# split the sentence into words
words = sentence.split() # split() method splits the string into a list of words based on whitespace

#initilize an empty dictionary to store word frequencies
word_freq = {}

# count the frequency of each word
for word in words:  
    word = word.lower()  # convert the word to lowercase to ensure case-insensitivity
    if word in word_freq:
        word_freq[word] += 1  # increment the count if the word is already in the dictionary
    else:
        word_freq[word] = 1  # add the word to the dictionary with a count of 1

# print the word frequencies
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
    