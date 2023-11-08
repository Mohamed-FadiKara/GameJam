import pygame
import pytmx
import pyscroll

from Player import Player


class Game:
    def __init__(self):
        #creer la fenetre du jeu
        self.screen = pygame.display.set_mode((1000,1000))
        pygame.display.set_caption("IUT2 Adventure")
        tmx_data = pytmx.util_pygame.load_pygame('carte/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())

        #GENERER LE JOUEUR
        self.player = Player(30,40)

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)
        self.group.add(self.player)

    def imput(self):
        bouton = pygame.key.get_pressed()
        if  bouton[pygame.K_UP]:
            self.player.move_haut()
            self.player.change_animation("haut")
        elif bouton[pygame.K_DOWN]:
            self.player.move_bas()
            self.player.change_animation("bas")
        elif bouton[pygame.K_LEFT]:
            self.player.move_gauche()
            self.player.change_animation("gauche")
        elif bouton[pygame.K_RIGHT]:
            self.player.move_droite()
            self.player.change_animation("droite")

    def run(self):

        clock = pygame.time.Clock()

        running = True

        while running:
            self.imput()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()

