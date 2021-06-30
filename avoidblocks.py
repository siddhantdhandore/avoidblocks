import pygame
import random
import time
import math

#constants
WIDTH=600
HEIGHT=500
FPS=60
SCORE=0

#COLORS
BLACK=(0,0,0)
RED=(255,0,0)

WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(0,0,255)
GOLD=(255, 215, 0)
KHAKI=(189, 183, 107)
THISTLE=(216, 191, 216)
OLIVE=(107, 142, 35)
PERU=(205, 133, 63)
ENEMYCOLORS=[WHITE,GREEN,BLUE,GOLD,KHAKI,THISTLE,OLIVE,PERU]

#initialize game window
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Avoid Blocks")
clock=pygame.time.Clock()

#GAME OBJECTS 
def player(playerX,playerY,playerWidth,playerHeight,playerColor):
	pygame.draw.rect(screen,playerColor,[playerX,playerY,playerWidth,playerHeight])
playerWidth=50
playerHeight=50
playerX=WIDTH//2-playerWidth//2
playerY=HEIGHT-playerHeight
playerX_change=0
playerColor=RED


#ENEMY
numberOfEnemies=6
def enemy(enemyX,enemyY,enemyWidth,enemyHeight,enemyColor):
	pygame.draw.rect(screen,enemyColor,[enemyX,enemyY,enemyWidth,enemyHeight])


enemyWidth=[]
enemyHeight=[]
enemyX=[]
enemyY=[]
enemyColor=[]
enemyY_change=[]

for i in range(numberOfEnemies):
	enemyWidth.append(random.randint(40,80))
	enemyHeight.append(50)
	enemyX.append(random.randint(0,WIDTH-enemyWidth[i]))
	enemyY.append(random.randint(-40,0))
	enemyColor.append(random.choice(ENEMYCOLORS))
	enemyY_change.append(random.randint(5,10))

#DISPLAY SCORE

scoreFont=pygame.font.Font("freesansbold.ttf",30)
def displayScore():
	textSurface=scoreFont.render(f"Score : {SCORE}",True,(0,255,255))
	screen.blit(textSurface,(10,10))

gameOverFont=pygame.font.Font("freesansbold.ttf",50)
def displayGameOver():
	textSurface=gameOverFont.render("Game Over...!!!",True,(255,255,0))
	textRect=textSurface.get_rect()
	textRect.center=((WIDTH/2),(HEIGHT/2))
	screen.blit(textSurface,textRect)
	pygame.display.update()
	time.sleep(3)


#DETECT COLISION
def hasColided(enemyX,enemyY,playerX,playerY):
	if math.sqrt(math.pow((enemyX-playerX),2)+math.pow((enemyY-playerY),2))<=55:
		return True
#GAME RESET
def reset():
	global enemyWidth,enemyHeight,enemyX,enemyY,enemyColor,enemyY_change,SCORE
	enemyWidth=[]
	enemyHeight=[]
	enemyX=[]
	enemyY=[]
	enemyColor=[]
	enemyY_change=[]
	for i in range(numberOfEnemies):
		enemyWidth.append(random.randint(40,80))
		enemyHeight.append(50)
		enemyX.append(random.randint(0,WIDTH-enemyWidth[i]))
		enemyY.append(random.randint(-40,0))
		enemyColor.append(random.choice(ENEMYCOLORS))
		enemyY_change.append(random.randint(5,10))
	SCORE=0

#game loop
running=True

while running:
	clock.tick(FPS)
	

	# 1 --> event checking loop
	for event in pygame.event.get():
		#exit game
		if event.type==pygame.QUIT:
			running=False
			pygame.quit()
			quit()

		#keyevents for player movement
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				playerX_change=-5
			if event.key==pygame.K_RIGHT:
				playerX_change=5
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
				playerX_change=0


	# 2 --> draw objects
	screen.fill(BLACK)

	#PLAYER
	# 1)player horizontal movement
	playerX+=playerX_change

	# 2)boundaries for players
	if playerX<=0:
		playerX=0
	if playerX>=WIDTH-playerWidth:
		playerX=WIDTH-playerWidth


	player(playerX,playerY,playerWidth,playerHeight,playerColor)




	#ENEMY
	# 1)ENEMY vertical movement
	for i in range(numberOfEnemies):
		enemyY[i]+=enemyY_change[i]
		# 2)respawn for ENEMY
		if enemyY[i]>=HEIGHT:
			SCORE+=1
			enemyY[i]=random.randint(-40,0)
			enemyX[i]=random.randint(0,WIDTH-enemyWidth[i])
			enemyWidth[i]=random.randint(40,80)
			enemyColor[i]=random.choice(ENEMYCOLORS)
			enemyY_change[i]=random.randint(5,10)
		#COLISION DETECTION BETWEEN PLAYER AND ENEMY
		if hasColided(enemyX[i],enemyY[i],playerX,playerY):
			reset()
			displayGameOver()


		enemy(enemyX[i],enemyY[i],enemyWidth[i],enemyHeight[i],enemyColor[i])

	
	# 3 --> display updation
	displayScore()
	pygame.display.update()


quit()

