# B - Trees
# 
# B-tree nodes have more than two children.
# A B-tree node may contain more than just a single element.
# 
# Rule 1: The root can have as few as one element (or even no elements if it also has no children); every other node has at least the MINIMUM number of elements. 
# Rule 2: The maximum number of elements in a node is twice the value of the MINIMUM.
# Rule 3: The elements of each B-tree node are stored in a partially filled array, sorted from the smallest element (at index 0) to the largest element (at the final used position of the array)
# Rule 4: The number of subtrees below a non-leaf node is always one more than the number of elements in the node. Subtree 0, subtree 1, ...
# Rule 5: For any non-leaf node:
  # An element at index i is greater than all the elements in the subtree number i of the node, and
  # An element at i is less than all the elemetns in the subtree number i + 1 of the node.
# Rule 6: Every leaf in a B-tree has the same depth, ensuring the tree remains balanced.