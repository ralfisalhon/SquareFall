import pygame
import time
from pygame.locals import *
from random import randrange
import pygame.surfarray as surfarray
pygame.init()

imgsurface = pygame.image.load("surfarray.jpg")
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

'''print imgarray
print len(imgarray)
print imgarray[0][0]

print imgarray[0][0][0]
print imgarray[0][0][1]
print imgarray[0][0][2]'''

positions = []

while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()

	screen.blit(background,(0,0))
	
	for x in range(len(positions)):
		pygame.draw.rect(screen, positions[x][0], (positions[x][1],positions[x][2],2,2), 0)

	random1 = randrange(0, Width)
	random2 = randrange(0, Height)

	#print imgarray[random1][random2]

	toAppend = imgarray[random1][random2][0],imgarray[random1][random2][1],imgarray[random1][random2][2]

	positions.append((toAppend,random1,random2))

	#print positions

	pygame.display.update()