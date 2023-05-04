import pygame

zamok = pygame.Surface([100, 160])
pygame.draw.circle(zamok, [20, 100, 255], [50, 38], 18, 18)
pygame.draw.circle(zamok, [255, 255, 255], [50, 38], 18, 2)
pygame.draw.circle(zamok, [20, 100, 255], [50, 70], 30, 40)
pygame.draw.circle(zamok, [255, 255, 255], [50, 70], 30, 2)
pygame.draw.rect(zamok, [20, 100, 255], [10, 70, 80, 80])
pygame.draw.rect(zamok, [255, 255, 255], [10, 70, 80, 80], 2)
pygame.image.save(zamok, "zamok.png")

doroga = pygame.Surface([800, 20])
pygame.draw.rect(doroga, [109, 110, 100], [0, 0, 800, 20])
pygame.draw.rect(doroga, [255, 255, 255], [0, 0, 800, 20], 2)
pygame.image.save(doroga, "doroga.png")

vrag = pygame.Surface([75, 75])
pygame.draw.rect(vrag, [255, 15, 20], [0, 15, 75, 60])
pygame.draw.rect(vrag, [255, 15, 20], [27, 0, 23, 17])
pygame.draw.rect(vrag, [255, 255, 255], [0, 15, 75, 60], 2)
pygame.draw.rect(vrag, [255, 255, 255], [27, 0, 23, 17], 2)
pygame.image.save(vrag, "vrag.png")
