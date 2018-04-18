import pygame, sys, glob
from pygame import *

h = 400
w = 800

screen = pygame.display.set_mode((w,h))
screen.fill((225,225,225))

clock = pygame.time.Clock()

class chara:
    def __int__(self):
        self.x = w/2
        self.y = h/2
        self.img1 = open("Texture/Chara_animation/ani_1.jpg")
        self.img2 = open("Texture/Chara_animation/ani_2.jpg")
        self.img3 = open("Texture/Chara_animation/ani_3.jpg")
        self.img4 = open("Texture/Chara_animation/ani_4.jpg")
        self.img5 = open("Texture/Chara_animation/ani_5.jpg")
        self.img6 = open("Texture/Chara_animation/ani_6.jpg")
        self.img7 = open("Texture/Chara_animation/ani_7.jpg")
        self.img8 = open("Texture/Chara_animation/ani_8.jpg")
        self.img9 = open("Texture/Chara_animation/ani_9.jpg")
        self.img10 = open("Texture/Chara_animation/ani_10.jpg")
        self.img11 = open("Texture/Chara_animation/ani_11.jpg")
        self.img12 = open("Texture/Chara_animation/ani_12.jpg")
        self.img13 = open("Texture/Chara_animation/ani_13.jpg")
        self.list = [self.img1, self.img2, self.img3, self.img4, self.img5, self.img6, self.img7, self.img8, self.img9, self.img10, self.img11, self.img12, self.img13]

    def animation(self):
        self.pos = 1
        if self.pos != 0:
            while self.pos != 13:
                for i in len(self.list):
                    screen.blit(self.img, (self.x, self.y))
                    self.pos += 1
                if self.pos == 13:
                    self.pos = 1
chara1 = chara()


while 1:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                chara1.pos = 1
                chara1.animation()
            if event.key == pygame.K_d:
                chara1.pos = 1
                chara1.animation()
            if event.key == pygame.K_s:
                chara1.pos = 1
                chara1.animation()
            if event.key == pygame.K_w:
                chara1.pos = 1
                chara1.animation()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                chara1.pos = 0
            if event.key == pygame.K_d:
                chara1.pos = 0
            if event.key == pygame.K_s:
                chara1.pos = 0
            if event.key == pygame.K_w:
                chara1.pos = 0

    pygame.display.update()