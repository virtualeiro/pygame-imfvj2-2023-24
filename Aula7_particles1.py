import pygame
import sys

class Particle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display window
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Particle Class Example")

    # Define colors (RGB format)
    BLACK = (0, 0, 0)

    # Create a Particle object
    particle = Particle(width // 2, height // 2, 5, BLACK)

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background with white
        screen.fill((255, 255, 255))
        
        # Draw the particle
        particle.draw(screen)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
