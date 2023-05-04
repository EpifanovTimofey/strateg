import pygame
import model
from pygame import display

dis = display.set_mode([800, 600])
zamok = pygame.image.load("zamok.png")
dis.blit(zamok,model.rect)
pygame.display.flip()