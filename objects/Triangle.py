from objects.PackingObject2D import PackingObject2D
class Triangle (PackingObject2D):
    def __init__(self, base, height):
        super().__init__(base,height)
        self.get_height()
    def get_base(self):
        return self.get_width()

    def draw(self,canvas,color='yellow'):
        x, y = self.get_coordinate()
        base, height = self.get_base(), self.get_height()
        points = [x, y, x + base / 2, y - height, x - base / 2, y - height]
        canvas.create_polygon(points, fill=color)
        # self.canvas.create_text(x, y - height / 2, text=f"{base}x{height}", fill="white")


    def can_be_placed(self, list_objects, x, y, bac_width, bac_height):
        if x - self.get_base()/2 < 0 or x + self.get_base()/2 > bac_width or y < 0 or y + self.get_height() > bac_height:
            return False
        
        for obj in list_objects:
            px, py = obj.get_x() , obj.get_y()
            from objects.Cercle import Cercle
            if isinstance(obj, Cercle):
                if (px - obj.get_radius() < x + self.get_base()/2 and px + obj.get_radius() > x - self.get_base()/2 and 
                    py - obj.get_radius() < y + self.get_height() and py + obj.get_radius() > y):
                    return False
            elif isinstance(obj, PackingObject2D):
                if (x < px + obj.get_width() and x + self.get_width() > px and 
                    y < py + obj.get_height() and y + self.get_height() > py):
                    return False
            elif isinstance(obj, Triangle):
                if (x < px + obj.get_base()/2 and x + self.get_width() > px - obj.get_base()/2 and 
                    y < py + obj.get_height() and y + self.get_height() > py):
                    return False
        return True