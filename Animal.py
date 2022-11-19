import Organism


class Animal(Organism.Organism):

    strenght = 0


    def action(self):
        pass

    def draw(self):
        pass

    def breed(self):
        self.report(str(type(self)).split(".")[-1].split("'")[0] + " fucked")

    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.world.map[x][y] = self

    def __str__(self):
        return "Animal"

    def __repr__(self):
        return self.__str__()

    def GetStrenght(self):
        return self.strenght

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def GetWorld(self):
        return self.world

    def SetX(self, x):
        self.x = x

    def SetY(self, y):
        self.y = y

    def SetWorld(self, world):
        self.world = world

    def SetStrenght(self, strenght):
        self.strenght = strenght

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
            if neighbours[i]: # if not None
                return neighbours[i]
        # move in random direction

    def collision(self):
        pass
        # breed
