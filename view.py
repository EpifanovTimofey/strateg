import pygame
import model
from pygame import display

a = None
l1 = "n"
l2 = "n"
dis = display.set_mode([800, 600])
zamok = pygame.image.load("zamok.png")
doroga = pygame.image.load("doroga.png")
vrag = pygame.image.load("vrag.png")
lovushka = pygame.image.load("lovushka.png")


def view1():
    global l1, l2, a
    dis.fill([0, 0, 0])
    if model.rect_vrag.left > 524:
        if l1 == "y":
            l2 = "y"
    if l2 == "n":
        a = dis.blit(vrag, model.rect_vrag)
    dis.blit(zamok, model.rect_zamok)
    dis.blit(doroga, model.rect_doroga1)
    dis.blit(doroga, model.rect_doroga2)

    if a != None and a.left >= 615:
        exit()
    if model.rect_lov1 != None:
        dis.blit(lovushka, model.rect_lov1)
        l1 = "y"
    if model.rect_lov1 == None:
        l1 = "n"
    pygame.display.flip()
