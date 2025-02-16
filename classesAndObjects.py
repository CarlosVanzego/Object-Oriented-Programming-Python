# Classes and Objects
# 
# Since Python is an object-oriented programming language, almost everything in Python is an object with its own set of attributes and methods. A Class is an object constructor or a blueprint for creating objects:
class sampleClass:
  name = "Carlos"

sampleObject = sampleClass()
print(sampleObject.name)  



# The __init__() function:
# In Python, when defining a class, an __init__() method (class constructor) can be included to initalize the objects attributes.

# For example, in a 'Student' class, attributes like "student_name", "roll_no", and "grade" can be initialized.

# The __init__() method is used to assign values to the objects properties or to perform any other necessary operations at the time of the objects creation.
# Ex.
# 
# I created a class called 'Student'.
class Student:
  # I defined the __init__() method, which is the constructor for the class.
  # It initializes new instances of the 'Student' class with the parameters 'name' and 'age'.
  def __init__(self, name, age):
    # I assigned the 'name' parameter to the instance variable 'self.name'.
    self.name = name
    # I assigned the 'age' parameter to the instance variable 'self.age'.
    self.age = age

# I created an instance of the 'Student' class and assigned it to the variable 'studentObject'.
# I passed the arguments "Carlos" (name) and 28 (age) to the constructor.
studentObject = Student("KingLos", 400)

# I then print the 'name' attribute of 'studentObject'.
print(studentObject.name)

# I also print the 'age' attribute of 'studentObject'.
print(studentObject.age)