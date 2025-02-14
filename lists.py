# Lists 
# 
# Lists are used to store multiple items in a single variable. The items in a list can be of any data type.
# To create a list, the elements are placed inside square brackets "[]", seperated by commas. As shown below, lists can contain elements of different types as well as duplicated elements.
# List items are indexed, the first item has index O, the second item has index 1, etc.

# Accessing an item from a list:
numbers = [1, 2, 'three', 4, 5, 6, None, 8.0]
print(numbers[7])
# This is a list I called 'letters'. I assigned the list [a,b,c,d,e,f] to the variable letters.
letters = ['a', 'b', 'c', 'd', 'e', 'f']
# Then I'm printing the letter in index 5, so the output will be 'f'.
print(letters[5])

songs = ["Over", "FTCU", "TOO FAST", "Blow for Blow"]
print(songs[2])

# If you add new items to a list, the new items will be placed at the end of list 
# List Appending:
cities = ['new york', 'chicago', 'new orleans']

cities.append("san juan")
print(cities)

# List deletion:
# The remove() method removes the specified item.
cities = ["Maryland", "florida", "texas"]
cities.remove("Maryland")
print(cities)


listWithDifferentTypes = ['List', 4, "NO", 'REaSoN', 5.0]
listWithDifferentTypes.remove("NO")
print(listWithDifferentTypes)