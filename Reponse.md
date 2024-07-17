# 1D-packing
## 2-4-2
    Pour chaque algorithme de placement énoncé ci-dessus, trouver un exemple de données d’entrées
    pour lequel l’algorithme ne donne pas la solution optimale c’est-à-dire il utilise plus de bac que
    nécessaire.
### First-fit
Limitation:
L'algorithme ne prend pas en compte l'utilisation globale de l'espace et peut laisser des espaces inutilisés dans les conteneurs, ce qui entraîne une utilisation inefficace des conteneurs disponibles.

Exemple: 
Objets : [8, 7, 6, 5, 4]
Taille des conteneurs : 10

### Best fit
Limitation:
Essaie de minimiser l'espace restant, mais peut créer des situations où de petits espaces inutilisables s'accumulent, empêchant l'ajout optimal de futurs objets.

Exemple:
Objets : [8, 6, 5, 5]
Taille des conteneurs : 10

### Worst fit
Limitation:
Peut répartir les objets de manière trop dispersée, en plaçant des objets dans de nouveaux conteneurs même si des espaces suffisants existent dans d'autres conteneurs, entraînant une fragmentation excessive.

Exemple:
Objets : [8, 5, 5, 3, 3]
Taille des conteneurs : 10

# 2D Packing
## Next fit decreasing height
L'algorithme place les objets sequentiellement sur l'etage actuel en placant les objets de hauteur plus grande en premier jusqu'a ce que ça ne rentre plus, et passe a l'etage suivant

## Best fit
Consiste a placer l'objet dans l'etage avec le moins de surface possible restant

## First fit decreasing height
L'algorithme place les objets sequentiellement sur le premier etage où il peut rentrer en placant les elements plus grand en hauteur en premier

## 
