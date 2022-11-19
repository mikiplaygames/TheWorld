import random
import Organism


class Animal(Organism.Organism):
    strenght = 0
    lifeSpan = 0

    def action(self):
        self.lifeSpan -= 1
        if self.lifeSpan == 0:
            self.world.map[self.x][self.y] = None
            self.world.organisms.remove(self)
            del self
            return
        else:
            self.subaction()

    def subaction(self):
        pass

    def draw(self):
        pass

    def breed(self, attacker):
        rand = random.randrange(0, 10)
        if rand < 2 and self.lifeSpan <= self.defaultLifeSpan * 0.8:
            self.report(str(type(self)).split(".")[-1].split("'")[0] + " created a child")
            self.world.organisms.append(type(self)(self.x, self.y, self.world))
            self.world.map[self.x][self.y] = self.world.organisms[-1]
        else:
            self.report(str(type(self)).split(".")[-1].split("'")[0] + " got railed")

    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.world.map[x][y] = self

    def __str__(self):
        return "Animal"

    def __repr__(self):
        return self.__str__()

    def GetOrganism(self, x, y):
        return self.world.map[x][y]

    def SetOrganism(self, x, y, organism):
        self.world.map[x][y] = organism

    def GetNeighbours(self):
        neighbours = []
        if self.x > 0:
            if self.y > 0:
                neighbours.append(self.world.map[self.x - 1][self.y - 1])
            neighbours.append(self.world.map[self.x - 1][self.y])
            if self.y < self.world.HEIGHT - 1:
                neighbours.append(self.world.map[self.x - 1][self.y + 1])

        if self.y > 0:
            neighbours.append(self.world.map[self.x][self.y - 1])
        if self.y < self.world.HEIGHT - 1:
            neighbours.append(self.world.map[self.x][self.y + 1])

        if self.x < self.world.WIDTH - 1:
            if self.y > 0:
                neighbours.append(self.world.map[self.x + 1][self.y - 1])
            neighbours.append(self.world.map[self.x + 1][self.y])
            if self.y < self.world.HEIGHT - 1:
                neighbours.append(self.world.map[self.x + 1][self.y + 1])

        return neighbours

    def GetNeighbour(self):
        neighbours = self.GetNeighbours()
        for i in range(0, len(neighbours)):
            if neighbours[i]:  # if not None
                return neighbours[i]
        # move in random direction

    def collision(self):
        pass
        # breed
