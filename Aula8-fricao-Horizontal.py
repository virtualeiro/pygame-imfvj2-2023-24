import pygame
import math
WIDTH=800
HEIGHT=600
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS=60
def main():
     # Ball parameters
    ball_radius = 20
    ball_x = ball_radius
    ball_y = HEIGHT // 2 
    ball_mass = 20 # Mass of the body in k
    floor_y = HEIGHT // 2 # Y-coordinate of the floor line
    force_applied=0
    force_increment=10
        # Gravitational force
    gravity = 9.8
    t=0.05
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RIGHT:
                    force_applied+=10
                elif event.key == pygame.K_LEFT:
                    force_applied-=10
        if(force_applied<0):
          force_applied=0 
       

        coefficient_of_kinetic_friction =0.02

        coefficient_of_static_friction=0.555
        normal_force = math.cos(math.pi/2)*ball_mass * gravity 

        static_friction = coefficient_of_static_friction * normal_force
        net_force = force_applied - static_friction
        if(net_force>0):
        #kinetic friction
            kinetic_friction = coefficient_of_kinetic_friction * normal_force
            net_force = force_applied - kinetic_friction

            acceleration = net_force / ball_mass
            velocity_x = acceleration * t
        else: velocity_x=0
        # Update ball position
        if ball_x < WIDTH - ball_radius:
            ball_x += velocity_x
        # Check if ball is below the floor
        if ball_y > floor_y - ball_radius:
           ball_y = floor_y - ball_radius
        
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,0,0), [ball_x-20,ball_y-50, 40,100], 3)
        pygame.draw.line(screen,(0,255,0), [ball_x,ball_y],  [ball_x-5,ball_y-5],3)
        pygame.draw.line(screen,(0,255,0), [ball_x,ball_y],  [ball_x-force_applied,ball_y],3)
        pygame.draw.line(screen,(0,255,0), [ball_x,ball_y],  [ball_x-5,ball_y+5],3)
        
        pygame.draw.line(screen, (0,0,255), [0,ball_y+50],[WIDTH,ball_y+50],  3)
        # Update the screen
        print("RightKey - aumenta força, LeftKey - diminui")   
        print("Net force", net_force, "Força aplicada", force_applied, coefficient_of_kinetic_friction, coefficient_of_static_friction )
        pygame.display.flip()

        # Wait for the next frame
        clock.tick(FPS)

    # Done
    pygame.quit()


main()
