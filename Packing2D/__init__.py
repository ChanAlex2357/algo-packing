from bacs.Bac2D import Bac2D
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

def First_Fit_Decreasing_Height(width, height, objects):
    '''
        Minimiser la hauteur totale utilisée dans une zone 2D en plaçant 
        les objets rectangulaires de manière à utiliser efficacement l'espace disponible.
        ARGS :
            - la longueur des bacs
            - la hauteur des bacs
            - la liste des objets à faire entrer dans des boites
        RETURN :
            - La liste des bacs utilisés pour le packing
    '''
    objects.sort(key=lambda obj: obj.get_height(), reverse=True)  # Trier les objets par hauteur décroissante
    bacs = []
    bac_num = 1

    for obj in objects:
        placed = False
        for bac in bacs:
            if bac.can_place(obj[0], obj[1]):
                bac.place(obj[0], obj[1])
                placed = True
                break
        if not placed:
            new_bac = Bac2D(width, height, bac_num)
            new_bac.place(obj[0], obj[1])
            bacs.append(new_bac)
            bac_num += 1

    return bacs


    