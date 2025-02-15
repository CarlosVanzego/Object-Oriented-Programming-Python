# B+ Trees
# 
# B+ tree is an extension of the B-tree, and the data here is stored in leaf nodes only. Due to this factor, searching in a B+ tree is faster and more efficient.

# Leaves are used to store data records
# Data keys are stored in the internal nodes of the tree.
# If a target key value is less than that of the internal node, the search follows the node just to its left.
# If a target key value is greater than or equal to that of the internal code, the search follows the node just to its right.
# The root has a minimum of two children.
# A comprehensive scan of all elements requires just one linear pass, as all leaf nodes in a B+ tree are linked.

# Search Operation
# To find the require record, you need to execute the binary search on the available records in the Tree. In case of an exact match with the search key, the corresponding record is returned to the user.

# In case the exact key is not located by the search in the parent, current, or leaf node, the a "not found message" is displayed to the user.

# The search process can be re-run for better and more accurate results.