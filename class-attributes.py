# Class-Attributes are Attributes that are specific to the entire Class, not to an instance or an Object of that Class.

# This is a class called "Person"
class Person:
  # This is a Class-Attribute of the class "Person" and not a regular Attribute because it does not use 'self'. It is not defined in any method, and it does not  have access to an instance of the Class, it is defined for the entire Class; Which means it is not specific to any instance.
  # Class attribute shared among all instances of the class.
  number_of_people = 0
  # this line initializes the function with the arguments self and name; the contstructor method that initializes an instance with a name attribute.
  def __init__(self, name):
      self.name = name
# This is a variable I called p1 and assigned an instance of the Person class with the string "Harold", I created a new instance of the Person Class with the name Harold.
p1 = Person("Harold")
# here I am printing the variable p1.
print(p1)
# This is a variable I called p2 and assigned another instance of the Person class with the string "Tina"
# I created a new instance of the Person Class with the name Tina.
p2 = Person("Tina")
# here I am printing the variable p2.
print(p2)


# Class-Attributes are useful for/when...