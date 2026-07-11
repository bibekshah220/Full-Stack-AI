
with open("sample.txt", "r") as file:
    # read() reads the entire content of the file.
    content = file.read()

    # Display the complete file content.
    print("Complete File Content:")
    print(content)


print("\nReading Line by Line:")

# Open the file again because after read(),
# the file pointer reaches the end of the file.
with open("sample.txt", "r") as file:

    # Loop through each line in the file.
    for line in file:
        # strip() removes the newline character (\n)
        # from the end of each line.
        print(line.strip())


print("\nReading First 10 Characters:")

# Exception handling is used to prevent the program
# from crashing if an error occurs.
try:
    with open("sample.txt", "r") as file:

        # read(10) reads only the first 10 characters.
        first_ten = file.read(10)

        print(first_ten)

# This exception occurs if the file does not exist.
except FileNotFoundError:
    print("Error: sample.txt file was not found.")

# This exception handles other input/output errors.
except IOError:
    print("Error: Unable to read the file.")