import pygame

import Button
import World


class THEWORLD:
    WIDTH = 20
    HEIGHT = 20
    textureSize = 32
    logBoxSize = 400

    theWorld = World.WORLD()
    theWorld.RandomizeWorld(WIDTH, HEIGHT)
    map = theWorld.map

    pygame.init()

    buttonSpace = 40
    s_width = textureSize * WIDTH + logBoxSize
    s_height = textureSize * HEIGHT + buttonSpace
    screen = pygame.display.set_mode((s_width, s_height))
    screen.blit(pygame.image.load('resources/bg.png'), (0, 0))
    font = pygame.font.SysFont('Arial', 20)

    def draw(self):
        self.screen.fill(0)
        self.screen.blit(pygame.image.load('resources/bg.png'), (0, 0))
        for i in self.theWorld.organisms:
            if i is not None:
                self.screen.blit(pygame.image.load(i.image_path), (i.x * self.textureSize, i.y * self.textureSize))


w = THEWORLD()
pygame.display.set_caption("THE WORLD")
w.draw()
bt = Button.BUTTON(w.s_width / 4, w.s_height - 40, pygame.image.load('resources/button.png'), 1)
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


while running:

    if bt.draw(w.screen):
        w.theWorld.NextRound()
        w.draw()
        blit_text()
        w.theWorld.log = ""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()