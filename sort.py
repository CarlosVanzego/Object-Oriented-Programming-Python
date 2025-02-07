# The sort() method sorts the elements of a given list in either ascending or descending order. 
# By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
# reverse - If 'True', the sorted list is reversed (or sorted in Descending order).
# key - function that serves as a key for the sort comparison.
# Ex.
# 
numbers = [4, 2, 1, 3]

numbers.sort()
print(numbers)


vegetables = ["zucchini", "broccoli", "onion", "potato", "brussel", "carrot"]

vegetables.sort()
print(vegetables)


mandalorian = ["grogu", "darksaber", "force", "space", 'bounty hunter']

mandalorian.sort()
print(mandalorian)

games = ["Link", "Mario", "Zelda"]

games.sort()
print(games)


brands = ["gucci", "polo", "hermes"]

brands.sort()
print(brands)

# To sort a list in descending order, a parameter reverse=True is passed as shown in the below example:
# 
numbers = [4, 2, 1, 3]

numbers.sort(reverse=True)
print(numbers)

drinks = ["jameson", "tequila", "rum"]

drinks.sort(reverse=True)
print(drinks)