# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True: # This loop will run indefinitely
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")  # This paints the entire screen black for this frame
        pygame.display.flip()  # This updates the window with the new frame

if __name__ == "__main__":
    main()