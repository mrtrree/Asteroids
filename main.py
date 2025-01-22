import pygame
from constants import *

def main():
    pygame.init()
    __clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        __clock.tick(60)
        dt = __clock.tick(60) / 1000
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()