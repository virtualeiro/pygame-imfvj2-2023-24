import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball parameters
ball_radius = 20
ball_color = RED
ball_position = [WIDTH // 2, 0]  # Start at the top-center of the screen
ball_velocity = [0, 0]  # Initial velocity

# Constants
GRAVITY = 9.8  # Acceleration due to gravity

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

    # Update ball position and velocity
    ball_velocity[1] += GRAVITY * dt  # Update vertical velocity due to gravity
    ball_position[1] += ball_velocity[1] * dt + 0.5 * GRAVITY * dt**2  # Update vertical position

    # Bounce if the ball hits the ground
    if ball_position[1] >= HEIGHT - ball_radius:
        ball_position[1] = HEIGHT - ball_radius  # Move ball to ground level
        ball_velocity[1] *= -0.9  # Reverse and dampen velocity (loss of energy on bounce)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Update the display
    pygame.display.flip()