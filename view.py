import pygame
import model
from pygame import display

dis = display.set_mode([800, 600])
zamok = pygame.image.load("zamok.png")
doroga = pygame.image.load("doroga.png")
vrag = pygame.image.load("vrag.png")


def view1():
    dis.fill([0, 0, 0])
    dis.blit(zamok, model.rect_zamok)
    dis.blit(doroga, model.rect_doroga1)
    dis.blit(doroga, model.rect_doroga2)
    dis.blit(vrag, model.rect_vrag)
    pygame.display.flip()
    if model.rect_vrag.left >= 620:
        exit()
