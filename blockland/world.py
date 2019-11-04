# Blockland World Generation
from opensimplex import OpenSimplex

class Block:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id


class Chunk:
    def __init__(self, chunkX, chunkWidth, chunkHeight, noiseObject):
        # Generate Chunk
        self.x = chunkX
        self.width = chunkWidth
        self.height = chunkHeight
        self.blocks = []
        for x in range(self.width):
            y = noiseObject.noise2d(x = self.x + x, y = 1) / 3* 5
            yRounded = round(y)
            self.createBlock(self.x + x, yRounded, 0)
            for i in range(self.height):
                yRounded = yRounded + 1
                self.createBlock(self.x + x, yRounded, 1)

    def createBlock(self, x, y, id):
        self.blocks.append(Block(x, y, id))

class World:
    def __init__(self, seed):
        self.chunks = []
        self.seed = seed
        self.chunkWidth = 64
        self.chunkHeight = 32
        self.generator = OpenSimplex(self.seed)
        self.genChunk(0)

    def genChunk(self, x):
        self.chunks.append(Chunk(x, self.chunkWidth, self.chunkHeight, self.generator))
