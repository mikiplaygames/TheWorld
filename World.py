import array
import random

import Animal
import Animals.Sheep as Sheep
import Animals.Fox as Fox
import Plants.Weed as Weed
import Plants.Coke as Coke
import Animals.Snail as Snail
import Animals.Mouse as Mouse
import Organism as Organism


class WORLD:
    WIDTH: int
    HEIGHT: int
    organisms = []
    rangeX: int
    rangeH: int

    log: str = ""

    map = []

    def NextRound(self):
        self.organisms.sort(key=lambda x: x.iniciative, reverse=True)
        for i in self.organisms:
            if i is not None:
                i.action()

    def Summon(self, org, posX: int, posY: int):

        self.map[posX][posY] = org
        self.organisms.append(self.map[posX][posY])

        self.log += "Summoned " + str(type(self.map[posX][posY])).split(".")[-1].split("'")[0] + "|"

    def RandomizeWorld(self, w: int, h: int):
        self.WIDTH = w
        self.HEIGHT = h
        self.map = [([Organism.Organism for x in range(h)]) for y in range(w)]

        for x in range(0, w):
            for y in range(0, h):
                self.map[x][y] = None

        for x in range(0, w):
            for y in range(0, h):
                rand = random.randrange(0, 600)
                if rand < 25:
                    self.map[x][y] = Sheep.SHEEP(x, y, self)
                elif 24 < rand < 30:
                    self.map[x][y] = Fox.FOX(x, y, self)
                elif 30 <= rand < 45:
                    self.map[x][y] = Weed.WEED(x, y, self)
                elif 45 <= rand < 55:
                    self.map[x][y] = Snail.SNAIL(x, y, self)
                elif 55 <= rand < 65:
                    self.map[x][y] = Mouse.MOUSE(x, y, self)
                elif 65 <= rand < 69:
                    self.map[x][y] = Coke.COKE(x, y, self)
                else:
                    self.map[x][y] = None

                if self.map[x][y] is not None:
                    self.organisms.append(self.map[x][y])
