import pygame
import sys
import math
GRAVITY =1 
class Projectile:
    def __init__(self, x, y, v0, angle): 
        self.x = x
        self.y = y
        self.v0 = v0
        self.angle = angle
        self.delta_time = 0.01
        self.vx = 0
        self.vy = 0
        self.time = 0
        self.radius=5
        self.color=(0,0,0)
 
    def update(self):
        self.time += self.delta_time 
        #x=x0+Vxt
        #x=Vx×t  
        self.x += self.vx*self.delta_time

        #y=h+Vy*t−(g×t2)/2    no inicio h=y0 altura inicial
        #y=y0+v0yt-1/2gt2  
        self.y += self.vy*self.delta_time - (GRAVITY*self.delta_time**2)/2
        self.vy += GRAVITY*self.delta_time

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
    particle = Projectile(20, height // 2, 25, 85)

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
        particle.update()
        particle.draw(screen)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
