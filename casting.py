# Casting
# 
# If you want to specify the data type of a variable, this can be done with casting.
# You can overwrite the default data type with the data type of your choice. However, attempting to convert incompatible values, such as converting the string 'Messi' into an integer, will result in an error.
# 
# I'm converting the integer 44 into a string.
x = str(44)
# Then I am printing the type of 'x', which will now be <class 'str'>.
print(type(x))
# I'm converting the integer 3 explicitly into an integer (redundant but shows casting).
y = int(3)
# Then i'm printing the type of 'y', which remains <class 'int'>.
print(type(y))
# I'm converting the integer 3 into a floating-point number.
z = float(3)
# Print the type of 'z', which should now be <class 'float'>.
print(type(z))




# Invalid Type Conversion (Will cause an Error)
# Attempting to convert a non-numericstring into an integer will raise a ValueError
try:
  # This will cause an error 
  invalid_conversion = int("Messi") 
# Thi line uses the ValueError class to define the error and assign the error message to the variable 'e'.
except ValueError as e:
  # This wiill catch and print the error message.
  print(f"Error: {e}")  