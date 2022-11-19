import random
import Organism


class Plant(Organism.Organism):
    spreadChance = 50

    def currentImage(self):
        return "resources/weed.png"