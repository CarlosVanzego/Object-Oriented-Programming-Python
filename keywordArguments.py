# Keyword Arguments:
# Keyword Arguments are arguments that can be passed with the key = value syntax. This way the order of the arguments does not matter. 
# Ex.
# 
def findYoungestKid(kid4, kid3, kid2, kid1):
  print("The youngest kid is " + kid4)

findYoungestKid(kid1 = "Carlos", kid2 = "Taylor", kid3 = "Robert", kid4 = "Nia")  



# Arbitrary Keyword Arguments:
# If the number of keyword arguments to be passed to a function is unknown, two asterisks (**) are placed before the parameter name in the functions definition. 
# This approach allows the function to receieve the arguments as a dictionary enabling access to each item by key.
# Ex.
# 
def printLastName(**kid):
  print("Her last name is " + kid["lname"])

printLastName(fname = "Nia", lname = "Hall") 

