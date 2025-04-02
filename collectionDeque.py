# Collection Deque
# 
# In Python, a Deque (Doubly Ended Queue) is implemented via the "collections" module. It is more advantageous than a list when swift append and pop operators are required at both ends of the container. This is because a deque ensures O(1) time complexity for these operations, whereas a list has an O(n) time complexity.
# Ex.
# 
from collections import deque

first_deque = deque([1, 2, 3, 4])
# Add 4 to the right end.
first_deque.append(5)
print(first_deque)

# Add 0 to the left end.
first_deque.appendleft(0)
print(first_deque)

# Remove and return the rightmost item.
first_deque.pop()
print(first_deque)

# Remove and return the leftmost item. 
first_deque.popleft()
print(first_deque)

# Add multiple elements at the right end.
first_deque.extend([6, 7, 8])
print(first_deque)

