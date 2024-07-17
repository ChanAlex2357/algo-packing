from bacs.Bac import Bac
from objects.PackingObject2D import PackingObject2D 
from packingException import IncompatibleBacException

class Bac2D  (Bac) :
    def __init__(self,width:int,height:int , num_bac:int):
        super().__init__(width,height,num_bac)
        self.set_free_height(height)
        self.set_free_width(width)

#Functions
    #free_width
    def get_free_width(self):
        return self._free_width

    def set_free_width(self,free_width):
        self._free_width=free_width

    #free_height
    def get_free_height(self) -> int:
        return self._free_height

    def set_free_height(self,free_height) -> int:
        self._free_height=free_height

    def check_free_space(self,obj:PackingObject2D):
        # Verifier si l'objet peut entrer en hauteur et en largeur
        if (obj.get_height() > self.get_free_height()) or (obj.get_width() > self.get_free_width()):
            raise IncompatibleBacException()

    def add_object(self,obj:PackingObject2D):
        super().add_object(obj)
        # Mettre a jour les espaces libres
        reste_height = self.get_free_height() - obj.get_height()
        reste_width = self.get_free_width() - obj.get_width()

        self.set_free_height(reste_height)
        self.set_free_width(reste_width)

    def get_free_area(self):
        return self.get_free_height() * self.get_free_width()
    


