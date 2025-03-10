# Quick Sort
# 
# Quick Sort uses a pivoting technique to break the main list into a smaller list and the smaller list uses the pivoting technique unless they are sorted.

# How quicksort works
# Quick sort follows the Divide and Conquer approach.
# Choose a pivot.
# Place all numbers less than the pivot to the left.
# The left and the right subparts are again paritioned by selectiung pivot elements for them.
# A pivot element is chosen from the array. You can choose any element from the array as the pivot element.
# The elements smaller than the pivot are put on the left and the elements greater than the pivot element are put on the right.
# It uses recursion for the implementation.



# Space completxity: O(log n)

# TIME COMPLEXITY
# Best case - O(nlog(n))
# Worst case - O(n^2))
# Average case - O(nlog(n))