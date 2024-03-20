import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Horizontal and Vertical Acceleration Simulation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball parameters
ball_radius = 20
ball_color = RED
ball_position = [WIDTH // 2, 0]  # Start at the top-center of the screen
ball_velocity = [0, 0]  # Initial velocity
ball_acceleration = [0.9, 0.5]  # Horizontal and vertical acceleration

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

    # Update horizontal velocity and position
    ball_velocity[0] += ball_acceleration[0] * dt
    ball_position[0] += ball_velocity[0] * dt

    # Update vertical velocity and position
    ball_velocity[1] += (GRAVITY + ball_acceleration[1]) * dt
    ball_position[1] += ball_velocity[1] * dt + 0.5 * (GRAVITY + ball_acceleration[1]) * dt**2

    # Bounce if the ball hits the ground
    if ball_position[1] >= HEIGHT - ball_radius:
        ball_position[1] = HEIGHT - ball_radius  # Move ball to ground level
        ball_velocity[1] *= -0.9  # Reverse and dampen velocity (loss of energy on bounce)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Update the display
    pygame.display.flip()