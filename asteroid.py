from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

        pygame.draw.circle(screen, (255,0,0), self.position, self.radius, width=1)

    def update(self, dt):
        self.position += self.velocity * dt
