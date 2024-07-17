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
        temp = self.get_height
        self.set_height(self.get_width())
        self.set_width(temp)
