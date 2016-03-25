import pygame
import time
from pygame.locals import *
from random import randrange
pygame.init()

pygame.display.set_caption("Square Fall")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
cyan = (0,255,255)

colors = [red, green, blue, darkBlue, black, pink, cyan]

Width = 800
Height = 600

positions = []

screen = pygame.display.set_mode((Width,Height),pygame.FULLSCREEN)
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(white)
screen.blit(background,(0,0))

moving = False

heights = []

for x in range(Width/50):
	heights.append(Height-50)

while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_q:
				print positions
				exit()

	screen.blit(background,(0,0))

	for x in range(len(positions)):
		pygame.draw.rect(screen, positions[x][0], (positions[x][1],positions[x][2],50,50), 0)

	if not moving:
		moving = True
		positions.append(list((colors[randrange(0,len(colors))],randrange(0,Width/50)*50,0)))
	else:
		positions[len(positions)-1][2] += 50

	if positions[len(positions)-1][2] == heights[(positions[len(positions)-1][1]/50)-1] or heights[(positions[len(positions)-1][1]/50)-1]<0:
		moving = False
		heights[(positions[len(positions)-1][1]/50)-1] -= 50
		
		if heights[(positions[len(positions)-1][1]/50)-1]<-50:
			del positions[len(positions)-1]

	pygame.display.update()
	#time.sleep(0.1)