import Animal
import random
import Plants.Coke as Coke
import Plants.Weed as Weed


class SHEEP(Animal.Animal):
    strength = 4
    defaultLifeSpan = 130
    lifeSpan = defaultLifeSpan
    iniciative = 4
    moveChance = 50
    breedChance = 50

    def currentImage(self):
        if self.defaultLifeSpan * 0.8 < self.lifeSpan <= self.defaultLifeSpan:
            return "resources/shep1.png"
        elif self.defaultLifeSpan * 0.1 <= self.lifeSpan <= self.defaultLifeSpan * 0.8:
            return "resources/shep2.png"
        else:
            return "resources/shep3.png"

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
                    self.lifeSpan += 1
                    consumed = True
                if isinstance(attacker, Weed.WEED):
                    self.lifeSpan += 1
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
        elif attacker != self:
            self.breed(attacker)
