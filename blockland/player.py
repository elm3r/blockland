# Blockland Library Player Code
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("res/player.png")
        self.rect = self.image.get_rect()
        self.x = -64
        self.y = 128
        self.yVelocity = 0
        self.grav = -0.981
        self.maxYVelocity = 20
        self.movementSpeed = 5
        self.cameraOffset = self.calculateCameraOffset()
        super().__init__()

    def calculateCameraOffset(self):
        offset = [None, None]
        offset[0] = self.x + self.rect.x
        offset[1] = self.y + self.rect.y
        self.cameraOffset = offset
        return offset

    def tick(self, blockList):
        self.yVelocity += self.grav
        if(self.yVelocity < -self.maxYVelocity):
            self.yVelocity = -self.maxYVelocity

        for block in blockList.sprites():
            if(block.rect.collidepoint(self.rect.x, self.rect.y + 65) or block.rect.collidepoint(self.rect.x + 32, self.rect.y + 65)):
                if(self.yVelocity < 0):
                    self.yVelocity = 0

        self.move(blockList, [0, self.yVelocity])

    def move(self, blockList, offset):
        moveX = True
        moveY = True
        for block in blockList.sprites():
            if(offset[1] < 0):
                if(block.rect.collidepoint(self.rect.x, self.rect.y + 65) or block.rect.collidepoint(self.rect.x + 32, self.rect.y + 65)):
                    moveY = False

            if(offset[0] > 0):
                if(block.rect.collidepoint(self.rect.x - self.movementSpeed, self.rect.y + 63)):
                    if(block.rect.collidepoint(self.rect.x -1, self.rect.y + 63)):
                        self.x -= 1
                    moveX = False
            else:
                if(block.rect.collidepoint(self.rect.x + 32 + self.movementSpeed, self.rect.y + 63)):
                    if(block.rect.collidepoint(self.rect.x + 33, self.rect.y + 63)):
                        self.x += 1
                    moveX = False
        if(moveX):
            self.x += offset[0]

        if(moveY):
            self.y += offset[1]
