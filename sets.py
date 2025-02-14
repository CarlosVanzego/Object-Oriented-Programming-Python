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

cities = {"houston", "denver", "kansas", "denver"}
#  When printing the cities set, the 2nd "denver" does not show in the terminal. This is because sets cannot have duplicates.
print(cities)

states = {"Texas", "Maryland", "Louisiana", "California"} 
print(states)

cities2 = {"new york", "chicago", "kansas"}
# this prints the length of the cities2 set. Which is 3.
print(len(cities2))

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
# The union() method is used to combine two or more sets, creating new set that contains all the unique elements from all sets included.
set3 = set1.union(set2)
print(set3)

fruits = {"blackberry", "apple", "strawberry"}

companies = {"microsoft", "google", "apple"}

presidents = {"Obama", "Trump", "Clinton"}
print(presidents)

common = fruits.intersection(companies)
print(common)


aircrafts = {"airplane", "jets", "spaceship", "airplane", "helicopter"}
print(aircrafts)



