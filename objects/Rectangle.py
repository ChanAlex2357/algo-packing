from Cercle import Cercle
from Triangle import Triangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def can_be_placed(self, list_objects, x, y, bac_width, bac_height):
        if x < 0 or x + self.width > bac_width or y < 0 or y + self.height > bac_height:
            return False
        for px, py, obj in list_objects:
            if isinstance(obj, Cercle):
                if (px - obj.radius < x + self.width and px + obj.radius > x and 
                    py - obj.radius < y + self.height and py + obj.radius > y):
                    return False
            elif isinstance(obj, Rectangle):
                if (x < px + obj.width and x + self.width > px and 
                    y < py + obj.height and y + self.height > py):
                    return False
            elif isinstance(obj, Triangle):
                if (x < px + obj.base/2 and x + self.width > px - obj.base/2 and 
                    y < py + obj.height and y + self.height > py):
                    return False
        return True
        