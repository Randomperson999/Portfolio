# ---Sprite(s)---

### imports ###
import os
from settings import *
import pygame as pg
from os import path
vec = pg.math.Vector2

def rotateRoom(bgNum, flip=False):
    if flip:
        bgNum += 1
        if bgNum > 3:
            bgNum = 0
    elif not flip:
        bgNum -= 1
        if bgNum < 0:
            bgNum = 3
    return bgNum


class Arrow(pg.sprite.Sprite):
    def __init__(self, game, x, y, flip=False):
        self._layer = ARROW_LYR
        self.groups = game.allSprites, game.arrowsGroup
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.arrowList[0]
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (68, 36))
        self.flip = flip
        if flip:
            self.image = pg.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.frame = 0
        self.lastUpdate = pg.time.get_ticks()
        self.frameRate = 5
        self.flipped = flip
    def update(self):
        now = pg.time.get_ticks()
        if now - self.lastUpdate > 90:
            self.lastUpdate = now
            center = self.rect.center
            if self.frame < 5:
                self.image = self.game.arrowList[self.frame]
                self.image = pg.transform.scale(self.image, (68, 36))
                self.image.set_colorkey(BLACK)
                if self.flipped:
                    self.image = pg.transform.flip(self.image, True, False)
            else:
                self.frame = 0
                self.image = self.game.arrowList[0]
                self.image = pg.transform.scale(self.image, (68, 36))
                self.image.set_colorkey(BLACK)
                if self.flipped:
                    self.image = pg.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame += 1




class Object(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = OBJECT_LYR
        self.groups = game.allSprites, game.objectsGroup
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((80, 25))
        self.image.fill(N_BLUE)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos


class Thing(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        self._layer = THING_LYR
        self.groups = game.allSprites, game.thingsGroup
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos


