from objects import PackingObject
from packingException import IncompatibleBacException
class Bac :
    def __init__(self,width:int,height:int,numBac:int):
        self.set_width(width)
        self.set_height(height)
        self.set_free_space(width*height)
        self.set_num_bac(numBac)
        self.set_objects(list())
    #Getteurs and Setteurs
    #width
    def get_width(self) -> int :
        return self._width

    def set_width(self,width):
        self._width=width

    #height
    def get_height(self) -> int:
        return self._height

    def set_height(self,height):
        self._height=height

    #free_space
    def get_free_space(self) -> int:
        return self._free_space

    def set_free_space(self,free_space):
        self._free_space=free_space

    #objects
    def get_objects(self) -> list:
        return self._objects

    def set_objects(self,objects):
        self._objects=objects

    #num_bac
    def get_num_bac(self) -> int:
        return self._num_bac

    def set_num_bac(self,num_bac):
        self._num_bac=num_bac

    # Functions
    def check_free_space(self,obj:PackingObject):
        raise IncompatibleBacException()

    def add_object(self,obj:PackingObject):
        '''
            Ajoute un objet dans le bac
        '''
        self.check_free_space(obj)
        # ajouter dans la liste des objets
        self.get_objects().append(obj)
        # Designer le bac avec son num dans l'objet ajouter
        obj.set_numbac( self.get_num_bac())
