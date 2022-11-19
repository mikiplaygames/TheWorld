import Animal
import random

class SHEEP(Animal.Animal):
    image_path = "resources/shep.png"
    strength = 4
    iniciative = 4
    moveChance = 50

    def action(self):
        if random.randrange(1, 101) <= self.moveChance:
            yy = self.y + random.randrange(-1, 2)
            xx = self.x + random.randrange(-1, 2)
            if yy in range(0, self.world.HEIGHT - 1) and xx in range(0, self.world.WIDTH):
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
            if self.strength > attacker.strength:
                self.report(str(self) + " killed " + str(attacker))
                self.world.map[attacker.x][attacker.y] = None
                self.world.map[self.x][self.y] = None
                self.x = attacker.x
                self.y = attacker.y
                self.world.map[self.x][self.y] = self
                self.world.organisms.remove(attacker)
                del attacker

            else:
                self.report(str(attacker) + " killed " + str(self))
                self.world.map[self.x][self.y] = None
                self.world.organisms.remove(self)
                del self
        else:
            self.breed()

