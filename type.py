# Type Keyword
# The built-in function type() returns the type of an object. In Python3, everything is an object and thus an instance of a class. Therefore, the built-in function type() can be used to return the class type of the passed variable.
# Ex
# 
# output: <class 'int'> because I passed an integer.
type(8)
print(type(8))

# output: <class 'str'> because I passed a string.
type("Hello friend.")
print(type("Hello friend."))

# output: <class 'dict'> because I passed a dictionary.
type({"age": 24})
print(type({"age": 24}))

# output: <class 'list'> because I passed a list.
type([1,2,3,4,5])
print(type([1,2,3,4,5]))

# output: <class 'float'> because I passed a float.
type(4.0)
print(type(4.0))

# output: <class 'bool> because I passed a boolean.
type(False)
print(type(False))

# output: <class 'NoneType'> because I passed None.
type(None)
print(type(None))

# output: <class 'tuple> because I passed a tuple.
type((10,9,8))
print(type((10,9,8)))

# output: <class 'set'> because I passed a set.
type({1,2,3,4,5,6})
print(type({1,2,3,4,5,6}))

# output: <class 'frozenset'> because I passed a frozenset. A frozenset is an immutable version of a set. Meaning it is a set thats values can not be changed.
my_set = {10, 4, 7, 1 ,8 , 6}
# I created a variable called 'my_frozenset' and assigned it the 'frozenset' class, and passed the 'my_set' variable I created above.
my_frozenset = frozenset(my_set)
print(my_set)



# I created a variable called 'randomType' and assigned it the value 'type(14)' which is an instance of the 'type' class and I am passing the integer 14.
randomType = type("Hi")
# the output will be <class 'int'>
print(type("Hi"))


# this is a list I passed with mixed elements; the output will be of type list.
type(['this', 'is', 'list', 'number', 2])
print(type(['this', 'is', 'list', 'number', 2]))



