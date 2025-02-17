# Merge Sort
# 
# Merge sort is also a divide and conquer algorithm.
# It uses recursion to keep dividing an array into two halves.
# At the end, it merges the two sorted halves.
# Any run of merge sort can be visualized as a tree. The leaves of the tree are the individual elements of the array. Each inner node of the tree cooresponds to merging two smaller arrays into one larger array.

# Divide phase
# Divide the unsorted list into two sublists of about half the size.

# Conquer phase
# Sort each of the two sublists recursively until we have list sizes of lenght 1, in which case the list items are returned.

# Combine phase 
# Join the two sorted sublists back into one sorted list. When the conquer step reaches the base step and we get two sorted subarrays, we combine the results by creating a sorted array from two sorted arrays.



# TIME COMPLEXITY
# Best Case = O(nlog(n))
# Worst Case = O(nlog(n))
# Average Case = O(nlog(n))