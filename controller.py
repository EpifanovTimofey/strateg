import pygame, model

a = "n"
def p():
    global a
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.QUIT:
            exit()
        if f.type == pygame.KEYDOWN:
            if f.key == pygame.K_q:
                if a == "y":
                    a = "n"
                    model.lovushka2()
                    break
                if a == "n":
                    a = "y"
                    model.lovushka1()

