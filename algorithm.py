# Exercise 1:
# Create a list with values ranging from 0 to 9.
# lst = list(range(10))
# print(lst)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exercise 2:
# Convert a list of integers to a list of strings.
# lst2 = [1,3,4, 5, ]
# str_lst2 = list(map(str, lst2))
# print(str_lst2)
# ['1', '3', '4', '5']

# Exercise 3:
# Multiply all elements in a list by 2.
# lst = [1, 2, 3, 4, 5, 6]
# multiplied_lst = [x*2 for x in lst]
# print(multiplied_lst)
# [2, 4, 6, 8, 10, 12]

# Exercise 4:
# Extract all odd numbers from a list of integers.
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_number = []
# for x in lst:
#     if x % 2 != 0:
#         odd_number.append(x)
# print(odd_number)

# Exercise 5:
# Replace all odd numbers in a list with -1
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# replaced_lst = [-1 if x % 2 != 0 else x for x in lst]
# print(replaced_lst)

# Exercise 6:
# Convert a list of integers to a list of booleans where all non-zero values become True.   
lst = [-1, 2, 0, -4, 5]
boolean_lst = []
for x in lst:
    boolean_lst.append(bool(x))
print(boolean_lst)
[True, True, False, True, True]
        
