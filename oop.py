# Object Oriented Programming in Python

# This is a Class I called "Wolf"
class Wolf:
    # This constructor '__init__' allows me to initialize (creating a new instance of a class, or object, from a class template) the Object right when it is created. This will be called whenever I call 'Wolf'. Inside this I am passing the Attributes 'self' (the actual instance of the class), 'name' and 'age'.
    def __init__(self, name="Carlos", age=28):
        # This line creates an Attribute of the Class 'Wolf' which is 'name'.
        self.name = name
        self.age = age
    # This is a method called 'get_name' that I can use to get the name of the wolf.
    def get_name(self):
          return self.name
    
    def get_age(self):
         return self.age
    
    # This is a method called 'set_age' that I can use to set the age of the wolf. I can use methods to modify or change Attributes.
    def set_age(self, age):
         self.age = age


# This is a variable called "w" that I am assigning to an instance of the Class "Wolf"; This is me instantiating (creating a new instance) of the class Wolf; "w" then becomes an Object of type "Wolf".
w = Wolf()
print(w.get_name())

w2 = Wolf("anything", 2)
print(f"new name {w2.get_name()} and new age {w2.get_age()}")

# # This is me using a method on the instance of the Class 'howl'
# w.howl()   
# #prints <class '__main__.Wolf'>  
# print (type(w))

# w = Wolf("Carlos", 28)
# w.set_age(14)
# print(w.get_age())



# This is typically how Class' work. I name the Class (usually starts with uppercase and in CamelCase), then I define different methods and operations that can be performed by the Object.
# In OOP, once you create a Class, you can have an infinite number of instances of that Class without having to change anything.


# this is a class I called controller
class Controller:
    #  this is the constructor method with the arguments "self", "triggers", "analogs", "touchpad", and "buttons" which I set equal to "8"
     def __init__(self, triggers, analogs, touchpad, buttons="8"):
          # this pass does nothing, it ensures the function does not break by remaining syntatically correct.   
          pass
    #  this is a method called button with the arguments "self", "triangle", "circle", "x", and "square".
     def press_button(self, triangle, circle,x, square):
            # This line creates and Attribute of the Class 'Controller' which is 'triangle'.
            self.triangle = triangle 
            # This line creates and Attribute of the Class 'Controller' which is 'circle'.
            self.circle = circle
            # This line creates and Attribute of the Class 'Controller' which is 'x'.
            self.x = x
            # This line creates and Attribute of the Class 'Controller' which is 'square'.
            self.square = square


