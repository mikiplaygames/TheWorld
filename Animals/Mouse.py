import Animal
import random


class MOUSE(Animal.Animal):
    strength = 2
    defaultLifeSpan = 40
    lifeSpan = defaultLifeSpan
    moveChance = 90
    breedChance = 50

    def currentImage(self):
        if self.defaultLifeSpan * 0.8 < self.lifeSpan <= self.defaultLifeSpan:
            return "resources/mous1.png"
        elif self.defaultLifeSpan * 0.1 <= self.lifeSpan <= self.defaultLifeSpan * 0.8:
            return "resources/mous2.png"
        else:
            return "resources/mous3.png"

    def subaction(self):
        if random.randrange(1, 101) <= self.moveChance:
            yy = self.y + random.randrange(-1, 2)
            xx = self.x + random.randrange(-1, 2)
            if yy in range(0, self.world.HEIGHT) and xx in range(0, self.world.WIDTH):
                if self.world.map[xx][yy] is None:
                    self.world.map[self.x][self.y] = None
                    self.x = xx
                    self.y = yy
                    self.world.map[xx][yy] = self
                else:
                    self.collision(self.world.map[xx][yy])

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
            elif self.strength < attacker.strength:
                f = self.GetNearestFree()
                if f is not None:
                    self.world.map[self.x][self.y] = None
                    self.x = f[0]
                    self.y = f[1]
                    self.world.map[f[0]][f[1]] = self

            else:
                self.report(attackName + " killed " + defenseName + " at " + str(self.x) + "," + str(self.y))
                self.world.map[self.x][self.y] = None
                self.world.organisms.remove(self)
                del self
        elif attacker != self:
            self.breed(attacker)