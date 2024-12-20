import circleshape
from constants import *
import pygame
import shots

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen, color="white", line_width=2):
        points = self.triangle()
        pygame.draw.polygon(screen, color, points, line_width)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            s = shots.Shot(self.position[0], self.position[1])
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            s.velocity = forward*PLAYER_SHOOT_SPEED
            self.timer += PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer == 0
                
        if keys[pygame.K_a]:
            # print("A key pressed!")
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()