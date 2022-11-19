import Animal
import random


class FOX(Animal.Animal):
    image_path = "resources/lis.png"
    strength = 9
    iniciative = 5
    moveChance = 100

    def action(self):
        found = False
        while not found:
            yy = self.y + random.randrange(-1, 2)
            xx = self.x + random.randrange(-1, 2)
            if yy not in range(0, self.world.HEIGHT - 1) or xx not in range(0, self.world.WIDTH):
                continue
            if self.world.map[xx][yy] is not None:
                if self.world.map[xx][yy].strength <= self.strength:
                    self.move(xx, yy)
                    found = True
            else:
                self.move(xx, yy)
                found = True

    def move(self, x: int, y: int):
        if self.world.map[x][y] is None:
            self.world.map[self.x][self.y] = None
            self.x = x
            self.y = y
            self.world.map[self.x][self.y] = self
        else:
            self.collision(self.world.map[x][y])

    def collision(self, attacker):
        if not isinstance(attacker, type(self)):
            if attacker == self:
                return

            attackName = str(type(attacker)).split(".")[-1].split("'")[0]
            defenseName = str(type(self)).split(".")[-1].split("'")[0]
            if self.strength > attacker.strength:
                self.report(defenseName + " killed " + attackName + " at " + str(self.x) + "," + str(self.y))
                self.world.map[attacker.x][attacker.y] = None
                self.world.map[self.x][self.y] = None
                self.x = attacker.x
                self.y = attacker.y
                self.world.map[self.x][self.y] = self
                self.world.organisms.remove(attacker)
                del attacker

            else:
                self.report(attackName + " killed " + defenseName + " at " + str(self.x) + "," + str(self.y))
                self.world.map[self.x][self.y] = None
                self.world.organisms.remove(self)
                del self
        else:
            self.breed()
