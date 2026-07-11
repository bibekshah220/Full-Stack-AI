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