# Sets
# 
# Sets are used to store multiple items in a single variable just like a list, but they cannot have duplicate values. To create a Set, elements are placed inside curly braces "{}".
# 
# A few characteristics of Sets:
# Sets do not have a proper order. The items in a set are arranged in a random order.
# The items in a Set do not have an index.
# Sets cannot have two items with the same value.
# Sets are used when you want to store a set of unique values and perform venn diagram like operations on it, for example union (method used to combine two or more sets, creating a new set that contains all the unique elements from all the sets involved), intersection (a set method that returns a new set containing elements common to two or more sets), etc.
# 
# Sets cannot have duplicates as illustrated below:
cities = {"new york", "chicago", "kansas", "chicago"}

print(cities)

# This is a variable I called otherCities where I stored a set of cities.
otherCities = {"houston", "fort lauderdale", "new orleans"}

print(len(otherCities))

# 
set1 = {"a", "B", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



fruits = {"apple", "banana", "strawberry", "Blueberry", "raspberry", "blackberry"}
companies = {"microsoft", "IBM", "NASA", "apple"}

common = fruits.intersection(companies)
print(common)