import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, height = 800, 400
screen = pygame.display.set_mode((WIDTH, height))
pygame.display.set_caption("Square Motion with Drag Simulation - using velocity vector")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Square parameters
square_size = 40
square_x = square_size
square_y = height // 2
# Ball parameters
ball_radius = 20
ball_x = ball_radius
ball_y = height // 2
# Ball velocity
ball_speed = 5
ball_drag = False
# Air drag parameters
drag_coefficient = 0.1
air_density = 1.225
# Ball mass
ball_mass = 20




# Drag status
drag_active = False

# Air drag parameters
drag_coefficient = 0.1
air_density = 1.225

# Square mass
square_mass = 20

# Font
font = pygame.font.Font(None, 28)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
 # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_drag = True
    # Calculate the drag force
    drag_force = 0
    surface_area=ball_radius/4# Se fosse um quadrado seria uma aresta
    if ball_drag:
        velocity_squared = ball_speed ** 2
        drag_force = 0.5 * drag_coefficient * air_density * velocity_squared * surface_area
    
    # Calculate the acceleration based on drag force
    acceleration = -drag_force / ball_mass
    # Update ball velocity and position
    ball_speed += acceleration
    ball_x += ball_speed

    # Draw the scene
    screen.fill(BLACK)
    pygame.draw.circle(screen, (255,0,0), [ball_x, ball_y], ball_radius)
    if ball_drag:
        pygame.draw.line(screen, (0,0,255),[0, ball_y-40],[10, ball_y-50],5)
        pygame.draw.line(screen, (0,0,255), [WIDTH, ball_y-40],[0, ball_y-40],5)
        pygame.draw.line(screen, (0,0,255),[0, ball_y-40],[10, ball_y-30],5)

        pygame.draw.line(screen, (0,0,255), [ball_x+ball_radius, ball_y],[ball_x+ball_radius+5, ball_y-15],5)
        pygame.draw.line(screen, (0,0,255), [WIDTH, ball_y],[ball_x+ball_radius, ball_y],5)
        pygame.draw.line(screen, (0,0,255), [ball_x+ball_radius, ball_y],[ball_x+ball_radius+5, ball_y+15],5)
        
        pygame.draw.line(screen, (0,0,255),[0, ball_y+40],[10, ball_y+30],5)
        pygame.draw.line(screen, (0,0,255), [WIDTH, ball_y+40],[0, ball_y+40],5)
        pygame.draw.line(screen, (0,0,255),[0, ball_y+40],[10, ball_y+50],5)
        

            # Draw message
    message = "Drag Force activates when space key is pressed"
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, height // 2 + 50))
    screen.blit(text, text_rect)
    
    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
