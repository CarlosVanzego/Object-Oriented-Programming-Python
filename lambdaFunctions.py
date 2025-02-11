# Lambda function
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression. The result of the expression is implicitly returned.
# We use lambda functions when we require a nameless function for a short period of time. Simply put, a lambda function is just like any normal Python function, except that it has no name when defining it, and it is contained in one line of code.
# You can use lambda functions when you have a very simple one line expression. This way you can make the code look much cleaner.
# Ex.
# Syntax -> lambda arguments : expression 
# The keyword lambda must come first. A full colon (:) seperates the argument and the expression.
# The expression is executed and the result is returned.
# In the example code below, c is the argument and c+4 is the expression:
sum = lambda c : c + 8

print(sum(8))
# this is a lambda function where I have the variable 'sum' and assigned it the lamda function in which v is the argument, and v-14 is the expression.
sum = lambda v : v - 14
# then I am printing the sum, where 'v' is equal to 20. The output will be 6 (28 - 14).
print(sum(28))



# In the example code below, a, b are the arguments and a * b is the expression.
multiply = lambda a, b : a * b

print(multiply(8, 4))

divide = lambda c, v : c / v

print(divide(144, 12))



# I created a variable named 'greet' and assigned it a lambda function that takes a single argument, 'name'.
# The lambda function returns the string "Hello" concatenanted with the provided 'name' argument.
greet = lambda name: "Hello " + name
# then I call the 'greet' function with the argument "Los" and print the returned value; the output will be "Hello Los"
print(greet("Carlos"))

# Example with a regular function.
# I defined a function called 'name' with no parameters.
def hiName():
  # Inside the function I created a variable 'name' and assigned it the string "Carlos"
  name = "Python"
  # I then print the string "Hello There. " concatenated with the name variable.
  print("Hello There. " + name)
# finally i'm calling the name function to execute it.
hiName()