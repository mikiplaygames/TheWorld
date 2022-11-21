import json
import time

import pygame
import pickle
import Button
import World
import Animals.Sheep as Sheep
import Animals.Fox as Fox
import Plants.Weed as Weed
import Plants.Coke as Coke
import Animals.Snail as Snail
import Animals.Mouse as Mouse
import Organism as Organism


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

    def write_list(self):
        # store list in binary file so 'wb' mode
        with open('list', 'wb') as fp:
            pickle.dump(w.theWorld.organisms, fp)
            print('Done writing list into a binary file')

    # Read list to memory
    def read_list(self):
        # for reading also binary mode is important
        with open('list', 'rb') as fp:
            n_list = pickle.load(fp)
            return n_list

    def write_map(self):
        # store list in binary file so 'wb' mode
        with open('map', 'wb') as fp:
            pickle.dump(map, fp)
            print('Done writing list into a binary file')

    # Read list to memory
    def read_map(self):
        # for reading also binary mode is important
        with open('map', 'rb') as fp:
            n_list = pickle.load(fp)
            return n_list

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
        if event.type == pygame.KEYDOWN:
            pos = pygame.mouse.get_pos()
            posX = int(pos[0] / w.textureSize)
            posY = int(pos[1] / w.textureSize)
            if posX >= w.WIDTH:
                posX = w.WIDTH - 1

            match event.key:
                case pygame.K_1:
                    w.theWorld.Summon(Sheep.SHEEP(posX, posY, w.theWorld), posX, posY)
                case pygame.K_2:
                    w.theWorld.Summon(Mouse.MOUSE(posX, posY, w.theWorld), posX, posY)
                case pygame.K_3:
                    w.theWorld.Summon(Snail.SNAIL(posX, posY, w.theWorld), posX, posY)
                case pygame.K_4:
                    w.theWorld.Summon(Fox.FOX(posX, posY, w.theWorld), posX, posY)
                case pygame.K_5:
                    w.theWorld.Summon(Coke.COKE(posX, posY, w.theWorld), posX, posY)
                case pygame.K_6:
                    w.theWorld.Summon(Weed.WEED(posX, posY, w.theWorld), posX, posY)
                case pygame.K_F1:
                    w.write_list()
                    w.write_map()
                case pygame.K_F2:
                    w.theWorld.organisms.clear()
                    # w.map.clear()
                    for x in range(0, w.WIDTH):
                        for y in range(0, w.HEIGHT):
                            w.theWorld.map[x][y] = None
                    a = w.read_list()
                    for i in a:
                        match type(i):
                            case Weed.WEED:
                                w.map[i.x][i.y] = Weed.WEED(i.x, i.y, w.theWorld)
                                w.theWorld.organisms.append(w.map[i.x][i.y])
                            case Coke.COKE:
                                w.map[i.x][i.y] = Coke.COKE(i.x, i.y, w.theWorld)
                                w.theWorld.organisms.append(w.map[i.x][i.y])
                            case Fox.FOX:
                                w.map[i.x][i.y] = Fox.FOX(i.x, i.y, w.theWorld)
                                w.theWorld.organisms.append(w.map[i.x][i.y])
                            case Sheep.SHEEP:
                                w.map[i.x][i.y] = Sheep.SHEEP(i.x, i.y, w.theWorld)
                                w.theWorld.organisms.append(w.map[i.x][i.y])
                            case Snail.SNAIL:
                                w.map[i.x][i.y] = Snail.SNAIL(i.x, i.y, w.theWorld)
                                w.theWorld.organisms.append(w.map[i.x][i.y])
                            case Mouse.MOUSE:
                                w.map[i.x][i.y] = Mouse.MOUSE(i.x, i.y, w.theWorld)
                        w.theWorld.organisms.append(w.map[i.x][i.y])


        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
