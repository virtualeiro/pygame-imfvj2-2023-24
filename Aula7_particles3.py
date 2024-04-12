import pygame
import random

# Define Particle class
class Particle:
    def __init__(self, position):
        self.acceleration = pygame.Vector2(0, 0.05)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 0))
        self.position = position
        self.time_to_live = 255.0

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.time_to_live -= 2

    def display(self, screen):
        if self.time_to_live < 0:
            self.time_to_live = 0
        
        fade_factor = self.time_to_live / 255.0
        r = int(255 * fade_factor)
        g = int(255 * fade_factor)
        b = int(255 * fade_factor)

        color = (r, g, b)
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), 12)

    def is_dead(self):
        return self.time_to_live == 0


# Define ParticleEmitter class
class ParticleEmitter:
    def __init__(self, position, emission_rate=0, interval=0):  # Interval in milliseconds (3000 ms = 3 seconds)
        self.position = position
        self.emission_rate = emission_rate
        self.interval = interval
        self.particles = []
        self.last_emit_time = pygame.time.get_ticks()  # Get current time in milliseconds

    def update(self):
        current_time = pygame.time.get_ticks()  # Get current time in milliseconds
        if current_time - self.last_emit_time >= self.interval:
            # Time to emit new particles
            count=0
            for _ in range(self.emission_rate):
                new_particle = Particle(self.position.copy())
                self.particles.append(new_particle)
                print("Nova"+ str(count)+ str(self.position))
                count=count+1
            self.last_emit_time = current_time  # Update last emit time

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
    emitter = ParticleEmitter(pygame.Vector2(width/2, 20), emission_rate=10, interval=1000)  # Emit 10 particles every 5 seconds

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update particle emitter (emit new particles, update existing particles)
        emitter.update()

        # Draw background
        screen.fill((0, 0, 0))  # Fill screen with black background

        # Display particles
        emitter.display(screen)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
