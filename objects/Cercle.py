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
        canvas.create_oval(x, y, x+self.get_width(), y+self.get_height(), fill=color)
        canvas.create_text(x+self.get_radius(), y+self.get_radius(), text=f"R={radius}", fill="white")
        # print(f"Circle at coordinates: {self.get_coordinate()} with radius {self.get_radius()}")

    # def can_be_placed(self, list_object, x, y, bac_width, bac_height):
    #     from objects.Triangle import Triangle
    #     if x - self.get_radius() < 0 or x + self.get_radius() > bac_width or y - self.get_radius() < 0 or y + self.get_radius() > bac_height:
    #         return False
    #     for obj in list_object:
    #         px, py = obj.get_width() , obj.get_height()
    #         if isinstance(obj, Cercle):
    #             if math.hypot(px - x, py - y) < obj.get_radius() + self.get_radius():
    #                 return False
    #         elif isinstance(obj, Triangle):
    #             if (x + self.get_radius() > px - obj.get_base()/2 and x - self.get_radius() < px + obj.get_base()/2 and y + self.get_radius() > py and y - self.get_radius() < py + obj.get_height()):
    #                 return False
    #         elif isinstance(obj, PackingObject2D):
    #             if (x + self.get_radius() > px and x - self.get_radius() < px + obj.get_width() and y + self.get_radius() > py and y - self.get_radius() < py + obj.get_height()):
    #                 return False
    #     return True
        