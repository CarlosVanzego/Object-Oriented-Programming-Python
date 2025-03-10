# I created a class called 'PublicClass'.

class PublicClass:
    # here I am initializing the constructor method (creating an object from the class) with the __init__ constructor.
    def __init__(self, value):
        # then I am instantiating the 'value' attribute, setting it equal to "public_var" a public variable; You know this is public because there is no (_) prefix in the variable name.
        self.public_var = value
    # then I am defining a public method called 'public_method'; You know this is a public method becuase there is no (_) prefix in the method name.
    def public_method(self):
        # then I am printing 'Public Method'
        print("Public Method")    
 

# Ex. 2
# I created a class called 'PublicBathroom'
class PublicBathroom:
    # then I instantiated (created and object from the 'PublicBathroom' class) the __init__ constructor.
    def __init__(self, sink="blanco", toilet="kohler"):
        # then I initialized the 'sink' value setting it equal to 'sink="blanco"'.
        self.sink = sink
        # and the 'toilet' value setting it equal to 'toilet="kohler"'.
        self.toilet = toilet
    # this is a public method I called 'get_sink'; you know this is public because there is no (_) prefix in the variable name.
    def get_sink(self):
        # then i'm returning sink.
        return self.sink
    # this is another public method I called 'get_toilet'; you know this is public because there is no (_) prefix in the variable name.
    def get_toilet(self):
        # then i'm returning toilet.
        return self.toilet
    
    
# I created another instance of the 'PublicBathroom' class called 'nastyBath'. 
nastyBath = PublicBathroom()
# then I'm printing a statement saying "This public bathroom has a blanco sink and a kohler toilet."
print(f"This public bathroom has a {nastyBath.get_sink()} sink, and a {nastyBath.get_toilet()} toilet🤢.")
