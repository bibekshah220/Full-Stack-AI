# Write data into a file

with open("student.txt", "w") as file:
    file.write("Bibek Shah\n")
    file.write("Computer Engineering\n")
    file.write("Kathmandu")

print("Data written successfully.")