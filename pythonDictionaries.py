# Python Dictionaires
# 
# Dictionaires are used to store data in key:value pairs, unlike other data types (list, set, etc) where you usually hold only a single value as an element.

# In Python a dictionary can be created with curly braces "{}", seperated by a comma.

# Few characteristics of Dictionaries:
# The items in a dictionary follow a proper order.
# A dictionary is not a sequence, so the order isn't officially preserved.

# Dictionary items are presented in key:value pairs, as shown below:
# Ex.
# 
sampleDict = {
  "sport": "Football",
  "athlete": "Lamar Jackson",
  "team": "Baltimore Ravens"
  }

print(sampleDict["athlete"])



sampleDict = {
  "sport": "tennis",
  "player": "Serena Williams",
}

sampleDict["age"] = 43
print(sampleDict)


electionDict = {
  "party": "democrat",
  "candidate": "kamala harris🔵",
  "party2": "republican",
  "candidate2": "donald trump🔴"
}
print(electionDict)