# The for loop is used to iterate through the members of a sequence (lists and strings) or any iterable object (dictionaries and sets).
# loops continue until we reach the last item in the sequence or object. The body of a for loop is seperated from the rest of the code using indentation.

# List:
# A list is a collection of items that are ordered and changeable. Lists are defined by having values between square brackets []. Lists are mutable, meaning that the values inside the list can be changed.
# Ex.
# 
# I created a list called "fruits" and stored the values "blueberry", "banana", "strawberry", and "Apple" inside it. 
fruits = ["blueberry", "banana", "strawberry", "Apple" ]
# I created a for loop that iterates through the "fruits" list and prints each value.
for x in fruits:
    # I am printing the value of x.
    print(x)

movies = ["The Matrix", "The Dark Knight", "Up", "Den of Thieves"]
for x in movies:
    print(x)   

games = ["Assassins Creed", "Call of Duty", "Halo", "Gears of War"] 
for x in games:
    print(x)    

wands = ["Elm", "Cherry", "Alder", "Chestnut"]  
for x in wands:
    print(x)
# This is a variable named 'sportingBrands' that I assigned a list of strings.
sportingBrands = ["Nike", "Adidas", "Under Armour", "Puma"]  
# Them I am using a for loop to iterate through the list.
for x in wands:
    # then I am printing the contents of the list. The output will be "["Nike", "Adidas", "Under Armour", "Puma"]"
    print(x)


drinks = ["Tea", "Coffee", "Water", "Milk"] 
for x in drinks:
    print(x)


pizzaToppings = ["pepperoni", "cheese", "mushroom"]    
for x in pizzaToppings:
    print(x)


# String:
# A string is a collection of characters. Strings are defined by having values between single or double quotes. Strings are immutable, meaning that the values inside the string cannot be changed.
# Ex.
# 
# I am using the "Apple" string from within the "fruits" list and iterating through it using a for loop.
for x in "Apple":
    # This will print each character in the string "Apple".
    print(x)

for x in "The Matrix":
    print(x)   

for x in "Halo":
    print(x)    

for x in "Elm":
    print(x)    

# this is a for loop to iterate through the characters within the "Puma" item in the 'sportingBrands' list.
for x in "Puma":
    # then I am printing out the characters. The output will be "P u m a".
    print(x)    

# Range Function:
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# Ex.
# 
# I am using the range function to iterate through the numbers 0-7.
for x in range(8):
    # I am printing the numbers 0-7 indicating the range function is working.
    print(x)   
 
# this is a for loop that i am using the range function in, to iterate through the numbers 0-2.
for x in range(3):
    # then I am printing the numbers 0-2.
    print(x)   
     



# Dictionaires:
# A dictionary is a collection of key-value pairs. Dictionaries are defined by having values between curly brackets {}. Dictionaries are mutable, meaning that the values inside the dictionary can be changed.
# Ex.
# 
# I created a dictionary called "c" and stored the key-value pairs "a": 1, "b": 2, "c": 3, and "d": 4 inside it.
c = {"a": 1, "b": 2, "c": 3, "d": 4}
# I created a for loop that iterates through the "c" dictionary. c.items() returns a list of tuples. Each tuple contains a key-value pair.
for key, value in c.items():
    # I am printing the key and value of the dictionary. 
    print(key, value)


v = {"a": 1, "b": 2}    
for key, value in v.items():
    print(key, value)


h = {"C": 4, "D": 8, "E": 12,}
for key, value in h.items():
    print(key,value)    



i = {"x":24, "y": 25, "z": 26}     
for key, value in i.items():
    print(key, value)


d = {"o":24, "p": 25, "p": 26}    
for key, value in d.items():
    print(key, value)