# Python Dictionaires
# Dictionaires are used to store data in key:value pairs, unlike other data tpes (list, set, etc) where you usually hold only a songle value as an element.

# In Python a dictionary can be created with curly braces "{}", seperated by a comma.

# Few characterisitcs of Dictionaries:
# The items in a dictionary follow a proper order.
# A dictionary is not a sequence, so the order isnt officially preserved.

# Dictionary items are presented in key:value pars, as shown below:
# Ex.
# 
sampleDict = {
  "sport": "Basketball",
  "player": "Lebron James",
  "team": "LA Lakers"
  }

print(sampleDict["sport"])



sampleDict = {
  "sport": "Football",
  "player": "Cee Dee Lamb",
  "team": "Dallas Cowboys"
}

sampleDict["age"] = 25
print(sampleDict)