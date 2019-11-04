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

    def isOnFloor(self, world):
        if (world.blockAt(self.rect.x, self.rect.y + 66) or world.blockAt(self.rect.x + 32, self.rect.y + 66)):
            return True
        return False

    def tick(self, world):
        self.yVelocity += self.grav
        if(self.yVelocity < -self.maxYVelocity):
            self.yVelocity = -self.maxYVelocity

        if(self.isOnFloor(world)):
            if(self.yVelocity < 0):
                self.yVelocity = 0

        self.move(world, [0, self.yVelocity])

    def move(self, world, offset):
        moveX = True
        moveY = True

        if(offset[1] < 0):
            if(world.blockAt(self.rect.x, self.rect.y + 64 - offset[1]) or world.blockAt(self.rect.x + 32, self.rect.y + 64 - offset[1])):
                moveY = False
                if not(self.isOnFloor(world)):
                    self.y -= 1

        checkPoints = [64, 32, 0]
        if(offset[0] > 0):
            for checkPoint in checkPoints:
                if(world.blockAt(self.rect.x - offset[0], self.rect.y + checkPoint)):
                    moveX = False
                    if not(world.blockAt(self.rect.x - 2, self.rect.y + checkPoint)):
                        self.x -= 1
        else:
            for checkPoint in checkPoints:
                if(world.blockAt(self.rect.x + 32 - offset[0], self.rect.y + checkPoint)):
                    moveX = False
                    if not(world.blockAt(self.rect.x + 34, self.rect.y + checkPoint)):
                        self.x += 1

        if(moveX):
            self.x += offset[0]

        if(moveY):
            self.y += offset[1]
