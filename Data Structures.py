# what is list
# list is a collection of items in a particular order. It is a mutable data structure, which means that you can change the contents of a list after it has been created. Lists are defined by enclosing a comma-separated sequence of items in square brackets [].

# creating a list
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry']

mixed_list = [1, 'hello', 3.14, True]

# accessing list elements
print(numbers[0])  # Output: 1
print(fruits[1])  # Output: 'banana'
print(mixed_list[2])  # Output: 3.14

# modifying list elements
numbers[0] = 10 
print(numbers)  # Output: [10, 2, 3, 4, 5]
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

#Accessing indexes
print(numbers[0])  # Output: 10
print(numbers[1])  # Output: 2
print(numbers[2])  # Output: 3
print(numbers[3])  # Output: 4
print(numbers[4])  # Output: 5

# negative indexing
print(numbers[-1])  # Output: 5 
print(numbers[-2])  # Output: 4
print(numbers[-3])  # Output: 3
print(numbers[-4])  # Output: 2
print(numbers[-5])  # Output: 10

# tuples
colours = ('red', 'green', 'blue')
single_item = ("glass")

# accessing tuple elements
print(colours[0])  # Output: 'red'
print(colours[1])  # Output: 'green'    
print(colours[2])  # Output: 'blue'
print(colours[-1])  # Output: 'blue'

# Dictionaries
# A dictionary is a collection of key-value pairs. It is a mutable data structure, which means that you can change the contents of a dictionary after it has been created. Dictionaries are defined by enclosing a comma-separated sequence of key-value pairs in curly braces {}.
person = {
    "name": "bibek",
    "age": 25,
    "city": "Kathmandu"
}
# accessing dictionary values
print(person["name"])  # Output: 'bibek'
print(person["age"])  # Output: 25
print(person["city"])  # Output: 'Kathmandu'
# modifying dictionary values
person["age"] = 26
print(person)  # Output: {'name': 'bibek', 'age': 26, 'city': 'Kathmandu'}
del person["city"]
print(person)  # Output: {'name': 'bibek', 'age': 26}

#iteration
for key, value in person.items():
    print(f"{key}: {value}") # Output: name: bibek
                             #         age: 26  
                             #        city: Kathmandu

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
empty_set = set()
# adding elements to a set
set1.add(9) # Output: {1, 2, 3, 4, 5, 9}
# removing elements from a set
set1.remove(1)  # Output: {2, 3, 4, 5, 9}


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# union of sets
union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# intersection of sets
intersection_set = set1.intersection(set2)  # Output: {4, 5}
# difference of sets
difference_set = set1.difference(set2)  # Output: {1, 2, 3}


#intersection of sets
intersection_set = set1.intersection(set2)  # Output: {4, 5}
print(intersection_set)
print(set1 & set2)  # Output: {4, 5}   

