# write a program to reverse a list and remove duplicates usinf sets

my_list = [1, 2, 3, 4, 5, 2, 3]
# reverse the list
reversed_list = my_list[::-1]
# remove duplicates using sets
unique_list = list(set(reversed_list))
print(unique_list)
