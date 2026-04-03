from circleshape import CircleShape
import pygame

from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        velocity_a = self.velocity.rotate(angle)
        velocity_b = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_a.velocity = velocity_a * 1.2

        asteroid_b = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_b.velocity = velocity_b * 1.2


