from bacs.Bac2D import Bac2D
def NextFitDecreasingHeight(width,height,objects:list):
    '''
        Fait le 2D packing des objets dans des boites de taille width x hight
        ARGS :
            - la longueur des bacs
            - la hauteur des bacs
            - la liste des objets a faire entrer dans des boites
        RETURN :
            - La liste des bacs utiliser pour le packing
    '''
    bacs = []
    bac_num = 1
    bacs.append(Bac2D(width,height,num_bac))
    