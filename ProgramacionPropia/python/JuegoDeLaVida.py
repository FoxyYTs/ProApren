import pygame
import numpy as np

pygame.init()
pygame.font.init()

width, height = 1000, 1000
CUAK = 20
screen = pygame.display.set_mode((height, width))

bg = 25,25,25

screen.fill(bg)

for i in range(50):
    for j in range(50):
        pygame.draw.rect(screen,(255,255,0),(i*CUAK,j*CUAK,CUAK,CUAK),1)
pygame.display.update()

def main():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            
        continue
    
main()