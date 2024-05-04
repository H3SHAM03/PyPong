import pygame

pygame.init()
pygame.display.set_mode((1280,720))
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				print("UP press")
			elif event.key == pygame.K_DOWN:
				print("DOWN press")
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				print("UP released")
			elif event.key == pygame.K_DOWN:
				print("DOWN released")