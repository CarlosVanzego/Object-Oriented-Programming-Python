# this is a class I called "Car".
class Car:
     # This is the constructor method with the argument "self", "make", "model", "color". I set them each to a default value.
     def __init__ (self, make="Volskwagen", model="Passat", color="White"):
        # then I am initializing the "make", "model" and "color" attributes.
        self.color = color
        self.make = make
        self.model = model

     def start(self):
        print(f"The {self.color} {self.make} {self.model} is starting.")

     def stop(self):
         print(f"The {self.color} {self.make} {self.model} is stopping.")  


my_car = Car("Volkswagen", "Passat", "White")    
my_car.start()
my_car.stop()

