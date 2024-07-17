from bacs.Bac2D import Bac2D
from Rectangle import Rectangle
from Triangle import Triangle
import math

class Cercle:
    def __init__(self, radius):
        self.radius = radius 

    def can_be_placed(self, list_object, x, y, bac_width, bac_height):
        if x - self.radius < 0 or x + self.radius > bac_width or y - self.radius < 0 or y + self.radius > bac_height:
            return False
        for px, py, obj in list_object:
            if isinstance(obj, Cercle):
                if math.hypot(px - x, py - y) < obj.radius + self.radius:
                    return False
            elif isinstance(obj, Rectangle):
                if (x + self.radius > px and x - self.radius < px + obj.width and 
                    y + self.radius > py and y - self.radius < py + obj.height):
                    return False
            elif isinstance(obj, Triangle):
                if (x + self.radius > px - obj.base/2 and x - self.radius < px + obj.base/2 and 
                    y + self.radius > py and y - self.radius < py + obj.height):
                    return False
        return True
        