# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player
import asteroid
import asteroidfield
import sys
import shots

def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    SCREEN_WIDTH = constants.SCREEN_WIDTH
    SCREEN_HEIGHT = constants.SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot_g = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    shots.Shot.containers = (shot_g, updatable, drawable)

    p = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    af = asteroidfield.AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="Black")
        
        for t in updatable:
            t.update(dt)
        
        for a in asteroids:
            if a.collision(p):
                print("Game Over!")
                sys.exit()
            for s in shot_g:
                if a.collision(s):
                    a.split()
                    s.kill()

        for o in drawable:
            o.draw(screen=screen)

        pygame.display.flip()

        dt = clock.tick(60)
        dt /= 1000

if __name__ == "__main__":
    main()