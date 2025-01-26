
class Car:
     
     def __init__ (self, make="Volkswagen", model="Passat", color="Blue"):
        self.color
        self.make
        self.model

     def start(self):
        print(f"The {self.color} {self.make} {self.model} is starting.")

     def stop(self):
         print(f"The {self.color} {self.make} {self.model} is stopping.")  


my_car = Car("BMW", "M4", "Blue" )    
my_car.start()
my_car.stop()

