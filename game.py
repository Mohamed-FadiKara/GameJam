import pygame
import pytmx
import pyscroll

from Player import Player


class Game:
    def __init__(self):
        #creer la fenetre du jeu
        self.screen = pygame.display.set_mode(((800,600)))
        pygame.display.set_caption("IUT2 Adventure")
        tmx_data = pytmx.util_pygame.load_pygame('carte/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())

        #GENERER LE JOUEUR
        self.player = Player()


        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def run(self):
        running = True

        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
