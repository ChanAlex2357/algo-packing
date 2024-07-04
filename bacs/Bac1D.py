from bacs.Bac import Bac
from objects import PackingObject1D
from packingException import IncompatibleBacException

class Bac1D  (Bac) :
    def __init__(self,taille:int , num_bac:int):
        super().__init__(taille,taille,num_bac)
        self.set_free_space(taille)
#Functions
    def check_free_space(self,obj:PackingObject1D):
        free_space = self.get_free_space()
        object_size = obj.get_size()
        
        if ( free_space - object_size ) < 0 :
            raise IncompatibleBacException()
           
    def add_object(self,obj:PackingObject1D):
        super().add_object(obj)
        # Mettre a jour
        self.set_free_space(self.get_free_space() - obj.get_size())