import pygame
import random

pygame.init()  # imp. line to use the pygame
# Screen
screen = pygame.display.set_mode((800, 600))  # width and height

# background
background = pygame.image.load('background.png')
# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
K = 0.0

bulletImg = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 550
bullet_changeX = 0.0
bullet_changeY = 0.0

def player(x, y):
    screen.blit(bulletImg, (x, y))

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 550
player_changeX = 0.0
player_changeY = 0.0

def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy

 # Enemy 1
enemyImg1 = pygame.image.load('alien1.png')
enemyX1 = random.randint(0,800)
enemyY1 = random.randint(0,600)
enemy_changeX1 = 0.2
enemy_changeY1 = 0.0

def enemy1(x, y):
    screen.blit(enemyImg1, (x, y))

 # Enemy 2
enemyImg2 = pygame.image.load('alien2.png')
enemyX2 = random.randint(0,800)
enemyY2 = random.randint(0,600)
enemy_changeX2 = 0.2
enemy_changeY2 = 0.1

def enemy2(x, y):
    screen.blit(enemyImg2, (x, y))

 # Enemy 3
enemyImg3 = pygame.image.load('alien3.png')
enemyX3 = random.randint(0,800)
enemyY3 = random.randint(0,600)
enemy_changeX3 = 0.2
enemy_changeY3 = 0.0

def enemy3(x, y):
    screen.blit(enemyImg3, (x, y))

# Game infinite loop
running = True
while running:

    # RGB - Red,Green,Blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is press check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_changeX = -0.2
            if event.key == pygame.K_RIGHT:
                player_changeX = 0.2
            if event.key == pygame.K_UP:
                player_changeY = -0.2
            if event.key == pygame.K_DOWN:
                player_changeY = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                player_changeX = 0
                player_changeY = 0

    # player
    playerX += player_changeX
    playerY += player_changeY

    if playerX >= 800:
        playerX = 1
    if playerX <= 0:
        playerX = 800

    if playerY >= 600:
        playerY = 1
    if playerY <= 0:
        playerY = 600

   # enemy 1
    enemyX1 += enemy_changeX1
    enemyY1 += enemy_changeY1

    if enemyX1 >= 800:
        enemyX1 = 1
        k = random.randint(2,5)
        enemy_changeX1 = k*0.1
        enemyY1 += random.randint(-90,90)

    if enemyX1 <= 0:
        enemyX1 = 800
        k = random.randint(2, 5)
        enemy_changeX1 = k * 0.1
        enemyY1 += random.randint(-90,90)

    if enemyY1 >= 800:
        enemyY1 = 1
    if enemyY1 <= 0:
        enemyY1 = 800

    # enemy 2
    enemyX2 += enemy_changeX2
    enemyY2 += enemy_changeY2

    if enemyX2 >= 800:
        enemyX2 = 1
    if enemyX2 <= 0:
        enemyX2 = 800

    if enemyY2 >= 800:
        enemyY2 = 1
    if enemyY2 <= 0:
        enemyY2 = 800

    # enemy 3
    enemyX3 += enemy_changeX3
    enemyY3 += enemy_changeY3

    if enemyX3 >= 800:
        enemyX3 = 1
        k = random.randint(2, 5)
        enemy_changeX3 = k * 0.1
        enemyY3 += random.randint(-90, 90)

    if enemyX3 <= 0:
        enemyX3 = 800
        k = random.randint(2, 5)
        enemy_changeX3 = k * 0.1
        enemyY3 += random.randint(-90, 90)

    if enemyY3 >= 800:
        enemyY3 = 1
    if enemyY3 <= 0:
        enemyY3 = 800




    player(playerX, playerY)
    enemy1(enemyX1, enemyY1)
    enemy2(enemyX2, enemyY2)
    enemy3(enemyX3,enemyY3)
    pygame.display.update()
