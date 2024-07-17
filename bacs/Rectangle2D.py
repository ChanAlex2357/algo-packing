from .Bac2D import Bac2D

class Rectangle2D(Bac2D):
    def __init__(self,x:int,y:int, width: int, height: int, num_bac: int =1):
        super().__init__(width, height, num_bac)
        self.set_coordinate(x,y)

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
    def get_center_x(self):
        return (self.get_x() + self.get_width()) // 2
    def get_center_y(self):
        return (self.get_y() + self.get_height()) // 2
    def generate_bac(self,height:int=0,num_bac:int=0):
        if num_bac == 0:
            num_bac = self.get_num_bac()
        if height == 0:
            height = self.get_height()
        return Bac2D(self.get_width(),height,num_bac)
    
    def load_objects_from_bacs(self,bacs):
        x_base = self.get_x()
        y_base = self.get_y()
        for bac in bacs:



        
        pass