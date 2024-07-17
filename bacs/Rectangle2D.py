from .Bac2D import Bac2D

class Rectangle2D(Bac2D):
    def __init__(self,x,y, width: int, height: int, num_bac: int):
        super().__init__(width, height, num_bac)
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
        return self.get_x(),self.get_y()