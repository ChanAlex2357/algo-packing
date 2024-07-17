from bacs.Bac2D import Bac2D
from packingException import IncompatibleBacException
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
    bacs = []       # La liste des bacs
    bac_num = 1     # Le numero du premier bac
    # Creation de la premiere bac 
    current_bac = Bac2D(width,height,bac_num)   
    current_height = current_bac.height()
    # Ajouter le bac actuelle dans la liste des bacs
    bacs.append(current_bac)
    # Determier le bac pour chaque objet
    for packing_object in objects:
        try:
            # Verifier si c'est un Decreasing height
            if packing_object.get_height() >= current_height:
                # Throws exception si c'esp pas Decreasing
                raise IncompatibleBacException
            current_bac.add_object(packing_object)
        except IncompatibleBacException:
            # Exception si l'objet ne rentre pas dans le bac ou ne suit pas le format Decreasing
            # Alors Creation d'un nouveau bac
            bac_num += 1
            current_bac = Bac2D(width,height,bac_num)
            try:
                # Ajouter l'objet 
                current_bac.add_object(packing_object)
            except IncompatibleBacException :
                # Exception si l'objet ne peut rentrer dans aucun bac
                pass
        # Le height de reference devient celui de l'objet ajoutee
        current_height = packing_object.get_height()
    return bacs
 
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
