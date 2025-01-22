import pygame
from constants import *
from player import *

def main():

    pygame.init()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        for u in updateable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()