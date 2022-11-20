import random
import Organism


class Animal(Organism.Organism):
    defaultBreedCooldown = 20
    breedCooldown = defaultBreedCooldown
    strenght = 0
    lifeSpan = 0
    breedChance: int

    def action(self):
        if self.breedCooldown < self.defaultBreedCooldown:
            self.breedCooldown -= 1
        if self.breedCooldown <= 0:
            self.breedCooldown = self.defaultBreedCooldown
        self.lifeSpan -= 1
        if self.lifeSpan == 0:
            self.world.map[self.x][self.y] = None
            self.world.organisms.remove(self)
            del self
            return
        else:
            self.subaction()
            if self.queueAction:
                self.queueAction = False
                self.subaction()

    def subaction(self):
        pass

    def draw(self):
        pass

    def breed(self, attacker):
        if self.breedCooldown == self.defaultBreedCooldown:
            rand = random.randrange(1, 101)
            if rand <= self.breedChance and self.lifeSpan <= self.defaultLifeSpan * 0.8:
                f = self.GetNearestFree()
                if f is not None:
                    x = f[0]
                    y = f[1]
                    self.report(str(type(self)).split(".")[-1].split("'")[0] + " created a child at " + str(self.x) + "," + str(self.y))
                    self.breedCooldown -= 1
                    self.world.organisms.append(type(self)(self.x + x, self.y + y, self.world))
                    self.world.map[self.x + x][self.y + y] = self.world.organisms[-1]
                else:
                    self.report(str(type(self)).split(".")[-1].split("'")[0] + "'s child was obliterated at " + str(self.x) + "," + str(self.y))
            else:
                self.report(str(type(self)).split(".")[-1].split("'")[0] + " got finessed at " + str(self.x) + "," + str(self.y))

    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.world.map[x][y] = self

    def __str__(self):
        return "Animal"

    def __repr__(self):
        return self.__str__()

    def collision(self):
        pass
        # breed
