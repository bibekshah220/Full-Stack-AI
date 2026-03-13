# write a program to calculate the factorial of a number using a while loop
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1.")  
        