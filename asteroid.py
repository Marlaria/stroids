from constants import ASTEROID_MIN_RADIUS
import random
import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        ang = random.uniform(20, 50)
        aster = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        aster.velocity = self.velocity.rotate(ang) * 1.2
        aster = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        aster.velocity = self.velocity.rotate(-ang) * 1.2