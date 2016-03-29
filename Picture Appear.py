import pygame
import time
from pygame.locals import *
from random import randrange
import pygame.surfarray as surfarray
pygame.init()



#LOAD THE IMAGE
imgsurface = pygame.image.load("back1.jpg")

#SET IMAGE DEFORMATION (Min: 2)
deform = 10

#SET UPDATE TIMER
timer = 1000

#START FILLED?
filled = True

#SLOWLY BETTER PICTURE? (Deform Min: 10)
better = True



imgarray = surfarray.array3d(imgsurface)

blue = (0,0,255)
white = (255,255,255)
pink = (255,200,200)

Width = imgsurface.get_width()
Height = imgsurface.get_height()

screen = pygame.display.set_mode((Width,Height))
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(white)
screen.blit(background,(0,0))


if filled:
	for y in range(Height):
		for x in range(Width):
			toAppend = imgarray[x][y][0], imgarray[x][y][1], imgarray[x][y][2]
			pygame.draw.rect(screen, toAppend, (x, y, deform, deform), 0)

	pygame.display.update()


wait = 0

while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()

	#screen.blit(background,(0,0))
	
	random1 = randrange(0, Width)
	random2 = randrange(0, Height)

	toAppend = imgarray[random1][random2][0], imgarray[random1][random2][1], imgarray[random1][random2][2]

	pygame.draw.rect(screen, toAppend, (random1, random2, deform, deform), 0)

	if wait > timer:
		pygame.display.update()
		wait = 0
		if deform > 3 and better:
			deform = deform*0.99

	wait += 1