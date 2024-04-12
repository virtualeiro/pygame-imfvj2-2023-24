import pygame
import random

clock=pygame.time.Clock()

# Define Particle class
class Particle:
    def __init__(self, position):
        self.acceleration = pygame.Vector2(0, 0.05)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 0))
        self.position = position
        self.time_to_live = 255.0
        self.GRAVITY=9.8

    def run(self, screen):
        self.update()
        self.display(screen)

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.time_to_live -= 2

    def display(self, screen):
        if(self.time_to_live<0):
            self.time_to_live=0
 
        # Calculate fading color based on remaining lifespan
        # Decrease intensity of RGB components as time_to_live decreases
        fade_factor = self.time_to_live / 255.0  # Normalize time_to_live to range 0-1
        r = int(255 * fade_factor)  # Calculate red component
        g = int(255 * fade_factor)  # Calculate green component
        b = int(255 * fade_factor)  # Calculate blue component

        color = (r, g, b)
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), 12)

    def is_dead(self):
        return self.time_to_live == 0

def main():
    pygame.init()
   
    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, 32)

    pygame.display.set_caption("Particle Class Example")
    clock = pygame.time.Clock()

    # Create initial particle
    particle = Particle(pygame.Vector2(width/2, 20))

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        # Update particle
        particle.run(screen)

        # Check if particle is dead and respawn if necessary
        if particle.is_dead():
            particle = Particle(pygame.Vector2(width/2, 20))

        # Draw background
        screen.fill((0, 0, 0))
        
        # Draw particle
        particle.display(screen)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()