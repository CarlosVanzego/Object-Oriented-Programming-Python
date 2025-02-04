# In Python, information ccan be passed into functions as arguments.
# Arguments are specified after the functions name, inside the parenthesis. You can add multiple arguments by seperating them with a comma.
# Ex.
# 
# this is a function I called 'printStatement' that takes two arguments 'personName' and 'sport'.
def printStatement(personName, sport):
  # I am printing the values of the arguments passed into the function, and using string concatenation to make the output more readable.
  print(personName + " plays " + sport)
# I am calling the function 'printStatement' and passing in the arguments "Lebron James" and "Basketball".
printStatement("Lebron James", "Basketball")



# Arbitrary Arguments (*args)
# If you do not know how many arguments that will be passed into the function, an asterisk (*) can be placed before the parameter name in the function's definition. This feature allows Python to accomodate function calls with any variable number of arguments.
# The function will then recieve the arguments as a tuple, enabling it to access each item individually.
# Ex.
# 
# I created a function called 'findYoungestKid' and passed in the parameter '*kids'. This allows the function to take in any number of arguments that I choose.
def findYoungestKid(*kids):
  # I am printing the youngest kid by accessing the last element in the tuple.
  print("The youngest kid is " + kids[3])
# Then I am calling the function 'findYoungestKid' and passing in the arguments "Carlos", "Taylor", "Robert", and "Nia".
findYoungestKid("Carlos", "Taylor", "Robert", "Nia")

