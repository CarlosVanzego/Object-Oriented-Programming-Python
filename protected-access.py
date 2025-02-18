class ProtectedClass:
    def __init__(self, value):
        # this is a protected variable, you know this because it has an underscore (_) prefix before the variable name.
        self._protected_var = value 

    def _protected_method(self):
        print("This is a protected method")    

# class SubClass(MyClass):
#     def access_protected(self): 
#         print(self._protected_var)
#         self._protected_method()   
        