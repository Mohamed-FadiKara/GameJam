import pygame
pygame.init()

#création de la fenetre

pygame.display.set_mode((1920,1080))
pygame.display.set_caption("IUT2 Adventure")

running = True

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

pygame.quit()
