# Set a new variable; type is inferred from assigned value
x = 5

# Use f and simple quotes (enclosing sentence) to interpolate variables inside
# the to be printed message
print(f'x is equal to {x} and its type is {type(x)}')

# Set new value of a different type to the variable;
x = "6"

# Show the new value of x
print(f'x new value is equal to {x} and its type is {type(x)}')

# Try to add variables of different data types
# y = 5 + x # <- Error - can't have an str added to an int
# y = 5 + y # <- Error - can't have an str added to an int
# y = True + xError - can't have an str added to an boolean

# Adding a boolean value to an int value
x = 5
x = True + x
print(f'x new value is equal to {x} and its type is {type(x)}')

# Adding a boolean value to a float value
x = 5.1
x = True + x
print(f'x new value is equal to {x} and its type is {type(x)}')

# Arrays with elements of varying data types
x = [2,'2',False]
print(f'x new value is equal to {x} and its type is {type(x)}')

# Array using list comprehension
x = [i for i in x]
print(f'x new value is equal to {x} and its type is {type(x)}')

# Array using list function; argument may be any sequency, including str
x = list('abc')
print(f'x new value is equal to {x} and its type is {type(x)}')

# Reassigning one of the addresses in the array to a new value
x[0] = 2
print(f'x new value is equal to {x} and its type is {type(x)}')

# Tuple with data of multiple data types
x = (1,2,"d")
print(f'x new value is equal to {x} and its type is {type(x)}')

# Reassigning one of the addresses in the tuple to a new value
# x[0] = 2 # <- Error - Can't assign new value
# print(f'x new value is equal to {x} and its type is {type(x)}')

# Using comprehension to create new tuples
x = (i for i in x)
print(f'x new value is equal to {x} and its type is {type(x)}')
print(next(x))
print(next(x))
print(next(x))
