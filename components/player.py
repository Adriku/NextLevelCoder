import pygame

from utils.constants import (
    GREEN,
    SCREEN_HEIGHT ,
    SCREEN_WIDTH
)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT -10

    def update(self):
        self.movement_on_x = 10
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.movement_on_x
        if key[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.movement_on_x


        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
