# Blockland Library Player Code
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("res/player.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.movementSpeed = 5
        self.cameraOffset = self.calculateCameraOffset()
        super().__init__()

    def calculateCameraOffset(self):
        offset = [None, None]
        offset[0] = self.x + self.rect.x
        offset[1] = self.y + self.rect.y
        self.cameraOffset = offset
        return offset
