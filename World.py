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

    map = []

    def NextRound(self):
        print("Proceeded to next turn")
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                if self.map[x][y] != None:
                    self.map[x][y].action()

    def RandomizeWorld(self, w: int, h: int):
        self.WIDTH = w
        self.HEIGHT = h
        self.map = [([Organism.Organism for x in range(w)]) for y in range(h)]
        for x in range(0, w):
            for y in range(0, h):
                rand = random.randrange(0, 5)
                if rand == 1:
                    self.map[x][y] = Sheep.SHEEP(x, y, self)
                elif rand == 2:
                    self.map[x][y] = Fox.FOX(x, y, self)
                else:
                    self.map[x][y] = None
