# Binary Search Functions
# 
# Bisect_left: bisect_left(a, x, lo=0, hi=len(a)):

# Purpose: Finds the index at which element x should be inserted in the list a to maintain the sorted order. If x is already present in a, the function returns the leftmost (or first) position where x can be inserted without changing the order.

# Parameters:
# a: the sorted list
# x: The element to be inserted
# lo (optional): The lower bound of the search. Defaults to 0.
# hi (optional): The upper bound of the search. Defaults to the length of a.

# Returns: The insertion point for x in a to maintain sorted order.

# Bisect_right:
# bisect_right(a, x, lo=0, hi=len(a)):

# Purpose: Similar to bisect_left, but returns the rightmost place in the list where x can be inserted without changing the order.
# Parameters: Same as bisect_left
# Returns: The insertion point for x in a to maintain sorted order.
# Ex.
# 
import bisect

a = [1, 2, 4, 4, 5]
index_left = bisect. bisect_left (a, 4)
index_right = bisect. bisect_right (a, 4)

# Key points:
# These functions assume that the list is already sorted. 
# The list is not modified; the functions only return the index at which the insertion should occur.
# The time complexity of these operations is O(log n), which is much more efficient than linear search operations for large lists.
