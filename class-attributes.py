# Class-Attributes are Attributes that are specific to the entire Class, not to an instance or an Object of that Class.

class Person:
  # This is a Class-Attribute and not a regular Attribute because it does not use 'self'. It is not defined in any method, and it does not  have access to an instance of the Class, it is defined for the entire Class; Which means it is not specific to any instance.
  number_of_people = 0

  def __init__(self, name):
      self.name = name

p1 = Person("Carlos")
p2 = Person("Nia")      

# Class-Attributes are useful for/when...