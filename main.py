import pygame
from clock import my_clock

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SB")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
my_clock()
pygame.quit()
#123

#abckdbckdf

#lvhsldh;s