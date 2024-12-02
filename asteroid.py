import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return None
        else:
            a1 = random.uniform(20, 50)
            a2 = random.uniform(20, 50)
            v1 = self.velocity.rotate(a1)
            v2 = self.velocity.rotate(a2)

            A1 = Asteroid(self.position.x, self.position.y,self.radius-constants.ASTEROID_MIN_RADIUS)
            A2 = Asteroid(self.position.x, self.position.y,self.radius-constants.ASTEROID_MIN_RADIUS)

            A1.velocity = v1*1.2
            A2.velocity = v2*1.2