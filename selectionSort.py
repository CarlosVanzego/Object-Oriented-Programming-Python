# Selection Sort
# 
# The algorithm works by scanning a list of items for the smallest element and then swapping that element for the first position.
# Ex.
# 
def selectionSort(listToSort):
  # Traverse through  all array elements
  for i in range(len(listToSort)):

    # find the minimum element in remaining unsorted array
    for j in range(i+1, len(listToSort)):
      if listToSort[j] < listToSort[min]:
        min = j 

      # Swap the found minimum element with the first element
      listToSort[i], listToSort[min] = listToSort[min], listToSort[i]

    return listToSort



# Space complexity: O(1)
# 
# TIME COMPLEXITY
# Best Case - O(n^2) 
# Worst Case - O(n^2) 
# Average Case - O(n^2) 
