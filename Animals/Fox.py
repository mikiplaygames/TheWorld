import Animal
import random
import Plants.Coke as Coke


class FOX(Animal.Animal):
    strength = 9
    defaultLifeSpan = 80
    lifeSpan = defaultLifeSpan
    iniciative = 5
    moveChance = 100
    breedChance = 25

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
            if yy not in range(0, self.world.HEIGHT) or xx not in range(0, self.world.WIDTH):
                continue
            if self.world.map[xx][yy] is not None:
                if self.world.map[xx][yy].strength <= self.strength:
                    self.move(xx, yy)
                    found = True
                else:
                    continue
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
                self.world.map[attacker.x][attacker.y] = None
                self.world.map[self.x][self.y] = None
                self.x = attacker.x
                self.y = attacker.y
                self.world.map[self.x][self.y] = self
                if attacker in self.world.organisms:
                    self.world.organisms.remove(attacker)

                consumed = False
                if isinstance(attacker, Coke.COKE):
                    self.queueAction = True
                    self.report(defenseName + " consumed " + attackName + " at " + str(self.x) + "," + str(self.y))
                    consumed = True
                if consumed == False:
                    self.report(defenseName + " devoured " + attackName + " at " + str(self.x) + "," + str(self.y))

                del attacker


            else:
                self.report(attackName + " devoured " + defenseName + " at " + str(self.x) + "," + str(self.y))
                self.world.map[self.x][self.y] = None
                self.world.organisms.remove(self)
                del self
                return
        elif attacker != self:
            self.breed(attacker)
