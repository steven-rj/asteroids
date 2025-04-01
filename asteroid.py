import pygame, random
from circleshape import *
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vec1 = self.velocity.rotate(random_angle)
            new_vec2 = self.velocity.rotate(-random_angle)
            new_radii = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position.x, self.position.y, new_radii)
            new_ast1.velocity = new_vec1 * 1.2
            new_ast2 = Asteroid(self.position.x, self.position.y, new_radii)
            new_ast2.velocity = new_vec2