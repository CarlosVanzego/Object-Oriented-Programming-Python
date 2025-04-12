# Lists 
# 
# Lists are used to store multiple items in a single variable. The items in a list can be of any data type.
# To create a list, the elements are placed inside square brackets "[]", seperated by commas. As shown below, lists can contain elements of different types as well as duplicated elements.
# List items are indexed, the first item has index O, the second item has index 1, etc.

# Accessing an item from a list:
numbers = [1, 2, 3, "Four", 5, 8]

print(numbers[2])

# If you add new items to a list, the new items will be placed at the end of list 
# List Appending:
cities = ["new york", "chicago", "los angeles"]

cities.append("houston")
print(cities)


# List deletion:
# The remove() method removes the specified item.
cities = ["new york", "chicago", "los angeles"]

cities.remove("chicago")
print(cities)