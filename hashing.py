# Hashing
# 
# Hashing is the process of converting a given key into another value.
# A hash function is used to generate a specific value according to a mathematical algorithm.
# A hash table stores key/value pairs in the form of a list where any element can be accessed using its index.
# If two keys map to the same index, a collision occurs.
# Hashing is also used in data encryption. Passwords can be stored in the form of their hashes so that even if a database is breached, plaintext passwords are not accessible.
# Some popular cryptographic hashes are MD5, SHA-1 and SHA-2.


# Collision Resolution
# Seperate Chaining: In seperate chaining, each bucket is independent, and contains a list of entries for each index. The time for hash map operations is the time to find the bucket (constant time), plus the time to iterate through the list.

# Open Addressing: In open addressing, when a new entry is inserted, the buckets are examined, starting with the hashed-to-slot and proceeding in some sequence, until an unoccupied slot is found. The name open addressing refers to the fact that the location of an item is not always determined by its hash value.
