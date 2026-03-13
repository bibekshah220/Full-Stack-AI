# for loop
fruits = ["apple", "banana", "cherry"] 
for fruit in fruits:
    print(fruit)

# loop with range
for i in range(5): # [0, 1, 2, 3, 4]
    print(i)

# while loop
count = 5
while count > 0:
    print(count)
    count -= 1

    #break for loop
    for i in range(10):
        if i == 5:
            break
        print(i)  
        # output: 0, 1, 2, 3, 4  
#continue for loop
for i in range(10):
    if i  == 7:
        continue
    print(i)
    # output: 0, 1, 2, 3, 4, 5, 6, 8, 9
