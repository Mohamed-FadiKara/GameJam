import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('Joueur/sprit.png')
        self.image = self.get_image(1,1)
        self.rect = self.image.get_rect()
        self.image.set_colorkey([0,0,0])
        self.position = [x,y]


    def update(self):
        self.rect.topleft = self.position


    def get_image(self, x,y):
        image = pygame.Surface([32,64])
        image.blit(self.sprite_sheet, (0,0),(x,y,32,64))
        return image



