import random


class WORLD:

    organisms = []
    map = []

    def NextRound(self):
        print("Proceeded to next turn")

    def RandomizeWorld(self, w: int, h: int):
        self.map = [[0 for x in range(w)] for y in range(h)]
        for x in range(0, w):
            for y in range(0, h):
                rand = random.randrange(0, 5)
                if rand == 1:
                    self.map[x][y]# = SHEEP(x, y, self)
                elif rand == 2:
                    self.map[x][y]# = LION(x, y, self)
                else:
                    self.map[x][y]# = 0