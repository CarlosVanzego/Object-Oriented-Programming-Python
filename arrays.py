# Arrays
# 
# In Python, an array is a data structure similar to a list but is optimized for storing homogeneous elements (elements of the same type). Python's built-in array module provides support for operations on arrays.
# Ex.
# 
# this line imports the array class from the array module.
from array import array 

# Creating an array of integers.
# Include  'i' for integers, 'f' for floating points, 'u' for Unicode characters
arr = array('i', [0,1,2,3,4])

# Append a new element 
arr.append(5)
print(arr)

# Inserts 8 at index 2
arr.insert(2, 8)
print(arr)

# Appends 8,9,10 to the array
arr.extend([8, 9, 10])
print(arr)

# Removes the first occurence of 3
arr.remove(1)
print(arr)

# Returns the index of the first occurence of 4
arr.index(2)
print(arr)

# Access elements
print(arr[4])