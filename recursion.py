# Recursion
# 
# Recursion can be remembered with the help of Matryoshka dolls -- a set of wooden dolls of decreasing size placed one inside another.

# When you open a doll, you find another doll inside, and when you open that one, there's another one inside. The act of doing this is called recursion.

# Recursion should always have a base case.

# A recursive call must reach a base case to prevent the program from running indefinitely. 
# Ex.
# 
def openDoll(doll):

    if doll.isEmpty:
        return doll
    
    else:
        openDoll(doll)