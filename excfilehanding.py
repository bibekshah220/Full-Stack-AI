# Write data into a file

with open("student.txt", "w") as file:
    file.write("Bibek Shah\n")
    file.write("Computer Engineering\n")
    file.write("Kathmandu")

print("Data written successfully.")

# Read the complete file

with open("student.txt", "r") as file:
    content = file.read()

print(content)

# Read file line by line

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())

# Count total lines in a file

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))


# Count total words

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total Words:", len(words))

# Count total characters

with open("student.txt", "r") as file:
    content = file.read()

print("Total Characters:", len(content))

# Add new data without deleting old data

with open("student.txt", "a") as file:
    file.write("\nPython Programming")

print("Data appended successfully.")

# Copy contents from one file to another

with open("student.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as destination:
    destination.write(data)

print("File copied successfully.")

# Search a word in a file

word = input("Enter a word to search: ")

with open("student.txt", "r") as file:
    content = file.read()

if word in content:
    print("Word Found")
else:
    print("Word Not Found")

# Count vowels

with open("student.txt", "r") as file:
    content = file.read().lower()

count = 0

for ch in content:
    if ch in "aeiou":
        count += 1

print("Total Vowels:", count)

# Count uppercase and lowercase letters

with open("student.txt", "r") as file:
    content = file.read()

upper = 0
lower = 0

for ch in content:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)