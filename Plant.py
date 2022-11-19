import random

import Organism as Organism

class Plant(Organism):
    spreadChance: int

    def action(self):
        self.spread()
        self.subaction()

    def spread(self):
        if random.randrange(0, 100) < self.spreadChance:
            self.world.organisms.append(type(self)(self.x, self.y, self.world))
            self.world.map[self.x][self.y] = self.world.organisms[-1]
