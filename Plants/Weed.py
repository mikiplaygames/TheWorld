import random
import Organism
import Plant


class WEED(Plant.Plant):
    strength = 1
    spreadChance = 20
    iniciative = 0
    defaultLifeSpan = 50
    lifeSpan = defaultLifeSpan

    def currentImage(self):
        if self.defaultLifeSpan * 0.4 < self.lifeSpan:
            return "resources/weed1.png"
        else:
            return "resources/weed2.png"

    def collision(self, attacker):
        if not isinstance(attacker, type(self)):
            if attacker == self:
                return

            attackName = str(type(attacker)).split(".")[-1].split("'")[0]
            defenseName = str(type(self)).split(".")[-1].split("'")[0]
            if self.strength > attacker.strength:
                self.report(defenseName + " devoured " + attackName + " at " + str(self.x) + "," + str(self.y))
                self.world.map[attacker.x][attacker.y] = None
                self.world.map[self.x][self.y] = None
                self.x = attacker.x
                self.y = attacker.y
                if attacker in self.world.organisms:
                    self.world.map[self.x][self.y] = self
                    self.world.organisms.remove(attacker)
                    del attacker

            else:
                self.report(attackName + " devoured " + defenseName + " at " + str(self.x) + "," + str(self.y))
                self.world.map[self.x][self.y] = None
                self.world.organisms.remove(self)
                del self
