# Example 1: checking a condition
num = 10
if num > 5:
    print("positive number")
elif num == 5:
    print("five")
else:
    print("Negative number")

# Example 2: nested conditions
age = 25
if age > 18:
    if age < 30:
        print("You are a young adult.")
    else:
        print("You are an adult.")
    