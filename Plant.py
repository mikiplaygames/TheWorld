import random

import Organism as Organism


class Plant(Organism.Organism):
    spreadChance: int
    lifeSpan: int

    def action(self):
        self.lifeSpan -= 1
        if self.lifeSpan <= 0:
            self.world.map[self.x][self.y] = None
            self.world.organisms.remove(self)
            self.report(str(type(self)).split(".")[-1].split("'")[0] + " withered away at " + str(self.x) + "," + str(self.y))
            del self
        else:
            self.subaction()

    def subaction(self):
        self.spread()

    def spread(self):
        if random.randrange(0, 100) < self.spreadChance and self.lifeSpan > self.defaultLifeSpan * 0.4:
            randX = random.randrange(-1, 2)
            randY = random.randrange(-1, 2)
            if randX == 0 and randY == 0:
                return
            if 0 <= self.x + randX < self.world.WIDTH and 0 <= self.y + randY < self.world.HEIGHT:
                if self.world.map[self.x + randX][self.y + randY] is not None:
                    return
                else:
                    self.world.organisms.append(type(self)(self.x + randX, self.y + randY, self.world))
                    self.world.map[self.x][self.y] = self.world.organisms[-1]

    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.world.map[x][y] = self
