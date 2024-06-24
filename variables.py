# Set a new variable; type is inferred from assigned value
x = 5

# Use f and simple quotes (enclosing sentence) to interpolate variables inside
# the to-be-printed message
print(f'x is equal to {x} and its type is {type(x)}')

# Set new value of a different type to the variable;
x = "6"

# Show the new value of x
print(f'x new value is equal to {x} and its type is {type(x)}')

# Try to add variables of different data types
# y = 5 + x # <- Error - can't have an str added to an int
# y = x + 5 # <- Error - can't have an str added to an int
# y = True + x Error - can't have an str added to an boolean
# y = x + True - can't have an str added to an boolean

# Adding a boolean value to an int value
x = 5
x = True + x
print(f'x new value is equal to {x} after adding True and its type is {type(x)}')

# Adding a boolean value to a float value
x = 5.1
x = True + x
print(f'x new value is equal to {x} after adding True and its type is {type(x)}')

# Arrays with elements of varying data types
x = [2,'2',False]
print(f'x new value is equal to {x} and its type is {type(x)}')

# Array using list comprehension
x = [i for i in x]
print(f'x new value is equal to {x} and its type is {type(x)}')

# Array using list function; argument may be any sequency, including str
x = list('abc')
print(f'x new value is equal to {x} after storing list(\'abc\') in it, and its type is {type(x)}')

# Reassigning one of the addresses in the array to a new value
x[0] = 2
print(f'x new value is equal to {x} after reassigning first value, and its type is {type(x)}')

# Tuple with data of multiple data types
x = (1,2,"d")
print(f'x new value is equal to {x} and its type is {type(x)}')

# Reassigning one the tuple's first index to a new value
# x[0] = 2 # <- Error - Can't assign new value to a tuple
# print(f'x new value is equal to {x} and its type is {type(x)}')

# Displaing first index of a tuple
print(f'x tuple first element is {x[0]}')

# There is no comprehension method to create a new tuple
x = (i for i in x) # <- creates an generator instead; note the () in lieu of []
print(f'x new value is equal to {x} and its type is {type(x)}')
# Printing each element of the tuple
indice = 0
for i in x:
    print(f'Element at position {indice} is {i}')
    indice += 1
# See https://bit.ly/3RbB7it

# Turning a generator into a tuple using the tuple function
x = tuple(x)
print(f'x new value is equal to {x} and its type is {type(x)}')

# Creating range objects; a type of sequence
x = range(50)
print(f'x new value is equal to {x} and its type is {type(x)}')

# The actual numbers in the sequence are generated as the sequence gets
# accessed
print(f'x new value at position 5 is {x[5]}')

# Creating dictionaries
x = {
    "The Mentalist":["Patrick Jane", "Cho", "Lisbon", "Van Pelt", "Rigsby"],
    "Severance":["Mark", "Helly", "Peggy", "Ms. Casey"]
}
print(f'x new value is {x} and its type is {type(x)}')

# Creating sets; sets itens may appear in different posision when called
x = {"The Mentalist", 3}
print(f'x new value is {x} and its type is {type(x)}')

# Trying to access an specif entry by index
# print(f'Value at position 0 is {type(x[0])}') # < - Error - Cant access position

# Trying to store two equal values; Only one remains
x = {"The Mentalist", 3, 3}
print(f'x new value is {x} and its type is {type(x)}')
