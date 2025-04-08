import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw a circle with position (x, y), radius, and width 2
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill() #kill original asteroid
        if self.radius <= ASTEROID_MIN_RADIUS: #if small asteroid, no split necessary
            return
        random_angle = random.uniform(20, 50) #generate a random angle for splitting asteroid
        new_velocity1 = self.velocity.rotate(random_angle) # velocities of split asteroids
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS #radius for 2 split asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 1.2 #velocity increased by 20%
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 1.2 #velocity increased by 20%
