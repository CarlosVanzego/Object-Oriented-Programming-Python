# Try Except Blocks
# 
# Try Except Blocks are used to catch exceptions in Python. The code is divided into two blocks: Try block and an Exception Block.

# The Try Block is used to test a block of code and if there's an error, the Exception block is used to handle it.
# Typically a try except block is used when you are unsure if an exception would come up. You are basically trying to ensure that a piece of code works, but that in the exception that it does not work, the except block handles the error peacefully and your program does not crash and moves on to the next block of code.

# It's good practice to use Try Except Blocks whenever you can.
# Ex.
# 
# The try block will generate an exception, because c is not defined, therefore the code execution moves onto the except block:
try:
  print()
except:
  # output: An exception occured
  print("An exception occured")  



# 'Else' Key word:
# Yuoo can use the else keyword tod efine a block of code to be executed if no errors were raised:
# 
try:
  print("Hello there.")
except:
  print("We have a problem..")
else:
  print("We are good to go.")     