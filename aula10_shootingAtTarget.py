import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CANNON_X = 100
CANNON_Y = SCREEN_HEIGHT - 50
TARGET_RADIUS = 20
TARGET_X, TARGET_Y = 600, 550#350
GRAVITY = 9.8
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cannon Shooting at a Target")

# Function to calculate initial velocity
def calculate_initial_velocity(distance, height, angle):
    angle_rad = math.radians(angle)
    return math.sqrt((GRAVITY * distance**2) / (2 * (distance * math.tan(angle_rad) - height) * math.cos(angle_rad)**2))

# Game loop
running = True
clock = pygame.time.Clock()
projectiles = []

class Projectile:
    def __init__(self, x, y, v0, angle):
        self.x = x
        self.y = y
        self.v0 = v0
        self.angle = math.radians(angle)
        self.t = 0

    def update(self, dt):
        self.t += dt
        self.x = CANNON_X + self.v0 * math.cos(self.angle) * self.t
        self.y = CANNON_Y - (self.v0 * math.sin(self.angle) * self.t - 0.5 * GRAVITY * self.t**2)

    def draw(self):
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), 5)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                distance = TARGET_X - CANNON_X
                height = CANNON_Y - TARGET_Y
                angle = 45  # Angle of 45 degrees for simplicity
                v0 = calculate_initial_velocity(distance, height, angle)
                projectiles.append(Projectile(CANNON_X, CANNON_Y, v0, angle))

    screen.fill(WHITE)

    # Draw cannon
    pygame.draw.rect(screen, BLACK, (CANNON_X - 10, CANNON_Y, 20, 50))

    # Draw target
    pygame.draw.circle(screen, RED, (TARGET_X, TARGET_Y), TARGET_RADIUS)

    # Update and draw projectiles
    for projectile in projectiles:
        projectile.update(10/FPS)
        projectile.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
