# Object Oriented Programming in Python (More practice)

# This is a Class called "Wolf"
class Wolf:
    # This method '__init__' allows me to instantiate (creating a new instance of a class, or object, from a class template) the Object right when it is created. This will be called whenever I call 'Wolf'. Inside this I am passing the Attributes 'self' (the actuall instance of the class), 'name' and 'age'.
    def __init__(self):
        # This line creates and Attribute of the Class 'Wolf' which is 'name'.
        self.name = 'Carlos'
        self.age = 28
    # This is a method called 'get_name' that I can use to get the name of the wolf.
    def get_name(self):
          return self.name
    
    def get_age(self):
         return self.age
    
    # this is a method called 'set_age' that I can use to set the age of the wolf. I can use methods to modify or change Attributes.
    # def set_age(self, age):
    #      self.age = age


# # This is a variable called "w" that I am assigning to an instance of the Class "Wolf"; This is me instantiating(creating a new instance) of the class Wolf; "w" then becomes an Object of type "Wolf".
w = Wolf()
print(f"My name is {w.get_name()} and I am {w.get_age()} years old")


wolves = Wolf()
wolves.name="los"
wolves.age=100

print(f"this is the new name {wolves.get_name()} and this is the new age {wolves.get_age()}")