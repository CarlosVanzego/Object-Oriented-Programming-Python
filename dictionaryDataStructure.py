# Dictionary (Data Structure)
# 
# A Dictionary is a data structure that can map keys to values. It uses a hash function to compute am index into an array of buckets or slots, from which the desired value can be found.
# Key - a unique identifier used to associate each element (value) in a map.
# Value - elements associated by keys in a map.
# Ex.
# 

# creating a dictionary
hashMap = {}

# Setting a key-value pair
hashMap['key1'] = 'value1'

# Getting the size of the dictionary
size = len(hashMap)

# Accessing a value with a key
# Replace <key> with the actual key, e.g. 'key1'
value = hashMap.get('<key>')

# Checking if a key exists in the dictionary
# Replace <key> with the actual key, e.g. 'key1'
has_key = '<key>' in hashMap

# Deleting a key-value pair
# Replace <key> with the actual key, e.g. 'key1'
hashMap.pop('<key>', None)
# The None is to avoid KeyError if the key does not exist.

# Clearing the dictionary
hashMap.clear()

# TIME COMPLEXITY
# Insertion - Average case O(1), Worst case O(n)
# Deletion - Average case O(1), Worst case O(n)
# Search - Average case O(1), Worst case O(n)
# Space - O(n)