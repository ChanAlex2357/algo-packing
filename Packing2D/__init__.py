from bacs.Bac2D import Bac2D
from bacs.Rectangle2D import Rectangle2D
from objects.PackingObject2D import PackingObject2D
from packingException import IncompatibleBacException

def place_object(bac:Bac2D,packing_object:PackingObject2D,x,y,fw=True,fh=False) -> int:
    bac.add_object(packing_object,fw,fh)
    # Attribuer un coordonne a l'objet
    packing_object.set_coordinate(x,y)
    # Retourner les nouvelles coordonnees de base
    return change_x_base(x,packing_object)

def change_x_base(x,packing_object:PackingObject2D)->int:
    x += packing_object.get_width()
    return x 

def change_y_base(y,packing_object:PackingObject2D):
    return y + packing_object.get_height()

def next_fit_placement(rectangle:Rectangle2D,packing_object:PackingObject2D,current_height,x,y,fw=True,fh=False):
    # Verifier si c'est un Decreasing height
    if packing_object.get_height() >= current_height:
        # Throws exception si c'esp pas Decreasing
        packing_object.unplaced()
        packing_object.set_coordinate(0,0)
        raise IncompatibleBacException
    # Placement de l'objet
    x = place_object(rectangle,packing_object,x,y,fh=fh)
    return x 
def next_fit_decreasing_height(objects:list,rectangle:Rectangle2D=Rectangle2D(0,0,1280,720)):
    '''
        Fait le 2D packing des objets dans des boites de taille width x hight
        Suivant l'algo Next Fit Decreasing Height (NFDH) qui consite a garder le
        dernier bac et le remplir tant que les objets sont en decreasing height
        ARGS :
            - la longueur des bacs
            - la hauteur des bacs
            - la liste des objets a faire entrer dans des boites
        RETURN :
            - La liste des bacs utiliser pour le packing
    '''
    # Coordonnee de depart sur le coin du rectangle
    x,y = rectangle.get_coordinate()
    bac_num = 1     # Le numero du premier bac 
    # La hauteur de reference
    current_height = rectangle.get_height()
    # L'objet de base de la reference
    base_object = None
    # on change le la hauteur libre
    fh = True

    # Determier le bac pour chaque objet
    for packing_object in objects:
        try:
            x = next_fit_placement(rectangle,packing_object,current_height,x,y,fh=fh)
            if fh :
                base_object = packing_object
                fh = False
            # Le height de reference devient celui de l'objet ajoutee
            current_height = packing_object.get_height()
        except IncompatibleBacException:
            # Exception si l'objet ne rentre pas dans le bac ou ne suit pas le format Decreasing
            # Alors Creation d'un nouveau bac
            bac_num += 1
            rectangle.reset_free_width()
            current_height = rectangle.get_free_height()
            x = rectangle.get_x()
            y = change_y_base(y,base_object)
            fh = True

            try:
                x = next_fit_placement(rectangle,packing_object,current_height,x,y,fh=fh)
                if fh :
                    base_object = packing_object
                    fh = False
                # Le height de reference devient celui de l'objet ajoutee
                current_height = packing_object.get_height()
            except IncompatibleBacException :
                # Exception si l'objet ne peut rentrer dans aucun bac
                packing_object
        
    return objects
 
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

def first_fit_decreasing_height(width, height, objects):
    '''
    Place les objets rectangulaires dans des boîtes de taille width x height
    en utilisant l'algorithme First Fit Decreasing Height (FFDH).
    
    ARGS :
        - width : largeur des boîtes
        - height : hauteur des boîtes
        - objects : liste des objets à placer dans les boîtes (doivent être triés par hauteur décroissante)
        
    RETURN :
        - La liste des bacs utilisés pour le packing
    '''
    # Tri des objets par hauteur décroissante
    objects_sorted = sorted(objects, key=lambda obj: obj.get_height(), reverse=True)
    
    bacs = []               # Liste des bacs utilisés
    current_bac_num = 1     # Numéro du premier bac
    
    # Création du premier bac
    current_bac = Bac2D(width, height, current_bac_num)
    bacs.append(current_bac)
    
    for obj in objects_sorted:
        try:
            # Ajouter l'objet au bac courant
            current_bac.add_object(obj)
        except IncompatibleBacException:
            # Si l'objet ne peut pas être ajouté au bac courant, créer un nouveau bac
            current_bac_num += 1
            current_bac = Bac2D(width, height, current_bac_num)
            try:
                current_bac.add_object(obj)
            except IncompatibleBacException:
                # Gérer le cas où l'objet ne peut être ajouté à aucun bac
                pass
    
    return bacs

def brute_force(width, height, objects:list):
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
        added = False

        for bac in bacs:
            try:
                bac.add_object(packing_object,true,false)
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

def brute_force_with_Rotation(width, height, objects:list):
