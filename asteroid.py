import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        movement_this_frame = self.velocity * dt
        self.position = self.position + movement_this_frame

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        neg_angle = -random_angle
        pos_vector = self.velocity.rotate(random_angle)
        neg_vector = self.velocity.rotate(neg_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(*self.position, new_radius)
        asteroid2 = Asteroid(*self.position, new_radius)
        asteroid1.velocity = pos_vector * 1.2
        asteroid2.velocity = neg_vector * 1.2
