import pygame
import numpy as np
from pygame.math import Vector2

def main():
    pygame.init()
    res_x = 640
    res_y = 480
    v_pos=Vector2(400, 300)
    screen = pygame.display.set_mode((res_x, res_y))
    # Game loop, runs forever
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos = Vector2(mouse_x, mouse_y)

        v_dir = mouse_pos - v_pos
        if(v_dir.magnitude() > 0):
            v_dir_normalized = v_dir.normalize() * 0.05
            v_pos += v_dir_normalized
        screen.fill((255,255,255))
        pygame.draw.circle(screen, (0, 0, 255), v_pos, 20)
        pygame.display.flip()
main()