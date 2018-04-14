import pygame

def loadConfig():
    global screenW, screenH
    config = open ("config.txt", "r")
    configDataStr = config.readlines()
    configData = []
    for item in configDataStr:
        item = item.split("=")
        configData.append(item[1][:-1])
    screenW = int(configData[0].split(",")[0])
    screenH = int(configData[0].split(",")[1])
loadConfig()

pygame.init()
gameDisplay = pygame.display.set_mode((screenW,screenH))
pygame.display.update()
pygame.quit()
quit()
