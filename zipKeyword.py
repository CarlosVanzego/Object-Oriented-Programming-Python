# Zip Keyword
# 
# The zip() function takes multiple iterators as arguments and returns an iterator of tuples with the first item in each of the passed iterators as the first tuple, second item in each of the passed iterators as the second tuple and so on..
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
# 
# Syntax:
a = ("apple", "banana", "cherry")
b = ("blueberry", "mango", "orange", "lemon")

x = zip(a, b)

print(tuple(x))

# The zip function is useful in For Loops where you want cooresponding elements of 2 or more iterables. It makes the code look much more readable and concise.
# Ex.
# 
# zip(iterator1, iterator2, iterator3 ...)