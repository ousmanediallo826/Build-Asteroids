
from constants import PLAYER_RADIUS
import pygame
import circleshape


class Asteroid(circleshape.CircleShape):
    # Static containers for updatables and drawables
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(velocity)

        # Add to the appropriate groups for updating and drawing
        Asteroid.updatables.add(self)
        Asteroid.drawables.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.x, self.y = self.position
