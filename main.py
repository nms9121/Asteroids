# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    SCREEN_WIDTH = constants.SCREEN_WIDTH
    SCREEN_HEIGHT = constants.SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="Black")
        pygame.display.flip()

if __name__ == "__main__":
    main()