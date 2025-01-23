import random
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        old_position = self.position
        old_velocity = self.velocity
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        split_one_angle = pygame.Vector2(old_velocity.x, old_velocity.y).rotate(random_angle)
        split_two_angle = pygame.Vector2(old_velocity.x, old_velocity.y).rotate(-random_angle)
        new_asteroid_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(old_position.x, old_position.y, new_asteroid_radius)
        asteroid_one.velocity = split_one_angle
        asteroid_two = Asteroid(old_position.x, old_position.y, new_asteroid_radius)
        asteroid_two.velocity = split_two_angle

