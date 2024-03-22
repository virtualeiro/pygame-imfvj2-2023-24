import pygame
import sys
import math

# Inicializacao
pygame.init()

# Constantes
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CHARACTER_RADIUS = 10
CHARACTER_COLOR = (255, 0, 0)
LINE_COLOR = (0, 255, 0)
GRAVITY = 9.8  # aceleracao gravitica (m/s^2)
LINE_START_X = 0
LINE_END_X = 300
LINE_Y = 30

# Screen Setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Character Movement")

# Character Setup
character_x = LINE_START_X
character_y = LINE_Y - CHARACTER_RADIUS
character_velocity_x = 0
character_velocity_y = 0
character_in_free_fall = False

# Time Setup
clock = pygame.time.Clock()
delta_time = 0

# Game Loop
while True:
    delta_time = clock.tick(60)  # Limita a frame rate a  60 FPS

    #Elementos estáticos da animação     
    screen.fill((255, 255, 255))#limpa o ecrã
    pygame.draw.line(screen, LINE_COLOR, (LINE_START_X, LINE_Y), (LINE_END_X, LINE_Y), 2)# Desenha plataforma
    
    # Processamento dos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Quando pressionamo na tecla right acelera
            if event.key == pygame.K_RIGHT:
                    character_velocity_x *=2

    # Animacao
    # delta_time em milisegundos. 
    timestep =  delta_time/100  #0.05 ideal
    acceleration=1
    
    if character_x <= LINE_END_X:
        character_velocity_x += acceleration * timestep  # Update posicao horizontal   
        character_velocity_y = 0 # Nao ha aceleracao vertical na plataforma 
    else: 
        character_velocity_x = 0  # Nao ha aceleracao vertical na queda livre
        character_velocity_y += GRAVITY * timestep 
    #Equacao abreviada da aceleracao constante      
    character_x += character_velocity_x * timestep    
    character_y += character_velocity_y * timestep    

    if character_y >= WINDOW_HEIGHT - CHARACTER_RADIUS:
            character_y = WINDOW_HEIGHT - CHARACTER_RADIUS
   
    # Personagem - Circulo
    pygame.draw.circle(screen, CHARACTER_COLOR, (round(character_x), round(character_y)), CHARACTER_RADIUS)

    pygame.display.flip()