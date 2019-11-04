print("Block Land ALPHA")

import pygame
from blockland import world
from blockland import player
from blockland import camera

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load block images
blocks = []
blocks.append(pygame.image.load("res/grass.png"))
blocks.append(pygame.image.load("res/dirt.png"))

# Load other images
playerImg = pygame.image.load("res/player.png")

# Mainloop
gameState = 0 # 0 - Good, 1 - Quit, 2 - Crashed

gameWorld = world.World(1234)
gameCamera = camera.Camera()
gamePlayer = player.Player()

freecamEnabled = True

while gameState == 0:
	screen.fill((58, 132, 253))

	keysPressed = pygame.key.get_pressed()

	###########
	# FREECAM #
	###########
	if(freecamEnabled):
		if(keysPressed[pygame.K_d]):
			gameCamera.x += 10
		if(keysPressed[pygame.K_a]):
			gameCamera.x -= 10
		if(keysPressed[pygame.K_w]):
			gameCamera.y -= 10
		if(keysPressed[pygame.K_s]):
			gameCamera.y += 10
		screen.blit(playerImg, (gamePlayer.x - gameCamera.x, gamePlayer.y- gameCamera.y - 32))
	else:
		if(keysPressed[pygame.K_a]):
			gamePlayer.x -= 5
		if(keysPressed[pygame.K_d]):
			gamePlayer.x += 5
		screen.blit(playerImg, (gamePlayer.x - gameCamera.x, gamePlayer.y- gameCamera.y - 32))
		gameCamera.centerOn(gamePlayer)

	for chunk in gameWorld.chunks:
		r = []
		for b in range(len(chunk.blocks)):
			block = chunk.blocks[b]
			# TODO: Clean Me
			if(pygame.mouse.get_pressed()[0]):
				if(pygame.mouse.get_pos()[0] > block.x * 32 - gameCamera.x and pygame.mouse.get_pos()[0] < (block.x + 1) * 32 - gameCamera.x):
					if(pygame.mouse.get_pos()[1] > (block.y) * 32 + 300 - gameCamera.y and pygame.mouse.get_pos()[1] < (block.y + 1) * 32 + 300 - gameCamera.y):
						print("Remove!")
						r.append(b)
			screen.blit(blocks[block.id], ((block.x * 32) - gameCamera.x, (300 + (block.y * 32)) - gameCamera.y))

		for block in r:
			chunk.blocks.pop(block)

	for event in pygame.event.get():
		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_q):
				if(freecamEnabled):
					freecamEnabled = False
				else:
					freecamEnabled = True
	pygame.display.update()
