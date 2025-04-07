import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()  #clock object helps control game's frame rate
    dt = 0 # delta time variable stores how much time passes between frames

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #instantiate a Player object
    asteroid_field = AsteroidField()

    while True: # This loop will run indefinitely
        for event in pygame.event.get(): # this allows the close window button to work
            if event.type == pygame.QUIT:
                return
        screen.fill("black")  # This paints the entire screen black for this frame
        for entity in drawable: # This creates the objects of the game
            entity.draw(screen) 
        updatable.update(dt)  #This updates the game with inputs (like moving and steering the ship)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
        pygame.display.flip()  # This updates the window with the new frame
        dt = clock.tick(60) / 1000 #sets the game loop to 60 frames per second

if __name__ == "__main__": #I'm not sure what this does...
    main()