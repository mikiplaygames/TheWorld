import World as World

class Organism:

    image_path: str
    strength: int
    iniciative: int
    moveChance: int
    x: int
    y: int
    world: World

    def action(self):
        pass

    def collision(self, attacker):
        pass

    def report(self,  message: str):
        # self.world.log.message(message)
        pass