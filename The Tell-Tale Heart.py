import pygame, sys
from pygame.locals import *
map = pygame.image.load("Texture/background.jpg")

#Funtions:
def loadConfig():
    global screenW, screenH, FPS
    config = open ("config.txt", "r")
    configDataStr = config.readlines()
    configData = []
    for item in configDataStr:
        item = item.split("=")
        configData.append(item[1][:-1])
    screenW = int(configData[0].split(",")[0])
    screenH = int(configData[0].split(",")[1])
    FPS = int(configData[1])
def character(x,y):
    gameDisplay.blit(map,(x,y))



loadConfig()



#game Initial


area = screenW * screenH
x, y = screenW / 2, screenH / 2
white = (225,225,225)
black = (0,0,0)
red = (225,0,0)
green = (0,225,0)
blue = (0,0,225)
yellow = (225,225,0)
purple = (225,0,225)
cyan = (0,225,225)

solid_fill = 0


pygame.init()
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption('The Tell-Tale Heart')




gameExit = False

lead_x = 0
lead_y = 0
lead_x_change = 0
lead_y_change = 0
speed = FPS/20

#game Event Loop:
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                lead_x_change = speed
            if event.key == pygame.K_d:
                lead_x_change = -speed
            if event.key == pygame.K_s:
                lead_y_change = -speed
            if event.key == pygame.K_w:
                lead_y_change = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                lead_x_change = 0
            if event.key == pygame.K_d:
                lead_x_change = 0
            if event.key == pygame.K_s:
                lead_y_change = 0
            if event.key == pygame.K_w:
                lead_y_change = 0

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)
    character(lead_x,lead_y)
    pygame.draw.rect(gameDisplay, red, [x, y, 20, 20])
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
quit()
