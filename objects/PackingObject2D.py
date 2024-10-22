from objects.PackingObject import PackingObject

class PackingObject2D (PackingObject) :
    def __init__(self,width,height):

        super().__init__(width,height)
        self.set_coordinate(0,0)

    def set_x(self,x:int):
        self._x = x
    def get_x(self):
        return self._x
    
    def set_y(self,y:int):
        self._y = y
    def get_y(self):
        return self._y
    def get_center_x(self):
        return (self.get_x() + self.get_width()) / 2
    def get_center_y(self):
        return (self.get_y() + self.get_height()) / 2

    def set_coordinate(self,x:int,y:int):
        self.set_x(x)
        self.set_y(y)
    def get_coordinate(self):
        return ( self.get_x(),self.get_y() )

    def do_rotation(self):
        print("rotated")
        temp = self.get_height()
        self.set_height(self.get_width())
        self.set_width(temp)

    def draw(self,canvas,color='gray'):
        x, y = self.get_coordinate()
        width, height = self.get_width(), self.get_height()
        canvas.create_rectangle(x, y, x + width, y + height, fill=color)
        # canvas.create_text(self.get_center_x(), self.get_center_y(), text=f"{width}x{height}", fill="white")

    def can_be_placed(self, list_objects, x, y, bac_width, bac_height,bac_x,bac_y):
        from objects.Cercle import Cercle
        from objects.Triangle import Triangle
        if x < bac_x or x + self.get_width() > bac_x+bac_width or y < bac_y or y + self.get_height() > bac_y+bac_height:
            return False
        for obj in list_objects:
            px, py = obj.get_x() , obj.get_y()
            # if isinstance(obj, Cercle):
            #     if (px + obj.get_width() < x + self.get_width() and px + obj.get_width() > x and py < y + self.get_height() and py + obj.get_radius() > y):
            #         return False
            # elif isinstance(obj, Triangle):
            #     if (x < px + obj.get_width() and x + self.get_width() > px - obj.get_base()/2 and y < py + obj.get_height() and y + self.get_height() > py):
            #         return False
            # elif isinstance(obj,PackingObject2D):
            if (x < px + obj.get_width() and x + self.get_width() > px and y < py + obj.get_height() and y + self.get_height() > py):
                return False
        return True