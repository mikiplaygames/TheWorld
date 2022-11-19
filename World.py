import array
import random

import Animal
import Animals.Sheep as Sheep
import Animals.Fox as Fox
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
        for i in self.organisms:
            if i != None:
                i.action()

    def RandomizeWorld(self, w: int, h: int):
        self.WIDTH = w
        self.HEIGHT = h
        self.map = [([Organism.Organism for x in range(w)]) for y in range(h)]

        for x in range(0, w):
            for y in range(0, h):
                self.map[x][y] = None
        """
        for i in range(0, 8):
            self.map[i][i] = Sheep.SHEEP(i, i, self)
            self.organisms.append(self.map[i][i])
        """
        for x in range(0, w):
            for y in range(0, h):
                rand = random.randrange(0, 1000)
                if rand < 25:
                    self.map[x][y] = Sheep.SHEEP(x, y, self)
                elif 24 < rand < 28:
                    self.map[x][y] = Fox.FOX(x, y, self)
                else:
                    self.map[x][y] = None
                self.organisms.append(self.map[x][y])