import pygame
import random

# Constants
GRAVITY = 0.0001  # Acceleration due to gravity (adjust as needed)

# Define Particle class
class Particle:
    def __init__(self, position):
        self.position = position.copy()  # Use a copy of the position vector
        self.velocity = pygame.Vector2(random.uniform(-0.035, 0.035), random.uniform(-0.05, 0))
        self.time_to_live = 255.0

        # Define color gradient (list of colors from start to end)
        self.color_gradient = [(0, 0, 0), (255, 255, 255), (255, 125, 125), (255, 0, 0)]  # Example gradient

    def update(self, delta_time):
        self.position.x += self.velocity.x*delta_time
        # Update position using projectile motion equations under gravity
        self.position.y += self.velocity.y * delta_time #- (GRAVITY * delta_time**2) / 2
        self.velocity.y += GRAVITY * delta_time

        # Decrease time to live
        self.time_to_live -= 2 #* delta_time

    def display(self, screen):
        if self.time_to_live < 0:
            self.time_to_live = 0
        
        # Interpolate color based on remaining lifespan
        color_index = int(self.time_to_live / 255.0 * (len(self.color_gradient) - 1))
        color_start = self.color_gradient[color_index]
        color_end = self.color_gradient[min(color_index + 1, len(self.color_gradient) - 1)]

        # Interpolate RGB values based on remaining lifespan
        fade_factor = self.time_to_live / 255.0
        color=self.color_gradient[int(fade_factor*len(self.color_gradient))]
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

    def update(self, delta_time):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_emit_time >= self.interval:
            # Time to emit new particles
            for _ in range(self.emission_rate):
                new_particle = Particle(self.position)
                self.particles.append(new_particle)
            self.last_emit_time = current_time

        # Update existing particles
        for particle in self.particles:
            particle.update(delta_time)

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
    emitter = ParticleEmitter(pygame.Vector2(width/2, 120), emission_rate=5, interval=1)  # Emit 1 particle per second

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()


        # Calculate delta time (time elapsed since last frame, in seconds)
        delta_time = clock.tick(24)

        # Update particle emitter (emit new particles, update existing particles)
        emitter.update(delta_time)

        # Draw background
        screen.fill((0, 0, 0))

        # Display particles
        emitter.display(screen)

        # Update display
        pygame.display.flip()


if __name__ == "__main__":
    main()
