import re

def clean_text(text):
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

    #convert the text to lowercase
    text = text.lower()
    return text

    input_text = input("hello im bibek: ")
    cleaned_text = clean_text(input_text)
    print("Cleaned text:", cleaned_text)