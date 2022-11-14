import Animal
import random


class FOX(Animal.Animal):
    image_path = "![](../resources/lis.png)"
    strength = 9
    iniciative = 5

    def action(self):
        found = False
        while not found:
            yy = self.y + int(random.randrange(-1, 1))
            xx = self.x + int(random.randrange(-1, 1))
            if self.world.map[xx][yy] is not None:
                if self.world.map[xx][yy].strength <= self.strength:
                    self.x = xx
                    self.y = yy
                    found = True
