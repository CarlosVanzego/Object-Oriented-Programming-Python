# AVL Tree
# The main idea with AVL trees is that you always know two things:
# The order invariant (if x<y then x is left of y)
# The height of the tree does not differ by more than one level, i.e. the tree is balanced.

# We can convert this from a BST to a height balanced AVL Tree. If we rearrange node "d" and its descendents, we can reformat the exact same BST into an AVL tree, which is balanced.