# Conditional Statements
# 
# Conditional statements in Python are used to perform different computations based on whether an expression/value evaluates to True or False.

# "if" key word:
# In this example, I use two variables, c and v, which are used as part of the if statements to test whether v is greater than c. As c is 400, and v is 8 we know that 400 is greater than 8, and so we print that "v is greater than c"

# "elif" keyword:
# the 'elif' keyword in python is used to execute a condition if the previous conditions weren't true. It's basically a way of saying that "if the previous conditions were not true, then try this condition."

# "else" key word:
# If the previous if and elif condition fails, then the else keyword is used.
# Ex.
# 
c = 8
v = 400

if v > c:
  print("v is greater than c")
elif c == v:
  print("c and v are equal")
else:
  print("c is greater than v")
