import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here
class Food(Actor):
    def __init__(self):
        super().__init__()
        self._points = 0
        self.set_text("testing")
        self.reset()
    
    def get_points(self):
        return self._points

    def reset(self):
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        self.set_position(Point(x, y))