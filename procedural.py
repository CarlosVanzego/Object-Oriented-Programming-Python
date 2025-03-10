# Procedural programming in Python
# 
# this is a function I called 'calculate_area' to calculate the area of a rectangle. I am passing the parameters 'length' and 'width' to give a set length and width for the calculation.
def calculate_area(length=10, width=5):
  # this is a variable I declared called 'area' that multiplies the length by the width.
  area = (length * width)
  # then I am returning the area.
  return area

# Get input values 
# I am using the variable 'length_input' with an instance of the float class, then passing the input function and the "Enter length: " string that will show in the terminal to allow the user to input a length for calculation.
length_input = float(input("Enter length: "))
# I am setting the variable 'width_input' equal to the float class, then passing the input function and the "Enter width: " string that will show in the terminal to allow the user to input a width for calculation.
width_input = float(input("Enter width: "))

# Calculate and print the area 
# then I set the 'result' variable equal to the 'calculate_area' function and passing the 'length_input' and 'width_input' variables that I created before.
result = calculate_area(length_input, width_input)
# then I am printing "Rectangle_area: " and the result of the calculation of the length by the width.
print("Rectangle area: ", result)
