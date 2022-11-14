import random
import pygame
import World
import Button


class THEWORLD:
    WIDTH = 20
    HEIGHT = 20

    theWorld = World.WORLD()
    theWorld.RandomizeWorld(WIDTH, HEIGHT)
    map = theWorld.map

    pygame.init()

    buttonSpace = 40
    s_width = 32 * WIDTH
    s_height = 32 * HEIGHT + buttonSpace
    screen = pygame.display.set_mode((s_width, s_height))
    screen.blit(pygame.image.load('resources/bg.png'), (0, 0))

    def ZWARAUTDO(self):
        for x in range(0, self.WIDTH):
            for y in range(0, self.HEIGHT):
                rand = random.randrange(0, 5)
                if rand == 1:
                    self.screen.blit(pygame.image.load('resources/shep.png'), (x * 32, y * 32))
                elif rand == 2:
                    self.screen.blit(pygame.image.load('resources/lis.png'), (x * 32, y * 32))


w = THEWORLD()
w.ZWARAUTDO()
bt = Button.BUTTON(w.s_width / 4, w.s_height - 40, pygame.image.load('resources/button.png'), 1)
running = True

while running:

    if bt.draw(w.screen):
        w.theWorld.NextRound()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
