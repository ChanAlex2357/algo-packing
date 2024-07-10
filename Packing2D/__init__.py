from bacs.Bac2D import Bac2D
def next_fit_decreasing_height(width,height,objects:list):
    '''
        Fait le 2D packing des objets dans des boites de taille width x hight
        Suivant l'algo Next Fit Decreasing Height (NFDH) qui consite a garder le
        dernier bac et le remplir tant que les objets sont en decreasing hheight
        ARGS :
            - la longueur des bacs
            - la hauteur des bacs
            - la liste des objets a faire entrer dans des boites
        RETURN :
            - La liste des bacs utiliser pour le packing
    '''
    bacs = []
    bac_num = 1
    bacs.append(Bac2D(width,height,bac_num))
    # 
    