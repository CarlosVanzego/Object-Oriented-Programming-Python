# Collections Counter
# 
# Collections.Counter is a subclass of the dictionary class in Python, provided by the collections module. It is designed for counting hashable objects and is a powerful tool for frequency analysis. Here's a brief review:

# Functionality:
# It counts the occurence of each element in an iterable (like lists, strings) and stores them as dictionary keys, with the counts as their corresponding value
# 
from collections import Counter

c = Counter('abracadabra')

# returns a list of the n most common elements and their counts.
print(c.most_common(3))
# output: [('a', 5),('b, 2'), ('r',2)]

# returns an iterator over elements, repeating each as many times as its count.
print(list(c.elements()))
# output: ['a', 'a', 'a', 'a' ,'a','b', 'b', 'r', 'r','c', 'd']

# subtracts count from the Counter
c.subtract('aab')
print(c)
# output: Counter({'a': 3, 'r': 2, 'b': 1, 'c': 1,'d': 1})]

# elements are counted and added to the Counter
c.update('aab')
print(c)
# output: Counter({'a': 5, 'r': 2, 'b': 2, 'c': 1,'d': 1})]



