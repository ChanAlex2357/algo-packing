from bacs.Bac2D import Bac2D
import math
from objects.PackingObject2D import PackingObject2D

class Cercle(PackingObject2D):
    def __init__(self, radius):
        super().__init__(2*radius,2*radius)
        self.set_radius(radius)
    def set_radius(self , rad):
        self.radius = rad
    def get_radius(self):
        return self.radius
    def draw(self, canvas, color='red'):
        x, y = self.get_coordinate()
        radius = self.get_radius()
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
        canvas.create_text(x, y, text=f"R={radius}", fill="white")
        # print(f"Circle at coordinates: {self.get_coordinate()} with radius {self.get_radius()}")

    def can_be_placed(self, list_object, x, y, bac_width, bac_height):
        from objects.Triangle import Triangle
        if x - self.radius < 0 or x + self.radius > bac_width or y - self.radius < 0 or y + self.radius > bac_height:
            return False
        for px, py, obj in list_object:
            if isinstance(obj, Cercle):
                if math.hypot(px - x, py - y) < obj.radius + self.radius:
                    return False
            elif isinstance(obj, PackingObject2D):
                if (x + self.radius > px and x - self.radius < px + obj.width and 
                    y + self.radius > py and y - self.radius < py + obj.height):
                    return False
            elif isinstance(obj, Triangle):
                if (x + self.radius > px - obj.base/2 and x - self.radius < px + obj.base/2 and 
                    y + self.radius > py and y - self.radius < py + obj.height):
                    return False
        return True
        