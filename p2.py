# create a program to find the largest number in a list using a for loop
numbers = [3, 5, 7, 2, 8]
largest = numbers[0]  # Assume the first number is the largest
for num in numbers:
    if num > largest:
        largest = num
print(f"The largest number in the list is: {largest}")
        