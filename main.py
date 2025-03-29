import pygame
from constants import * 
from player import Player
from asteroidfield import AsteroidField  # Ensure you have the correct import
from asteroid import Asteroid  # Import Asteroid
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt  = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 30)
    
    # Initialize AsteroidField
    asteroid_field = AsteroidField()
    
    # Initialize shots group
    shots = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update player and pass shots group to update method
        player.update(dt, shots)
        asteroid_field.update(dt)  # Ensure asteroids are updated from the field
        
        # Update shots
        shots.update(dt)
        
        # Check for collisions with asteroids and player
        for asteroid in asteroid_field.asteroids:  # Assuming AsteroidField manages asteroids
            if player.check_collision(asteroid):
                print("Game over!")
                running = False
                break 
        
        # Clear screen
        screen.fill((0, 0, 0))  # Clear screen before drawing

        # Draw all drawables (including player and asteroids)
        for drawable in Asteroid.drawables:
            drawable.draw(screen)
        
        # Draw shots
        for shot in shots:
            shot.draw(screen)
        
        # Draw player
        player.draw(screen)
        asteroid_field.draw(screen)  # Drawing asteroid field

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Update delta time

    pygame.quit()

if __name__ == "__main__":
    main()

