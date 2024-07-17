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

    def set_coordinate(self,x:int,y:int):
        self.set_x(x)
        self.set_y(y)
    def get_coordinate(self):
        return ( self.get_x(),self.get_y() )

    def do_rotation(self):
        temp = self.get_height()
        self.set_height(self.get_width())
        self.set_width(temp)

    def draw(self,canvas,color='gray'):
        x, y = self.get_coordinate()
        width, height = self.get_width(), self.get_height()
        canvas.create_rectangle(x, y, x + width, y + height, fill=color)
    def can_be_placed(self, list_objects, x, y, bac_width, bac_height):
        from objects.Cercle import Cercle
        from objects.Triangle import Triangle
        if x < 0 or x + self.get_width() > bac_width or y < 0 or y + self.get_height() > bac_height:
            return False
        for px, py, obj in list_objects:
            if isinstance(obj, Cercle):
                if (px - obj.radius < x + self.get_width() and px + obj.radius > x and 
                    py - obj.radius < y + self.get_height() and py + obj.radius > y):
                    return False
            elif isinstance(obj,PackingObject2D):
                if (x < px + obj.width and x + self.get_width() > px and 
                    y < py + obj.height and y + self.get_height() > py):
                    return False
            elif isinstance(obj, Triangle):
                if (x < px + obj.base/2 and x + self.get_width() > px - obj.base/2 and 
                    y < py + obj.height and y + self.get_height() > py):
                    return False
        return True