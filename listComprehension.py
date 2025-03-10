# List Comprehension
# 
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# You can use it to make your code look cleaner and more professional. It also enhances the readability for the programmer.
# 
# Syntax: 
# newlist = [expression for item in iterable if condition == True] 
# 
# Ex.
# 
players = ["LeBron", "Jordan", "Curry", "Bryant", "Harden"]

newPlayerlist = [x for x in players if "u" in x]
print(newPlayerlist)


whichPhone= ['iPhone', 'Samsung', 'sidekick']

myPhonelist = [x for x in whichPhone if "i" in x]
print(myPhonelist)


notThatPhone = [x for x in whichPhone if x != 'sidekick']
print(notThatPhone)
