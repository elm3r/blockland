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
            if(block.rect.collidepoint(self.rect.x, self.rect.y + 66) or block.rect.collidepoint(self.rect.x + 32, self.rect.y + 66)):
                if(self.yVelocity < 0):
                    self.yVelocity = 0

        self.move(blockList, [0, self.yVelocity])

    def move(self, blockList, offset):
        moveX = True
        moveY = True
        for block in blockList.sprites():
            if(offset[1] < 0):
                if(block.rect.collidepoint(self.rect.x, self.rect.y + 64 - offset[1]) or block.rect.collidepoint(self.rect.x + 32, self.rect.y + 64 - offset[1])):
                    if not(block.rect.collidepoint(self.rect.x, self.rect.y + 66) or block.rect.collidepoint(self.rect.x + 32, self.rect.y + 66)):
                        self.y -= 1
                    moveY = False

            if(offset[0] > 0):
                if(block.rect.collidepoint(self.rect.x - offset[0], self.rect.y + 64)):
                    if(not block.rect.collidepoint(self.rect.x - 2, self.rect.y + 64)):
                        self.x -= 1
                    moveX = False
                elif(block.rect.collidepoint(self.rect.x - offset[0], self.rect.y + 32)):
                    if(not block.rect.collidepoint(self.rect.x - 2, self.rect.y + 32)):
                        self.x -= 1
                    moveX = False
                elif(block.rect.collidepoint(self.rect.x - offset[0], self.rect.y)):
                    if(not block.rect.collidepoint(self.rect.x - 2, self.rect.y)):
                        self.x -= 1
                    moveX = False
            else:
                if(block.rect.collidepoint(self.rect.x + 32 + -offset[0], self.rect.y + 64)):
                    if(not block.rect.collidepoint(self.rect.x + 34, self.rect.y + 64)):
                        self.x += 1
                    moveX = False
                elif(block.rect.collidepoint(self.rect.x + 32 + -offset[0], self.rect.y + 32)):
                    if(not block.rect.collidepoint(self.rect.x + 34, self.rect.y + 32)):
                        self.x += 1
                    moveX = False
                elif(block.rect.collidepoint(self.rect.x + 32 + -offset[0], self.rect.y)):
                    if(not block.rect.collidepoint(self.rect.x + 34, self.rect.y)):
                        self.x += 1
                    moveX = False

        if(moveX):
            self.x += offset[0]

        if(moveY):
            self.y += offset[1]
