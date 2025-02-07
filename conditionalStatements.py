# Conditional Statements
# Conditional statementsin Python are sued to perform different computations based on whether an expression/value evaluates to True or False.

# if key word:
# In this example, we use etwo variables, a and b, which are used as part of the if statements to test whether b is greater than a. As a is 400, and b is 14 we know that 400 is greater than 14, and so we print that "a is grreater than b"

# elif keyword:

# the elif keyword in python is used to execute a condition if the previous conditions weren't true. It's basically a way of saying that "if the previous conditions were not true, then try this condition."

# else key word:
# If the previous if and elif condition fails, then the else keyword is used.
# Ex.
# 
c = 400
v = 14

if v > c:
  print("v is greater than c")
elif c == v:
  print("c and v are equal")
else:
  print("c is greater than v")
    