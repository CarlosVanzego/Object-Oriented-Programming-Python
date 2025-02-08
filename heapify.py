# Heapify
# 
# Heapify is the process of creating a heap data structure from a binary tree. It is used to create a Min-Heap or a Max-Heap.

# To create a Heapify:
# The index of left child is given by 2i + 1 and the right child is given by 2i + 2
# If leftChild is greater than currentElement, set leftChildInde3x as largest.
# If rightChild is greater than element in largest, set rightChildIndex as largest.
# Swap the element at the largest index with the currentElement.
# Repeat the process until the subtrees are heapified
# 

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ",(list(li)))

# output: The created heap is : [1, 3, 9, 7, 5]