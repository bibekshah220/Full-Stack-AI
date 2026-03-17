#create a function with parameters

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 10)
print(result)   

# local scope
def cooding():
    x = 10
    print(x)

cooding()   

# global scope
x = 10
def coding():
    print(x)

coding()       


