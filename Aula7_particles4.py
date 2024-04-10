import pygame
import random

# Define Particle class
class Particle:
    def __init__(self, position):
        self.acceleration = pygame.Vector2(0, 0.05)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 0))
        self.position = position.copy()  # Use a copy of the position vector
        self.time_to_live = 255.0

        # Define color gradient (list of colors from start to end)
        self.color_gradient = [(50, 0, 0),(125, 0, 0), (200, 0, 0), (255, 0, 0)]  # Example gradient from white to red to blue

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.time_to_live -= 2

    def lerp_color(self, t):
        # Interpolate color based on remaining lifespan
        color_index = int(self.time_to_live / 255.0 * (len(self.color_gradient) - 1))
        color_start = self.color_gradient[color_index]
        color_end = self.color_gradient[min(color_index + 1, len(self.color_gradient) - 1)]

        """ Linearly interpolate between two RGB colors. """
        r = int(color_start[0] * (1 - t) + color_end[0] * t)
        g = int(color_start[1] * (1 - t) + color_end[1] * t)
        b = int(color_start[2] * (1 - t) + color_end[2] * t)
        return (r, g, b)

    def display(self, screen):
        if self.time_to_live < 0:
            self.time_to_live = 0
        
        # Interpolate RGB values based on remaining lifespan
        fade_factor = self.time_to_live / 255.0
        color=self.lerp_color(fade_factor)
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), 12)

    def is_dead(self):
        return self.time_to_live <= 0


# Define ParticleEmitter class
class ParticleEmitter:
    def __init__(self, position, emission_rate=0, interval=0):
        self.position = position
        self.emission_rate = emission_rate
        self.interval = interval
        self.particles = []
        self.last_emit_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_emit_time >= self.interval:
            # Time to emit new particles
            for _ in range(self.emission_rate):
                new_particle = Particle(self.position)
                self.particles.append(new_particle)
            self.last_emit_time = current_time

        # Update existing particles
        for particle in self.particles:
            particle.update()

        # Remove dead particles
        self.particles = [particle for particle in self.particles if not particle.is_dead()]

    def display(self, screen):
        for particle in self.particles:
            particle.display(screen)


def main():
    pygame.init()

    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, 32)
    pygame.display.set_caption("Particle Emitter Example")
    clock = pygame.time.Clock()

    # Create particle emitter
    emitter = ParticleEmitter(pygame.Vector2(width/2, 20), emission_rate=1, interval=1)

    # Main loop
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()


        # Update particle emitter (emit new particles, update existing particles)
        emitter.update()

        # Draw background
        screen.fill((0, 0, 0))

        # Display particles
        emitter.display(screen)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
