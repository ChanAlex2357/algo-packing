from bacs.Bac1D import Bac1D
from objects.PackingObject1D import PackingObject1D
from packingException import IncompatibleBacException

def worst_fit( B:int , objects:list):
    '''
        Insérer chaque objet dans le bac qui laissera le plus d’espace restant après
        insertion
        Les objets seront associes directement a un bac a par l'attribut num_bac , et ajouter au liste des objets de bac

        ARGS:
            - B : la longueur des bacs sur un axe
            - objects : la liste des objets a inserer correspondant a une taille si chacun
        RETURN : 
            - La liste des bacs utiliser pour faire le packing
    '''
    # la liste des bacs
    bacs = []
    # Initialiser avec le bac numero 1
    num_bac = 1
    bacs.append(Bac1D(B,num_bac))
    for packing_object in objects:
        bacs = sorted(bacs,key=lambda bac : bac.get_free_space(),reverse=True)
        added = False
        for bac in bacs:
            try:
                bac.add_object(packing_object)
                added = True
                break
            except IncompatibleBacException :
                added = False
        if not added :
            num_bac+=1
            new_bac = Bac1D(B,num_bac)
            try:
                new_bac.add_object(packing_object)
                bacs.append(new_bac)
            except IncompatibleBacException :
                # Exception si l'objet ne peut entrer dans aucune bac
                pass
    return bacs

def best_fit(B: int, objects: list):
    '''
        Insérer chaque objet dans le bac qui laissera le moins d’espace restant après
        insertion
        Les objets seront associes directement a un bac a par l'attribut num_bac , et ajouter au liste des objets de bac

        ARGS:
            - B : la longueur des bacs sur un axe
            - objects : la liste des objets a inserer correspondant a une taille si chacun
        RETURN : 
            - La liste des bacs utiliser pour faire le packing
    '''
    # la liste des bacs
    bacs = []
    # Initialiser avec le bac numero 1
    num_bac = 1
    bacs.append(Bac1D(B,num_bac))
    for packing_object in objects:
        bacs = sorted(bacs,key=lambda bac : bac.get_free_space(),reverse=False)
        added = False
        for bac in bacs:
            try:
                bac.add_object(packing_object)
                added = True
                break
            except IncompatibleBacException :
                added = False
        if not added :
            num_bac+=1
            new_bac = Bac1D(B,num_bac)
            try:
                new_bac.add_object(packing_object)
                bacs.append(new_bac)
            except IncompatibleBacException :
                # Exception si l'objet ne peut entrer dans aucune bac
                pass
    return bacs

def brute_force(B:int , objects:list):
    print("Brute force")