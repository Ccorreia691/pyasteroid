from circleshape import *
from constants import *
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen , "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_asteroid_direction_1 = self.velocity.rotate(angle)
        new_asteroid_direction_2 = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ass1 = Asteroid(self.position.x, self.position.y, new_radius)
        ass2 = Asteroid(self.position.x, self.position.y, new_radius) 
        ass1.velocity = new_asteroid_direction_1 * 1.2
        ass2.velocity = new_asteroid_direction_2 * 1.2   