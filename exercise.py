# manipulate data in a diconary
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

# iteration
for key, value in person.items():
    print(f"{key}: {value}") # Output: name: bibek
                             #         age: 26  
                             #        city: Kathmandu   
# Add new key-value pair
person["country"] = "Nepal"
print(person)  # Output: {'name': 'bibek', 'age': 26, 'country': 'Nepal'}
person["name"] = "bibek shah"
print(person)  # Output: {'name': 'bibek shah', 'age': 26, 'country': 'Nepal'}
#update age
person["age"] = 27
print(person)  # Output: {'name': 'bibek shah', 'age': 27, 'country': 'Nepal'}
person.pop("age")
print(person)  # Output: {'name': 'bibek shah', 'country': 'Nepal'}
person.clear()
print(person)  # Output: {}

