from Cercle import Cercle
from Rectangle import Rectangle
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def can_be_placed(self, list_objects, x, y, bac_width, bac_height):
        if x - self.base/2 < 0 or x + self.base/2 > bac_width or y < 0 or y + self.height > bac_height:
            return False
        
        for px, py, obj in list_objects:
            if isinstance(obj, Cercle):
                if (px - obj.radius < x + self.base/2 and px + obj.radius > x - self.base/2 and 
                    py - obj.radius < y + self.height and py + obj.radius > y):
                    return False
            elif isinstance(obj, Rectangle):
                if (x < px + obj.width and x + self.base > px and 
                    y < py + obj.height and y + self.height > py):
                    return False
            elif isinstance(obj, Triangle):
                if (x < px + obj.base/2 and x + self.base > px - obj.base/2 and 
                    y < py + obj.height and y + self.height > py):
                    return False
        return True