import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('Joueur/sprite.png')
        self.image = self.get_image(0,0)
        self.rect = self.image.get_rect()
        self.image.set_colorkey([0,0,0])
        self.position = [x,y]
        self.images = {
            "bas": self.get_image(0, 0),
            "droite": self.get_image(41, 0),
            "haut": self.get_image(90, 0),
            "gauche": self.get_image(134, 0)
        }
        #print("Player initialized")

        self.speed= 3
    def change_animation(self,name):
        self.image = self.images[name]
        self.image.set_colorkey((0,0,0))
    def move_droite(self):
        self.position[0] += self.speed
    def move_gauche(self):
        self.position[0] -= self.speed
    def move_haut(self):
        self.position[1] -= self.speed
    def move_bas(self):
        self.position[1] += self.speed
    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x,y):
        image = pygame.Surface([50,64])
        image.blit(self.sprite_sheet, (0,0),(x,y,44,64))
        print(" image du Player ")
        return image



