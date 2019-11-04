print("Blockland Alpha (Version 0.01a)")

import pygame
import math
import blockland.player
import blockland.world
import blockland.gui
from random import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()
player = blockland.player.Player()
player.rect.x = 384
player.rect.y = 268
world = blockland.world.World(64, int(random() * 100000))
hotbar = blockland.gui.Hotbar()
itemImages = ["res/grass.png", "res/dirt.png", "res/stone.png", "res/brick.png", "res/wood.png", "res/gold.png", "res/iron.png", "res/diamond.png", "res/leaves.png", "res/tnt.png", ]
for image in itemImages:
	hotbar.items.append(pygame.image.load(image))
	world.blockImages.append(pygame.image.load(image))
world.generate()
world.entities.add(player)

while running:
	screen.fill((58, 132, 253))

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			running = False

		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_SPACE):
				player.yVelocity += 10

	# Player Code
	keysPressed = pygame.key.get_pressed()
	if(keysPressed[pygame.K_a]):
		player.move(world, [player.movementSpeed, 0])
	if(keysPressed[pygame.K_d]):
		player.move(world, [-player.movementSpeed, 0])

	# Hotbar Code
	if(keysPressed[pygame.K_1]):
		hotbar.selected = 0
	if(keysPressed[pygame.K_2]):
		hotbar.selected = 1
	if(keysPressed[pygame.K_3]):
		hotbar.selected = 2
	if(keysPressed[pygame.K_4]):
		hotbar.selected = 3
	if(keysPressed[pygame.K_5]):
		hotbar.selected = 4
	if(keysPressed[pygame.K_6]):
		hotbar.selected = 5
	if(keysPressed[pygame.K_7]):
		hotbar.selected = 6
	if(keysPressed[pygame.K_8]):
		hotbar.selected = 7
	if(keysPressed[pygame.K_9]):
		hotbar.selected = 8
	if(keysPressed[pygame.K_0]):
		hotbar.selected = 9

	# Left Click
	if(pygame.mouse.get_pressed()[0]):
		block = world.blockAt(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
		if(block != None):
			world.blockList.remove(block)

	# Right Click
	if(pygame.mouse.get_pressed()[2]):
		if not(world.blockAt(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
			clickX = pygame.mouse.get_pos()[0] - player.cameraOffset[0]
			clickY = pygame.mouse.get_pos()[1] - player.cameraOffset[1]
			gridX = (clickX - (clickX % 32)) / 32
			gridY = (clickY - (clickY % 32)) / 32
			world.createBlock(gridX, gridY, hotbar.selected)

	player.tick(world)
	clock.tick(60)
	player.calculateCameraOffset()
	world.draw(screen, player.cameraOffset)
	hotbar.draw(screen)
	pygame.display.update()
