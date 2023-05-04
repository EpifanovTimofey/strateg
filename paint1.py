import pygame

zamok = pygame.Surface([50, 80])
pygame.draw.circle(zamok, [20, 100, 255], [25, 19], 9, 9)
pygame.draw.circle(zamok, [255, 255, 255], [25, 19], 9, 1)
pygame.draw.circle(zamok, [20, 100, 255], [25, 35], 15, 20)
pygame.draw.circle(zamok, [255, 255, 255], [25, 35], 15, 1)
pygame.draw.rect(zamok, [20, 100, 255], [5, 35, 40, 40])
pygame.draw.rect(zamok, [255, 255, 255], [5, 35, 40, 40], 1)
pygame.image.save(zamok, "zamok.png")
