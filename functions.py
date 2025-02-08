# Functions are predefined tasks created by the programmer to be used later in a program.
# They help in breaking down the program into smaller, more modular chunks, making the code more organized and reusable.
# For example, you can write a function to draw a square and then call this function whenever you need to draw a square, instead of writing the square-drawing code each time.
# Ex.

def draw_square():
    print("Drawing a square")

    draw_square()

def function_add(a, b):
    s = a + b
    return s  

print(function_add(2, 4)) 

def multiplication_function():
    t = 12 * 12
    return t
    
print(multiplication_function())
# This is a function called 'spell_name'. I have pass on the line beneath the function declaration to keep it syntactically correct.
def spell_name():
    pass
# this is a function I called 'made_up_function'.
def made_up_function():
    pass