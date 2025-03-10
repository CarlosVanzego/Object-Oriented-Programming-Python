# this is a class I called "Car".
class Car:
     # This is the constructor method with the argument "self", "make", "model", "color". I set them each to a default value.
     def __init__ (self, make="Audi", model="A4", color="Blue"):
        # then I am initializing the "make", "model" and "color" attributes.
        self.color = color
        self.make = make
        self.model = model

     def start(self):
        print(f"The {self.color} {self.make} {self.model} is starting.")

     def stop(self):
         print(f"The {self.color} {self.make} {self.model} is stopping.")  


# my_car = Car("BMW", "M4", "Blue")    
# my_car.start()
# my_car.stop()

