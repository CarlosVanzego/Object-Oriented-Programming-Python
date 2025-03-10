# the purpose of this file was to create a function to draw a square..


# I'm importing the "turtle" module into this file. This module allows me to draw shapes and create animations.
import turtle


# Then I'm creating a new window for the turtle to draw in using a variable I called "screen" and assigning it to the "Screen" method from the turtle" module.
screen = turtle.Screen()
# I'm setting the background color of the window to "black" by using the 'bgcolor', this stands for "background color" and is performed by python's "turtle" module; '.tracer' is a method that I am using to turn the turtle animation on.
screen.tracer(1)

# this is a turtle object that I am creating and assigning to the variable "t".
t = turtle.Turtle()
# I made a function called "draw_square" to draw a square in a new window.
def draw_square(size):
    # I'm using a for loop to draw the square.
    for _ in range(4):
        # I am using the forward method (fd) to move the turtle forward by the size of the square.
        t.forward(size)
        # I am using the right method (rt) to turn the turtle 90 degress to the right. 
        t.left(90)
        
# then I am calling the function "draw_square" and passing the argument "150" to the function because the square is 150 pixels.
draw_square(150) 


# I made a function called "move_forward" to move the turtle and draw a new shape; This function allows me to use the up arrow key on my keyboard to move the turtle forward.
def move_forward():
    # I am using the 'forward' method to move the turtle forward 25 pixels.
    turtle.forward(25)
# I made a function called "turn_left" to turn the turtle, this function allows me to use the left arrow key on my keyboard to turn the turtle left.
def turn_left():
    # I am using the 'left' method to turn the turtle 50 degrees to the left.
    turtle.left(50)
# I made a function called "turn-right" to turn the turtle, this function allows me to use the right arrow key on my keyboard to turn the turtle right.
def turn_right():
    # I am using the right method to turn the turtle 50 degrees to the right.
    turtle.right(50)
# I am using the listen method to listen for the keyboard input and move the turtle accordingly.
screen.listen()
# I am using the 'onkey' method to listen for the up arrow key on the keyboard and move the turtle forward.
screen.onkey(move_forward, "Up")       
# I am using the 'onkey' method to listen for the left arrow key on the keyboard and turn the turtle left.     
screen.onkey(turn_left, "Left")    
# I am using the 'onkey' method to listen for the right arrow key on the keyboard and turn the turtle right.        
screen.onkey(turn_right, "Right")            


# this is a method that I am using to keep the window open until I close it; The reason for this is so that I can see the turtle move and draw shapes as I press the arrow keys on my keyboard.
# I can close the window by clicking the "X" in the top right corner of the window or by pressing 'ctrl + c' in the terminal.
turtle.done()




 
# This creates an object "c" which is an instance of the "Turtle" class.
# c = turtle()
# for _ in range(4):
#     # I'm using the forward method to move the turtle forward 444 pixels
#     c.forward(44)
#     # then I an using the right method to turn the turtle 80 degrees to the right.
#     c.right(80)
# this is a method that I am using to keep the window open until I close it.
# turtle.done()   

