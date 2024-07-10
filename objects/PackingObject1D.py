from objects.PackingObject import PackingObject
class PackingObject1D (PackingObject) :
    def __init__(self,taille):
        super().__init__(taille,taille)
    
    def get_size(self) -> int:
        return self.get_width()