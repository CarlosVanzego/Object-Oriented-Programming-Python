# Map Function
# 
# When you want to apply a function over each element of an iterable (list, tuple, set, etc), you can use the map() function. The map() function returns an iterable object after the function has been applied onto the input.
# 
# Syntax:
# map(function, iterable)
# 
# Function: It is a function to which map passes each element of a given iterable.
# Iterable: It is a data structure which is to be mapped, can be a list, tuple, set etc.
# 
# This is function called 'calculateLength', that returns the length of an iterable and a tuple fruits.
def calculateLength(n):
  return len(n)

fruits = ('apple', 'banana', 'cherry')

lengthOfItems = map(calculateLength, fruits)
print(list(lengthOfItems))

# In the above example, I pass two arguments to the map() function (calculateLength and fruits).
# The 'calculateLength' function runs on each item of the tuple fruits and returns the item's length.
# The lengths of these items are stored in a variable called 'lengthOfItems'.