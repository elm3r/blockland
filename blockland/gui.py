import pygame

class Hotbar:
    def __init__(self):
        self.bgimg = pygame.image.load("res/gui/hotbar.png")
        self.selimg = pygame.image.load("res/gui/hotbar-selected.png")
        self.selimg.set_colorkey((0, 0, 0))
        self.items = []
        self.selected = 0

    def draw(self, screen):
        screen.blit(self.bgimg, (0, 558))
        screen.blit(self.selimg, (3 + (self.selected * 37), 561))
        for item in range(len(self.items)):
            screen.blit(self.items[item], (5 + (item * 37), 563))
