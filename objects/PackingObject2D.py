from objects.PackingObject import PackingObject
class PackingObject2D (PackingObject) :
    def __init__(self,width,height):
        super().__init__(width,height)

    def get_size(self) -> int:
        return self.get_width()