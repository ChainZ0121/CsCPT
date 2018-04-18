import pygame, sys, glob
from pygame import *

h = 400
w = 800

screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

class player:
    def __int__(self):
        self.x = 200
        self.y = 300
        self.ani_speed_int = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob("Chara_animation/ani_*.jpg")
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        self.update(0)
    def update(self, pos):
        if pos != 0:
            self.ani_speed -= 1
            self.x += pos
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1
        screen.blit(self.img,(self.x,self.y))

player1 = player()
pos = 0

while 1:
    screen.fill((225,225,225))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            pos = 1
        elif event.type == KEYUP and event.key == K_RIGHT:
            pos = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            pos = -1
        elif event.type == KEYUP and event.key == K_LEFT:
            pos = 0
    player1.update(pos)
    pygame.display.update()