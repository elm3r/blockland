print("Block Land ALPHA")

import pygame
import math
import blockland.player
import blockland.world

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

player = blockland.player.Player()
player.rect.x = 384
player.rect.y = 268
world = blockland.world.World(32, 1234)
world.generate()
world.entities.add(player)

while running:
	screen.fill((58, 132, 253))

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			running = False

	# Player Code
	keysPressed = pygame.key.get_pressed()
	if(keysPressed[pygame.K_w]):
		player.y += player.movementSpeed
	if(keysPressed[pygame.K_s]):
		player.y -= player.movementSpeed
	if(keysPressed[pygame.K_a]):
		player.x += player.movementSpeed
	if(keysPressed[pygame.K_d]):
		player.x -= player.movementSpeed

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
			world.createBlock(gridX, gridY, 1)

	player.calculateCameraOffset()
	world.draw(screen, player.cameraOffset)
	pygame.display.update()
