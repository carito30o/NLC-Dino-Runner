from nlc_dino_runner.utils.constants import SMALL_CACTUS
from nlc_dino_runner.component.obstacles.obstacle import Obstacle
import random


class Cactus(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0, 2)
        super().__init__(image, self.index)
        self.rect.y = 325
