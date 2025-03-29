import pygame
import circleshape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT  # Import SCREEN_WIDTH and SCREEN_HEIGHT

class Shot(circleshape.CircleShape):
    # Initialize the shot class
    updatables = pygame.sprite.Group()  # Group for updating shots
    drawables = pygame.sprite.Group()   # Group for drawing shots
    
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
        # Add the shot to the update and draw groups
        Shot.updatables.add(self)
        Shot.drawables.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt  # Update shot's position based on velocity
        # Remove shot if it's off-screen
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH or self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            self.kill()  # Remove shot from the groups
