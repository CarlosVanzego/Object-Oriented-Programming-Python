# Tuples 
# 
# A tuple is similar to a list but, the main difference is that it's immutable once it's created. You cannot add or remove items in a tuple once you create it.
# Tuples are typically used when you want the data to remain unchanged throughout the program. It can be indexed just like a list and can have duplicates. It can hold multiple data types as well.
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


tuesdayTuple = ("Today", "is ", "Tuple", "Tuesday🤓")
print(tuesdayTuple)


# Another explanation:
# 
# A tuple is a collection of objects that are ordered and immutable. Tuples are defined by having values between parentheses (). Tuples are immutable, meaning that the values inside the tuple cannot be changed. Tuples are used to store multiple items in a single variable.

# Creating a tuple:
my_tuple = (4, "berry", 3.14, True)

# Accessing elements in a tuple:
print(my_tuple[1])
print(my_tuple[3])

# Iterating through the element of my_tuple:
for x in my_tuple:
    print(x)
# Another way to iterate through a tuple (will show the same output):
for item in my_tuple:
    print(item)   

# Tuple packing and unpacking:
a, b, c, d = my_tuple  
# output is 4
print(a)
# output is "berry"
print(b)

# -----------------------


def linear_search(list, key):
    #Returns the number of steps to determine if key is in the list 

    #Initialize the counter of steps
    steps=0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    return steps 

def binary_search(list, key):
    #Returns the number of steps to determine if key is in the list 

    #List must be sorted:
    list.sort()

    #The Sort was 1 step, so initialize the counter of steps to 1
    steps=1

    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        
        if list[middle] == key:
            break
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return steps 

def best_search(list, key):
    steps_linear = linear_search(list, key) 
    steps_binary = binary_search(list, key) 
    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "
    if (steps_linear < steps_binary):
        results += "Best Search is Linear."
    elif (steps_binary < steps_linear ):
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."

    return results

print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
#Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
#Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
#Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
#Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.