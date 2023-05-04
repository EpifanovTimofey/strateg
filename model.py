import pygame

rect_zamok = pygame.Rect([690, 260, 100, 160])
rect_doroga1 = pygame.Rect([0, 240, 800, 20])
rect_doroga2 = pygame.Rect([0, 420, 800, 20])
rect_vrag = pygame.Rect([20, 318, 75, 75])
def move_vrag():
    rect_vrag.left += 2