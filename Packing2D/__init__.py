from bacs.Bac2D import Bac2D
from objects.PackingObject2D import PackingObject2D
from packingException import IncompatibleBacException
def next_fit_decreasing_height(width,height,objects:list):
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
    # bacs.append(Bac2D(width,height,num_bac))


def best_fit(width, height, objects:list):
    '''
        Algorithme de packing consistant a faire rentrer les objets (width*height) dans des bacs
        en laissant la moindre surface disponible dans le bac
            - longueur des bacs
            - hauteur des bacs
            - listes des objets
        RETURN:
            - liste des bac utilisé 
    '''

    # liste des bacs
    bacs = []
    # numero du bac actuel, initialisé a 1
    num_bac = 1
    bacs.append(Bac2D(width,height,num_bac))

    for packing_object in objects:
        # Trier les bacs en fonction de la surface disponible
        bacs = sorted(bacs, key=lambda bac : bac.get_free_area(), reverse=False)
        added = False

        for bac in bacs:
            try:
                bac.add_object(packing_object)
                added = True
                break
            except IncompatibleBacException:
                added = False

            if not added:
                num_bac += 1
                new_bac = Bac2D(width,height,num_bac)
                try:
                    new_bac.add_object(packing_object)
                    bacs.append(new_bac)
                except IncompatibleBacException:
                    pass
    return bacs

        

    