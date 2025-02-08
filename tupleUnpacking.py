# Tuple Unpacking
# 
# We can assign each element of a tuple to a seperate variable in Python. This is called Tuple unpacking.

# This is usually used when you are calling multiple values from a function or when you have an ndividual use case fdor each variable that is extracted.
# 
person = ("Carlos", "Vanzego", "28")

(firstName, lastName, age) = person

print(firstName)
print(lastName)
print(age)