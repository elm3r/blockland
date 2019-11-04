print("Block Land ALPHA")

import pygame
import math
import blockland.player
import blockland.world
import blockland.gui

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

clock = pygame.time.Clock()
player = blockland.player.Player()
player.rect.x = 384
player.rect.y = 268
world = blockland.world.World(32, 1234)
world.generate()
world.entities.add(player)
hotbar = blockland.gui.Hotbar()
hotbar.items.append(pygame.image.load("res/grass.png"))
hotbar.items.append(pygame.image.load("res/dirt.png"))
hotbar.items.append(pygame.image.load("res/stone.png"))
hotbar.items.append(pygame.image.load("res/brick.png"))
hotbar.items.append(pygame.image.load("res/wood.png"))
hotbar.items.append(pygame.image.load("res/gold.png"))
hotbar.items.append(pygame.image.load("res/iron.png"))
hotbar.items.append(pygame.image.load("res/diamond.png"))
hotbar.items.append(pygame.image.load("res/leaves.png"))
hotbar.items.append(pygame.image.load("res/tnt.png"))

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
		player.move(world.blockList, [player.movementSpeed, 0])
	if(keysPressed[pygame.K_d]):
		player.move(world.blockList, [-player.movementSpeed, 0])

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
		for block in world.blockList.sprites():
			if(block.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
				world.blockList.remove(block)

	# Right Click
	if(pygame.mouse.get_pressed()[2]):
		blockFound = False
		for block in world.blockList.sprites():
			if(block.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
				blockFound = True

		if(blockFound == False):
			clickX = pygame.mouse.get_pos()[0] - player.cameraOffset[0]
			clickY = pygame.mouse.get_pos()[1] - player.cameraOffset[1]
			gridX = (clickX - (clickX % 32)) / 32
			gridY = (clickY - (clickY % 32)) / 32
			world.createBlock(gridX, gridY, hotbar.selected)

	player.tick(world.blockList)
	clock.tick(60)
	player.calculateCameraOffset()
	world.draw(screen, player.cameraOffset)
	hotbar.draw(screen)
	pygame.display.update()
