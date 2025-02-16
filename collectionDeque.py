# Collection Deque
# 
# In Python, a Deque (Doubly Ended Queue) is implemented via the "collections" module. It is more advantageous than a list when swift append and pop operators are required at both ends of the container. This is because a deque ensures O(1) time complexity for these operations, whereas a list has an O(n) time complexity.
# Ex.
# 
from collections import deque

d = deque([1, 2, 3])
# Add 4 to the right end.
d.append(4)
print(d)

# Add 0 to the left end.
d.appendleft(0)
print(d)

# Remove and return the rightmost item.
d.pop()
print(d)

# Remove and return the leftmost item. 
d.popleft()
print(d)

# Add multiple elements at the right end.
d.extend([5, 6, 7])
print(d)
