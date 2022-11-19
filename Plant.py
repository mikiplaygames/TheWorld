import random

import Organism as Organism


class Plant(Organism.Organism):
    spreadChance: int

    def action(self):
        self.spread()
        self.subaction()

    def spread(self):
        if random.randrange(0, 100) < self.spreadChance:
            randX = -1 if random.randrange(0, 2) == 0 else 1
            randY = -1 if random.randrange(0, 2) == 0 else 1
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
