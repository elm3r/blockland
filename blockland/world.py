# Blockland World Generation
from opensimplex import OpenSimplex
import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        self.id = 0
        self.image = image
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        super().__init__()

    def move(self, offset):
        self.rect.x = self.x + offset[0]
        self.rect.y = self.y + offset[1]

class World:
    def __init__(self, width, seed):
        self.generator = TerrainGenerator(seed)
        self.blockList = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
        self.width = width
        self.blockImages = []
        self.height = 32
        self.dirtHeight = 4

    def blockAt(self, x, y):
        for block in self.blockList.sprites():
            if(block.rect.collidepoint(x, y)):
                return block

        return None

    def generate(self):
        for x in range(self.width):
            y = self.generator.getHeight(x)
            self.createBlock(x, y)
            for i in range(self.dirtHeight):
                y += 1
                self.createBlock(x, y, 1)
            for i in range(self.height - self.dirtHeight):
                y += 1
                self.createBlock(x, y, 2)

    def createBlock(self, x, y, type=0):
        block = Block(self.blockImages[type])
        block.rect.x = x * 32
        block.rect.y = y * 32
        block.x = x * 32
        block.y = y * 32
        self.blockList.add(block)

    def draw(self, screen, offset):
        for block in self.blockList.sprites():
            block.move(offset)
        self.blockList.draw(screen)
        self.entities.draw(screen)

class TerrainGenerator:
    def __init__(self, seed):
        self.seed = seed
        self.noise = OpenSimplex(self.seed)

    def getHeight(self, x):
        return round(self.noise.noise2d(x = x, y = 1) / 2 * 3)
