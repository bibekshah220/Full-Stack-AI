# Read the content of a file

with open("sample.txt", "r") as file:
    # Read entire file content
    content = file.read()
    print(content)

print("Reading line by line:")

with open("sample.txt", "r") as file:
    # Read file line by line
    for line in file:
        print(line.strip())