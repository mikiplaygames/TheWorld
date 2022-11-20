import World as World


class Organism:
    image_path: str
    strength: int
    iniciative: int
    lifeSpan = 0
    moveChance: int
    x: int
    y: int
    world: World

    def action(self):
        self.subaction()

    def subaction(self):
        pass

    def collision(self, attacker):
        pass

    def report(self, message: str):
        self.world.log = self.world.log + message + "|"
