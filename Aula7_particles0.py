import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display window
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Circle")

# Define colors (RGB format)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit Pygame
            pygame.quit()
            sys.exit()
    
    # Fill the background with white
    screen.fill(WHITE)
    
    # Draw a circle
    radius = 5
    center = (width // 2, height // 2)
    pygame.draw.circle(screen, BLACK, center, radius)
    
    # Update the display
    pygame.display.flip()

