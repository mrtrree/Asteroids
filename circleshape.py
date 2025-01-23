import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, p_object):
        return self.position.distance_to(p_object.position) < self.radius + p_object.radius

    # def collision(self, p_object):
    #     distance = self.position.distance_to(p_object.position)
    #     radii_sum = self.radius + p_object.radius
    #     print(f"Distance: {distance}, Radii sum: {radii_sum}")
    #     return distance <= radii_sum