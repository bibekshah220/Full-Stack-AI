# what is Pythonic code
# ----------------------
# "Pythonic" code follows Python's idioms and conventions: it is clean,
# readable, and uses Python's built-in features the way they were designed to
# be used, instead of copying patterns from other languages (like C or Java).
# The guiding philosophy is "The Zen of Python" (run: import this).


# 1. Looping directly over items, not indexes
names = ["Alice", "Bob", "Carol"]

# Non-Pythonic
for i in range(len(names)):
    print(names[i])

# Pythonic
for name in names:
    print(name)


# 2. Use enumerate() when you need the index AND the value
# Pythonic
for index, name in enumerate(names):
    print(index, name)


# 3. List comprehensions instead of manual loops + append
# Non-Pythonic
squares = []
for n in range(10):
    squares.append(n * n)

# Pythonic
squares = [n * n for n in range(10)]


# 4. Truthiness: check emptiness directly
items = []

# Non-Pythonic
if len(items) == 0:
    print("empty")

# Pythonic
if not items:
    print("empty")


# 5. Multiple assignment / swapping without a temp variable
a, b = 1, 2
a, b = b, a  # swap


# 6. Use zip() to iterate over multiple sequences together
ages = [30, 25, 40]
for name, age in zip(names, ages):
    print(f"{name} is {age}")


# 7. Use 'in' to test membership
if "Alice" in names:
    print("found")


# 8. Context managers ('with') for handling resources like files
# Pythonic: file is closed automatically
with open("example.txt", "w") as f:
    f.write("hello")

