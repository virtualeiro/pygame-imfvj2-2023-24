import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Horizontal Acceleration Simulation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball parameters
ball_radius = 20
ball_color = RED
ball_position = [10, HEIGHT // 2]  # Start at the center of the screen
ball_velocity = [0, 0]  # Initial velocity
horizontal_acceleration = 0.9  # Horizontal acceleration

# Main loop
clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate elapsed time
    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    # Update horizontal velocity and position
    ball_velocity[0] += horizontal_acceleration * dt
    ball_position[0] += ball_velocity[0] * dt

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Update the display
    pygame.display.flip()