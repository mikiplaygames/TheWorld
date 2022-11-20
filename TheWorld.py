import time

import pygame

import Button
import World


class THEWORLD:
    WIDTH = 24
    HEIGHT = 24
    textureSize = 32
    logBoxSize = 400
    bgColor = '#95b84b'

    theWorld = World.WORLD()
    theWorld.RandomizeWorld(WIDTH, HEIGHT)
    map = theWorld.map

    pygame.init()

    s_width = textureSize * WIDTH + logBoxSize
    s_height = textureSize * HEIGHT
    screen = pygame.display.set_mode((s_width, s_height))
    # screen.blit(pygame.image.load('resources/bg.png'), (0, 0))
    screen.fill(bgColor)
    font = pygame.font.SysFont('Arial', 20)

    def draw(self):
        self.screen.fill(0)
        self.screen.fill(self.bgColor)
        self.screen.fill('#000000', pygame.Rect(self.s_width - self.logBoxSize, 0, self.logBoxSize, self.s_height))
        # self.screen.blit(pygame.image.load('resources/bg.png'), (0, 0))
        for i in self.theWorld.organisms:
            if i is not None:
                self.screen.blit(pygame.image.load(i.currentImage()), (i.x * self.textureSize, i.y * self.textureSize))


w = THEWORLD()
pygame.display.set_caption("THE WORLD")
w.draw()
nextBt = Button.BUTTON(w.s_width - w.logBoxSize, w.s_height - 40, pygame.image.load('resources/button.png'), 1)
autoBt = Button.BUTTON(w.s_width - w.logBoxSize / 4, w.s_height - 40, pygame.image.load('resources/auto.png'), 1)
running = True


def blit_text():
    slicedUpLog = w.theWorld.log.split('|')
    location = 20
    for i in slicedUpLog:
        text = w.font.render(i, True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.center = (w.s_width - w.logBoxSize / 2, location)
        location += 20
        w.screen.blit(text, textRect)


auto = False

while running:

    if nextBt.draw(w.screen):
        w.theWorld.NextRound()
        w.draw()
        blit_text()
        w.theWorld.log = ""

    if autoBt.draw(w.screen):
        auto = not auto

    if auto:
        time.sleep(0.1)
        w.theWorld.NextRound()
        w.draw()
        blit_text()
        w.theWorld.log = ""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
