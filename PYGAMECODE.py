# First I am importing the pygame module.
import pygame 
import os 
print(os.path.abspath("Assets/spaceship_yellow.png"))

# Here I am setting the width and height for the surface of the game.
WIDTH, HEIGHT = 900, 500
# WIN is the window of the game.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# this line creates the caption that will appear at the top of the game window.
pygame.display.set_caption("Third Game!")
# I created the whitle variable and passed the RGB code for the color white; this is so I can pass the variable later in the code within the "fill" function, instead of using RGB code.
WHITE = (255, 255, 255)
# this line determines how many frames per second the game will update at.
FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))


def draw_window():
    # this line fills the screen with whatever color I pass in the fill function.
    WIN.fill(WHITE) 
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (300, 100))
    pygame.display.update()



def main():
  clock = pygame.time.Clock()
  run = True
  # this is the main game loop that will start the game and allow it to continuosly run until the game is over.
  while run:
    # this line ensures the game does not exceed the frames per second that I specified earlier in the code.
    clock.tick(FPS)
    # This line is giving me a list of all the events happening in the game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          # this line is checking if the game is still running.
           run = False

    draw_window()       
      
  # this line is quitting the game. 
  pygame.quit()
# this line ensures that when I run this file, it will only run the main function from this file and not from anywhere else. Making it so the game can only be ran from this file directly. "__name__" is the name of the file, and "__main__" is main file that is run.
if __name__ == "__main__":
   main()