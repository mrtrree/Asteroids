import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():

    pygame.init()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Asteroid.containers = (asteroid, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        for u in updateable:
            u.update(dt)

        for a in asteroid:
            if a.collision(player) == True:
                print("Game over!")
                exit()
                
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()