from nlc_dino_runner.component.power_up.hammer.hammer import Hammer
from nlc_dino_runner.utils.constants import HAMMER, HAMMER_TYPE


class Army(Hammer):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)