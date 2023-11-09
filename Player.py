import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self,nom,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'Joueur/{nom}.png')
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

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

        self.speed= 3
    def save_location(self): self.old_position = self.position.copy()

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
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def get_image(self, x,y):
        image = pygame.Surface([50,64])
        image.blit(self.sprite_sheet, (0,0),(x,y,44,64))
        return image


class Player(Entity):
    def __init__(self, x, y):
        super().__init__("sprite", x, y)
class NPC(Entity):
    def __init__(self, nom, x, y):
        super().__init__(nom, x, y)


