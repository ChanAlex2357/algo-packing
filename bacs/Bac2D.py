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
    #reset free
    def reset_free_height(self) -> int:
        self._free_height=self.get_height()

    def reset_free_width(self):
        self._free_width=self.get_width()

    def check_free_space(self,obj:PackingObject2D,fw=False,fh=False):
        if fh :
            self.check_placement_height(obj)
            self.add_on_height(obj)
        if fw :
            self.check_placement_width(obj)
            self.add_on_width(obj)

    def check_placement_width(self,obj:PackingObject2D):
        # Verifier si l'objet peut entrer en hauteur et en largeur
        if (obj.get_height() > self.get_height()) or (obj.get_width() > self.get_free_width()):
            print(f"W : {obj.get_width()} ; H : {obj.get_height()}\nREF W :{self.get_free_width()} ; REF H : {self.get_height()}\nCOMPARAISON: > ; >")
            raise IncompatibleBacException()
    
    def check_placement_height(self,obj:PackingObject2D):
        # Verifier si l'objet peut entrer en hauteur et en largeur
        if (obj.get_height() > self.get_free_height()) or (obj.get_width() > self.get_width()):
            print(f"W : {obj.get_width()} ; H : {obj.get_height()}\nREF W :{self.get_width()} ; REF H : {self.get_free_height()}\nCOMPARAISON: > ; >")
            raise IncompatibleBacException()

    def add_on_height(self, obj:PackingObject2D):
        reste_height = self.get_free_height() - obj.get_height()
        self.set_free_height(reste_height)

    def add_on_width(self,obj:PackingObject2D):
        reste_width = self.get_free_width() - obj.get_width()
        self.set_free_width(reste_width)
    
    def get_free_area(self):
        return self.get_free_height() * self.get_free_width()
    

    

    def add_object(self,obj:PackingObject2D,fw:bool=False,fh:bool=False):
        if not fw and not fh:
            raise Exception("Vous n'avez specifiez aucun changement dans la taille du bac2D lors de l'ajout d'objet")
        # Mettre a jour les espaces libres
        self.check_free_space(obj,fw,fh)
        super().add_object(obj,False)

    def reset_free_space(self):
        pass

    def get_free_area(self):
        return self.get_free_height() * self.get_free_width()
    