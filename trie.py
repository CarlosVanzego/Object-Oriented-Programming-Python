# Trie
# 
# A Trie, sometimes called a radix or prefix tree, is a specialized Tree used in searching, most often in text.
# In most cases, it outperforms Binary Search Tree, has Tables and most other Data Structures.
# Tries allows you to know if a word or a part of a word exists in a body of text.
# A Trie usually has an empty root node, which is the starting point.
# All the descendents of a node have a common prefix, or the String associated with that node.
# Trie is used for searching words in a dictionary, providing auto suggestion and IP routing.

# Time complexity: O(length of the word)
# Space complkexity: Because we use prefix such as N is used in different word, we don't have to store it multiple times. Because of the prefixes you save a lof of space.