# A tuple is a collection of objects that are ordered and immutable. Tuples are defined by having values between parentheses (). Tuples are immutable, meaning that the values inside the tuple cannot be changed. Tuples are used to store multiple items in a single variable.

# Creating a tuple:
my_tuple = (4, "berry", 3.14, True)

# Accessing elements in a tuple:
print(my_tuple[3])
print(my_tuple[1])

# Iterating through a tuple:
for x in my_tuple:
    print(x)
# Another way to iterate through a tuple:
for item in my_tuple:
    print(item)   

# Tuple packing and unpacking:
a, b, c, d = my_tuple  
# output is 4
print(a)
# output is "berry"
print(b)