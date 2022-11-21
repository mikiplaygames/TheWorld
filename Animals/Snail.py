import Animal
import random
import Plants.Coke as Coke


class SNAIL(Animal.Animal):
    strength = 3
    defaultLifeSpan = 120
    iniciative = 1
    lifeSpan = defaultLifeSpan
    moveChance = 10
    breedChance = 100

    def currentImage(self):
        if self.defaultLifeSpan * 0.8 < self.lifeSpan <= self.defaultLifeSpan:
            return "resources/snail1.png"
        elif self.defaultLifeSpan * 0.1 <= self.lifeSpan <= self.defaultLifeSpan * 0.8:
            return "resources/snail2.png"
        else:
            return "resources/snail3.png"

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

                consumed = True
                if isinstance(attacker, Coke.COKE):
                    self.queueAction = True
                    self.report(defenseName + " consumed " + attackName + " at " + str(self.x) + "," + str(self.y))
                    consumed = True
                if consumed == False:
                    self.report(defenseName + " devoured " + attackName + " at " + str(self.x) + "," + str(self.y))

                del attacker

            elif attacker.strength < 2:
                return
            elif attacker.strength > 4:
                if random.randrange(1, 101) < 61:
                    return
                else:
                    self.report(attackName + " devoured " + defenseName + " at " + str(self.x) + "," + str(self.y))
                    self.world.map[self.x][self.y] = None
                    self.world.organisms.remove(self)
                    del self
                    return
            else:
                self.report(attackName + " devoured " + defenseName + " at " + str(self.x) + "," + str(self.y))
                self.world.map[self.x][self.y] = None
                self.world.organisms.remove(self)
                del self
                return

        elif attacker != self:
            self.breed(attacker)
