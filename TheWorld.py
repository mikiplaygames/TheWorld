import random
import time

import pygame
import World
import Button


class THEWORLD:
    WIDTH = 20
    HEIGHT = 20
    textureSize = 32

    theWorld = World.WORLD()
    theWorld.RandomizeWorld(WIDTH, HEIGHT)
    map = theWorld.map

    pygame.init()

    buttonSpace = 40
    s_width = textureSize * WIDTH + 500
    s_height = textureSize * HEIGHT + buttonSpace
    screen = pygame.display.set_mode((s_width, s_height))
    screen.blit(pygame.image.load('resources/bg.png'), (0, 0))

    def draw(self):
        self.screen.fill(0)
        self.screen.blit(pygame.image.load('resources/bg.png'), (0, 0))
        for i in self.theWorld.organisms:
            if i is not None:
                self.screen.blit(pygame.image.load(i.image_path), (i.x * self.textureSize, i.y * self.textureSize))


w = THEWORLD()
w.draw()
bt = Button.BUTTON(w.s_width / 4, w.s_height - 40, pygame.image.load('resources/button.png'), 1)
running = True

while running:

    if bt.draw(w.screen):
        w.theWorld.NextRound()
        w.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
