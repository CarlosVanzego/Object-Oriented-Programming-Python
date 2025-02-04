# The sort() methods sorts the eoements of a given list in either ascending or descending order. 
# By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
# reverse - If 'True', the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison.
# Ex.
# 
numbers = [4, 2, 1, 3]

numbers.sort()
print(numbers)


words = ["This", "is", "a", "list", "of", "words"]

words.sort()
print(words)


# To sort a list in descending order, a parameter reverse=True is passed as shown in the below example:
# 
numbers = [4, 2, 1, 3]

numbers.sort(reverse=True)
print(numbers)
