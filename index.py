# Hear is full python programming language

#(1) 2 types of comments
#=========================

"""
Multiline commend
hear you can write lots off program
and do your best 
"""

#(2) Variable names
#======================
# Pascal Case
# CamelCase
# snakeCase
# Assign Multiple Values
a, b, c = 'sohag', 'riya', 'ritu'
d = e = f = 'aminul'

#(3) Built in Data Types
#=========================
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Types: True, False
# Binary Types: bytes, bytearray, memoryview
# None Type: None

#(4) Python Operatiors
#===========================
# Arithmetic Operators ->| + - * / % ** //
# Assignment Operators ->| = += -+ *= /= %= **= //=
# Comparison Operators ->| == != > < >= <=
# Logical Operators    ->| and or not
# Identity Operators   ->| is is not
# Membership Operators ->| in not in
# Bitwise Operators    ->| & | ^ << >>

#(5) Python Conditions
#===========================
# if elif else

#(6) Python Loops
#==========================
# i = 0 while i < 6: i += 1
# for i in range(6): print(i)

#(7) Python Function
#===========================
# def fnc(): print('hello world')
# x = lambda a : a + 10

# Python String
#===========================
""" 
startswith()
endswith()
count()
index()
isalpha()
title()
casefold()
capitalize()
center()
ljust()
rjust()
zfill()
encode()
strip()
lstrip()
rstrip()
split()
join()
s[::-1] - Reversing a string
upper()
lower()
swapcase()
s2 in s1 - membership operator
find()
replace()
zip()
# --checking Anagrams
# --checking Palindromes

"""


# Python List method
#========================
append()
pop()
insert()
reverse()
index()
remove()
copy()
count()
clear() 
sort()
slice [:]

# List comprehensions
squares = [x**2 for x in range(1, 11)]

# Slicing a list
first_two = squares[2:]

#--------------List End---------------




# Dictionaries of python
#=====================================
new_users = {
    'first': 'sohag',
    'last' : 'mia',
    'username' : 'sohag123'
}

print(new_users['first'])
new_users['pass'] = '12345'
del new_users['last']

for k, v in new_users.items():
    print(k + ":" + v)

lisst = []
lisst.append(new_users)

for user_dict in lisst:
    for k, v in user_dict.items():
        print(k + " = " + v)

# ---------Dictionaries End -------

# Making a function
def greet_user():
    pass
    
# Passing information to a function
def greet_user(username):
    pass
    
# Using positional arguments
def describe_pet(animal, name):
    pass
describe_pet('dog','while')

# Using keyword arguments
def describe_pet(animal, name):
    pass
describe_pet(name='while', animal='dog')

# Using a default value
def desribe_pet(name, animal='dog'):
    pass
describe_pet('while')

# Using None to make an argument optional
def describe_pet(animal, name=None):
    pass
if name:
    print("It's name is " + name + ".")
describe_pet('snake')

# Collecting an arbitrary number of arguments
def make_pizza(size, *toppings):
    for topping in toppings:
        print(toppings)

# collecting an arbirary number of keyword arguments
def build_profile(first, last, **user_info):
    profile = {'first': first, 'last': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


# -----------End of function ------------