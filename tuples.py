# Tuples 
# 
# A tuple is similar to a list but the main difference is that it's immutable once it's created. You cannot add or remove items in a tuple once you create it.
# Tuples are typically used when you want the data to remain unchanged throughout the program. It can be indexed jsut like a list and can have duplicates. It can hold multiple data types as well.
# To create a Tuple, elements are placed inside these circular parentheses()
 
# Creating a tuple:
#
sampleTuple = ("LeBron", "Jordan", "Curry")

print(sampleTuple)


# Tuple Length:
sampleTuple2 = ("playstation", "xbox", "switch")
print(len(sampleTuple2))

# Accessing tuple elements:
sampleTuple3 = ("TV", "couch", "desk", "rug")
print(sampleTuple3[1])



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