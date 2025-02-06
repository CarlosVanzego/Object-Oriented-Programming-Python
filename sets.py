# Sets
# Sets are used to store multiple items in a siungle variable just like a list, but they cannot have duplicate values. To create a Set, elements are placed inside curly braces "{}".
# A few characteristics of Sets:
# Sets do not have a proper order. The items in a set are arranged in a random order.
# The items in a Set do not have an index.
# Sets cannot have two items with the same value.
# Sets are used when you want to store a set of unique values and perform venn diagram like operations on it for example union, intersection etc.
# 
# Sets cannot have duplicates as illustrated below:

cities = {"new york", "chicago", "kansas", "chicago"}
#  When printing the cities set, the 2nd "chicago" does not show in the terminal. This is because sets cannot have duplicates.
print(cities)

states = {"Texas", "Maryland", "Louisiana", "California"} 
print(states)

cities = {"new york", "chicago", "kansas"}
# this prints the length of the cities set. Which is 3.
print(len(cities))

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# The union() method is used to combine two or more sets, creating new set that contains all the unique elements from all sets included.
set3 = set1.union(set2)
print(set3)

fruits = {"blackberry", "apple", "strawberry"}
companies = {"microsoft", "google", "apple"}

common = fruits.intersection(companies)
print(common)




