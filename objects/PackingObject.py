class PackingObject :
    def __init__(self,width,height):
        self.set_width(width)
        self.set_height(height)
        self.set_numbac(0)

    def __str__(self):
        return f" W:{self.get_width()} | H:{self.get_height()} | NumBac:{self.get_numbac()} \n"
#Getteurs and Setteurs
#width
    def get_width(self) -> int:
        return self._width

    def set_width(self,width):
        self._width=width

    #height
    def get_height(self) -> int:
        return self._height

    def set_height(self,height):
        self._height=height

    #numBac
    def get_numbac(self) -> int:
        return self._numBac

    def set_numbac(self,numBac):
        self._numBac=numBac
        
    def get_size(self) -> int:
        return self.get_width() * self.get_height()