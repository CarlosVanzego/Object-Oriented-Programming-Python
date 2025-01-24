# Object Oriented Programming in Python

# This is a Class called "Wolf"
class Wolf:
    # This method '__init__' allows me to instantiate (creating a new instance of a class, or object, from a class template) the Object right when it is created. This will be called whenever I call 'Wolf'. Inside this I am passing the Attributes 'self' (the actuall instance of the class), 'name' and 'age'.
    def __init__(self, name, age):
        # This line creates and Attribute of the Class 'Wolf' which is 'name'.
        self.name = name
        self.age = age
    # This is a method called 'get_name' that I can use to get the name of the wolf.
    def get_name(self):
          return self.name
    
    def get_age(self):
         return self.age
    
    # tThis is a method called 'set_age' that I can use to set the age of the wolf. I can use methods to modify or change Attributes.
    def set_age(self, age):
         self.age = age

# # This is a variable called "w" that I am assigning to an instance of the Class "Wolf"; This is me instantiating(creating a new instance) of the class Wolf; "w" then becomes an Object of type "Wolf".
# w = Wolf()
# # This is me using a method on the instance of the Class 'howl'
# w.howl()   
# #prints <class '__main__.Wolf'>  
# print (type(w))

# w = Wolf("Carlos", 28)
# w.set_age(14)
# print(w.get_age())



# This is typically how Class' work. I name the Class (usually starts with uppercase and in CamelCase), then I define different methods and operations that can be performed by the Object.
# In OOP, once you create a Class, you can have an infinite number of instances of that Class without having to change anything.