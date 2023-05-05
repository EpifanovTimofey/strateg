import pygame

rect_lov1 = None
rect_zamok = pygame.Rect([690, 260, 100, 160])
rect_doroga1 = pygame.Rect([0, 240, 800, 20])
rect_doroga2 = pygame.Rect([0, 420, 800, 20])
rect_vrag = pygame.Rect([20, 318, 75, 75])


def move_vrag():
    rect_vrag.left += 2


def lovushka1():
    global rect_lov1
    rect_lov1 = pygame.Rect([600, 260, 60, 160])


def lovushka2():
    global rect_lov1
    rect_lov1 = None
