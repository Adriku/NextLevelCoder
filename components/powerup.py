import pygame
import random

from utils.constants import (RED, SCREEN_HEIGHT, SCREEN_WIDTH)
allowed_speed = list(range(3,7))
class powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(path.join(IMG_DIR "blue.png"))
        self.image ? pygame
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
