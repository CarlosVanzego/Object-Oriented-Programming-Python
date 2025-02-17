# Inheritence in OOP in Python


# To simplify this, I can remove the constuctor '__init__' method, and then I would need to make an upper level Class 'Pet':
# The 'Pet' Class contains the functinality that both the 'Cat' and 'Dog' Classes have.
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")    

# To allow the 'Cat' and 'Pet Classes to use the functionality of the 'Pet' Class, I can add 'Pet' as an Attribute to both; This makes both inherit the upper level Class 'Pet'.
class Cat(Pet):
    def __init__(self, name, age, color):
        # Super stands for reference the "Super Class" (the 'Pet' Class), or the class that is being inherited from here. "__init__" defines the method that I want to call, "name" and "age" are the arguments that I want to pass.
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")    


class Dog(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def speak(self):
        print("Bark")      

# this is an instance of the "Pet" class where I passed the strings "Carlos" and "28".
p = Pet("Carlos", 28)      
# then I am calling the show method 
p.show()
# this is an instance of the "Cat" class where I passed the strings "Charlie", "6" and "Grey".
c = Cat("Charlie", 6, "Grey")

# Even though there is no method called 'show' inside of 'Cat', this still prints because it inherits the properties from the 'Pet' Class because it is defined in the 'Cat' Class.
c.show()
d = Dog("Ace", 7)
d.show()