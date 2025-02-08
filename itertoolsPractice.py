# Itertools
# 
# Itertools.permutations(iterable, r=None):
# 
# Purpose: Generates all possible permutations of a given iterable. A permutation is a rearrangement of the elements of the iterable.
# Ex.
# 
import itertools

data = [1, 2, 3]

# This will print all 2-element permutations of the list [1, 2, 3]
for perm in itertools.permutations(data, 2):
  print(perm)

# Output: (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)


# itertools.combinations(iterable, r):
# Purpose: Generates all possible combinations of r elements from the given iterable. A combination is a selection of items from the iterable where the order does not matter.
# Ex.
# 
import itertools

data = [1, 2, 3]

# This will print all 2-element combinations of the list [1,2,3]
for combo in itertools.combinations(data, 2):
  print(combo)

# output: (1, 2), (1, 3), (2, 3),