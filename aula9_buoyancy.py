import pygame
import random
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Buoyancy Simulation")

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Rectangle parameters
rectangle_width = 200
rectangle_height = 100
rectangle_x = width // 2 - rectangle_width // 2
rectangle_y = 0  # Starts at the top

# Initial position and velocity
position = Vector2(rectangle_x, rectangle_y)
velocity = Vector2(0, 0)

# Buoyancy parameters
water_level = height * 2 // 3  # Initial position of the water level
water_density = 4.5  # Density of water (higher value for denser water)
gravity = 9.8

# Mass of the red rectangle
rectangle_mass = 700  # Smaller mass

FPS=60
# Game loop
running = True
clock = pygame.time.Clock()
buoyant_force=0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if position.y + rectangle_height < water_level:  # Rectangle is in the free-fall phase
        # Calculate the net force
        net_force = Vector2(0, rectangle_mass * gravity)

        # Apply the net force to the rectangle's position
        acceleration = net_force / rectangle_mass
        position += acceleration

 
    else:  # Rectangle is in water => in the buoyancy phase 
            # Calculate the submerged depth
            submerged_depth = ((position.y + rectangle_height) - water_level)
            
            # Calculate the buoyant force
            #----submerged_volume=submerged_depth/rectangle_height 
            submerged_volume=submerged_depth*rectangle_width*0.01# Convert pixels^2 to m^2
            
            #Version 1
            buoyant_force = water_density *  submerged_volume * gravity     
         
            # Calculate the net force
            net_force = Vector2(0, rectangle_mass * gravity - buoyant_force)
            # Apply the net force to the rectangle's position
            acceleration = net_force / rectangle_mass
            velocity += acceleration/FPS

            # Limit the buoyant force so the rectangle floats correctly
            if position.y + rectangle_height > water_level + rectangle_height * 0.9:
                position.y = water_level + rectangle_height * 0.9 - rectangle_height
                velocity.y = 0  
    position+=velocity

    # Draw the scene
    screen.fill((0, 0, 0))  # Fill the screen with black color
    pygame.draw.rect(screen, RED, (position.x, position.y, rectangle_width, rectangle_height))
    pygame.draw.line(screen, BLUE, (0, water_level), (width, water_level), 3)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
