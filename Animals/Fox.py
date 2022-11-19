import Animal
import random


class FOX(Animal.Animal):
    strength = 9
    defaultLifeSpan = 90
    lifeSpan = defaultLifeSpan
    iniciative = 5
    moveChance = 100

    def currentImage(self):
        if self.defaultLifeSpan * 0.8 < self.lifeSpan <= self.defaultLifeSpan:
            return "resources/lis1.png"
        elif self.defaultLifeSpan * 0.1 <= self.lifeSpan <= self.defaultLifeSpan * 0.8:
            return "resources/lis2.png"
        else:
            return "resources/lis3.png"

    def subaction(self):
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
                if attacker in self.world.organisms:
                    self.world.map[self.x][self.y] = self
                    self.world.organisms.remove(attacker)
                    del attacker

            else:
                self.report(attackName + " killed " + defenseName + " at " + str(self.x) + "," + str(self.y))
                self.world.map[self.x][self.y] = None
                self.world.organisms.remove(self)
                del self
        elif attacker != self:
            self.breed(attacker)
