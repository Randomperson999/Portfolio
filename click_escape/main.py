import pygame as pg
import random as r
import math as m
import os
from settings import *
from sprites import *

class Game(object):
    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.mousex, self.mousey = pg.mouse.get_pos()
        self.mouse_bttn_held = False
        self.arrowList = []
        self.f_arrowList = []
        self.bgColor = BLUE
        self.bgNum = 0
    def loadImgs(self):
        self.arrowList = []
        for i in range(1, 7):
            fn = "Arrow-{}.png".format(i)
            self.arrowList.append(pg.image.load(os.path.join(arrowFolder, fn)).convert())
        # Backgrounds
        self.backgrounds = []
        for i in range(0, 4):
            self.backgrounds.append(pg.image.load(os.path.join(bgFolder, "room{}.png".format(i + 1))).convert())
            self.backgrounds[i] = pg.transform.scale(self.backgrounds[i], (1000, 500))
        self.bgRect = self.backgrounds[0].get_rect()
    def newGame(self):
        """starts a new game"""
        self.loadImgs()
        # create new groups

        self.allSprites = pg.sprite.LayeredUpdates()
        self.arrowsGroup = pg.sprite.Group()
        self.objectsGroup = pg.sprite.Group()
        self. thingsGroup = pg.sprite.Group()
        # game objects
        self.arrow = Arrow(self, WIDTH * (23.5 / 25), HEIGHT / 2)
        self.arrow2 = Arrow(self, WIDTH * (1.5 / 25), HEIGHT / 2, True)

        self.run()

    def run(self):
        """runs the game"""
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.mousex, self.mousey = pg.mouse.get_pos()
            self.events()
            self.update()
            self.draw()
    def events(self):
        """Game Loop - Events"""
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                self.playing = False
            self.running = False
            for arrow in self.arrowsGroup:
                if event.type == pg.MOUSEBUTTONDOWN and arrow.rect.collidepoint(pg.mouse.get_pos()):
                    self.mouse_bttn_held = True
                    if arrow.flip:
                        self.bgNum = rotateRoom(self.bgNum)
                    elif not arrow.flip:
                        self.bgNum = rotateRoom(self.bgNum, True)
                if event.type == pg.MOUSEBUTTONUP and self.mouse_bttn_held:
                    self.mouse_bttn_held = False
    def update(self):
        """Game Loop - Update"""
        self.allSprites.update()

    def draw(self):
        """Game Loop - Draw"""
        self.screen.fill(BLACK)
        if self.bgNum > 3:
            self.bgNum = 0
        self.screen.blit(self.backgrounds[self.bgNum], self.bgRect)
        self.allSprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def startScreen(self):
        pass

    def gameOver(self):
        pass

    def options(self):
        pass


g = Game()
g.startScreen()


while g.running:
    g.newGame()
    g.gameOver()

pg.quit()

