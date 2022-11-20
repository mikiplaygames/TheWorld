import World as World


class Organism:
    image_path: str
    strength: int
    iniciative: int
    lifeSpan = 0
    moveChance: int
    x: int
    y: int
    world: World
    queueAction = False

    def action(self):
        self.subaction()

    def subaction(self):
        pass

    def collision(self, attacker):
        pass

    def report(self, message: str):
        self.world.log = self.world.log + message + "|"

    def GetOrganism(self, x, y):
        return self.world.map[x][y]

    def SetOrganism(self, x, y, organism):
        self.world.map[x][y] = organism

    def GetNearestFree(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
        for i in directions:
            x, y = i
            if 0 <= self.x + x < self.world.WIDTH and 0 <= self.y + y < self.world.HEIGHT:
                if self.world.map[self.x + x][self.y + y] is None:
                    return i

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