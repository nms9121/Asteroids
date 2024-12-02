# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player

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

    player.Player.containers = (updatable, drawable)

    p = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="Black")
        for t in updatable:
            t.update(dt)
        
        for o in drawable:
            o.draw(screen=screen)

        pygame.display.flip()

        

        dt = clock.tick(60)
        dt /= 1000

if __name__ == "__main__":
    main()