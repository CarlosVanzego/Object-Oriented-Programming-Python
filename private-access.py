class MyClass:
    def __init__(self, value):
        self.__private_var = value

    def __private_method(self):
        print("Private method")


# this is a class I called 'PrivateBathroom'.
class PrivateBathroom:
    # this is the constructor method where I passed 'sink', 'toilet', 'shower', and 'mirror'.
    def __init__(self, sink="Kraus", toilet="Drake", shower="AXOR", mirror="Maestro"):
        self.__private_sink = sink
        self.__private_toilet = toilet
        self.__private_shower = shower
        self.__private_mirror = mirror

    def get_sink(self):
        return self.__private_sink
    
    def get_toilet(self):
        return self.__private_toilet
    
    def get_shower(self):
        return self.__private_shower
    
    def get_mirror(self):
        return self.__private_mirror
    


NiceBath = PrivateBathroom()
NiceBath.get_toilet()
print(f"This bathroom is much nicer.. it has a {NiceBath.get_toilet()} toilet..🚽")
