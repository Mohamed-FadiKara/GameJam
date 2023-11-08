import pygame
import pytmx
import pyscroll

from Player import Player


class Game:
    def __init__(self):
        #creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("IUT2 Adventure")

        self.map = "world"

        tmx_data = pytmx.util_pygame.load_pygame('carte/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())

        #GENERER LE JOUEUR
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y)

        #dessin groupes calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_iut = tmx_data.get_object_by_name("enter_iut")
        self.enter_iut_rect = pygame.Rect(enter_iut.x, enter_iut.y, enter_iut.width, enter_iut.height)

        # collisions
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    def switch_house(self):

        self.map = "house"
        tmx_data = pytmx.util_pygame.load_pygame('carte/IUT.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # collisions
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessin groupes calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_iut = tmx_data.get_object_by_name("iut_exit")
        self.enter_iut_rect = pygame.Rect(enter_iut.x, enter_iut.y, enter_iut.width, enter_iut.height)

        # Intérieur
        spawn_iut_point = tmx_data.get_object_by_name("spawn_IUT")
        self.player.position[0] = spawn_iut_point.x
        self.player.position[1] = spawn_iut_point.y

    def switch_world(self):

        self.map = "world"
        tmx_data = pytmx.util_pygame.load_pygame('carte/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # collisions
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessin groupes calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_iut = tmx_data.get_object_by_name("enter_iut")
        self.enter_iut_rect = pygame.Rect(enter_iut.x, enter_iut.y, enter_iut.width, enter_iut.height)

        # Intérieur
        spawn_iut_point = tmx_data.get_object_by_name('enter_iut_exit')
        self.player.position[0] = spawn_iut_point.x
        self.player.position[1] = spawn_iut_point.y


    def update(self):
        self.group.update()
        # Vérifier l'entrer de la maison
        if self.map == "world" and self.player.feet.colliderect(self.enter_iut_rect):
            self.switch_house()
            self.map = 'house'

        if self.map == "house" and self.player.feet.colliderect(self.enter_iut_rect):
            self.switch_world()
            self.map = 'world'
        # Vérification des collisions
        for sprite in self.group.sprites():
                if sprite.feet.collidelist(self.walls) > -1:
                    sprite.move_back()

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
            self.player.save_location()
            self.imput()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()



