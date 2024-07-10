from bacs.Bac import Bac
from objects import PackingObject1D
from packingException import IncompatibleBacException

class Bac2D  (Bac) :
    def __init__(self,width:int,height:int , num_bac:int):
        super().__init__(width,height,num_bac)
#Functions
    def check_free_space(self,obj:PackingObject1D):
        pass

    def add_object(self,obj:PackingObject1D):
        super().add_object(obj)
        # Mettre a jour