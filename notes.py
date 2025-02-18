def hello():
# will print "<class 'function'>" 
    print(type("hello"))

# Type
x = 1
# will print the type 'str'
print(type("hello")) 
# In the terminal this prints "<class 'str'>", what this means is that the string "hello" is actually an Object of the Class String.

# Ex.
x = 1
# will print the type 'int'
print(type(x))
# In the terminal this prints "<class 'str'>", this is due to the same reasoning.


# What this all means is that everything in Python is an Object of some type of Class; Whenever you create something in Python, you are really creating an Object, which is an instance of a specific Class; That Class defines the way the Object can interact with other things in the program.
# These are called "built-in" types these are built into the python language; They work differently than normal classes.


# Methods - A function that goes inside of a class; Can be performed on Objects.
string = "hello"
# Here the method 'upper' acting on the Object of type Str that is stored in the "string" variable.
print(string.upper())
