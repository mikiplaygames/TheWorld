import Animal
import random
import Plants.Coke as Coke


class MOUSE(Animal.Animal):
    strength = 2
    defaultLifeSpan = 40
    iniciative = 3
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
                f = self.GetNearestFree()
                if f is not None:
                    self.world.map[self.x][self.y] = None
                    self.x += f[0]
                    self.y += f[1]
                    self.world.map[self.x][self.y] = self
                    self.report(defenseName + " escaped " + attackName + " to " + str(self.x) + "," + str(self.y))
                else:
                    self.report(attackName + " devoured " + defenseName + " at " + str(self.x) + "," + str(self.y))
                    self.world.map[self.x][self.y] = None
                    self.world.organisms.remove(self)
                    del self
                    return
        elif attacker != self:
            self.breed(attacker)
