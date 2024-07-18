from bacs.Bac2D import Bac2D
from packingException import IncompatibleBacException
from objects.Cercle import Cercle
from objects.Triangle import Triangle
from objects.Rectangle import Rectangle
from objects.PackingObject2D import PackingObject2D

def brute_force(objects, canvas_width, canvas_height,last_x=0,last_y=0):
    placed_objects = []
    for obj in objects:
        placed = False

        if isinstance(obj, Triangle):
            # teste chaque rotation
            for rotation in [(obj.base, obj.get_height()), (obj.get_height(), obj.base)]:
                for x in range(last_x,canvas_width):
                    for y in range(last_y,canvas_height):
                        obj.set_height(rotation[1])
                        obj.set_width(rotation[0])
                        if obj.can_be_placed(placed_objects, x, y, canvas_width, canvas_height):
                            triangle = Triangle(rotation[0], rotation[1])
                            triangle.set_coordinate(x,y)
                            placed_objects.append(triangle)
                            placed = True
                            break
                    if placed:
                        break
                if placed:
                    break
        
        elif isinstance(obj,Cercle):
            for x in range(last_x,canvas_width):
                for y in range(last_y,canvas_height):
                    if obj.can_be_placed(placed_objects, x, y, canvas_width, canvas_height):
                        placed_objects.append(obj.set_coordinate(x,y))
                        placed = True
                        break
                if placed:
                    break

        else:
            # teste chaque rotation 
            for rotation in [(obj.get_width(), obj.get_height()), (obj.get_height(), obj.get_width())]:

                for x in range(last_x,canvas_width):
                    for y in range(last_y,canvas_height):
                        obj.set_height(rotation[1])
                        obj.set_width(rotation[0])
                        if obj.can_be_placed(placed_objects,x, y, canvas_width, canvas_height):
                            rect = Rectangle(rotation[0], rotation[1])
                            rect.set_coordinate(x,y)
                            placed_objects.append(rect)
                            placed = True
                            break
                    if placed:
                        break
                if placed:
                    break
        

        if not placed:
            print("Failed to place object:", obj)
    return placed_objects


def placer_objet(objects, bac_width, bac_height ,ref_x=0,ref_y=0):
    last_x=ref_x
    last_y=ref_y
    placed_objects = []
    for obj in objects:
        placed = False
        if isinstance(obj, Triangle):
            for rotation in [(obj.base, obj.get_height()), (obj.get_height(), obj.base)]:
                w,h = rotation
                obj.set_width(w)
                obj.set_height(h)
                if obj.can_be_placed(placed_objects, last_x, last_y, bac_width, bac_height):
                    obj.set_coordinate(last_x, last_y)
                    placed_objects.append(obj)
                    last_x += obj.base

                    if last_x >= bac_width:
                        last_x = ref_x
                        last_y += obj.get_height()
                    placed = True
                    break
        elif isinstance(obj,Cercle):
            print(">>>> Cercle")
            if obj.can_be_placed(placed_objects, last_x, last_y, bac_width, bac_height):
                obj.set_coordinate(last_x,last_y)
                placed_objects.append(obj)
                last_x += obj.radius*2
                if last_x >= bac_width:
                    last_x = ref_x
                    last_y += obj.radius*2
                placed = True
                break
        else:
            for rotation in [(obj.get_width(), obj.get_height()), (obj.get_height(), obj.get_width())]:
                w,h = rotation
                obj.set_width(w)
                obj.set_height(h)
                if obj.can_be_placed(placed_objects, last_x, last_y, bac_width, bac_height):
                    obj.set_coordinate(last_x, last_y)
                    placed_objects.append(obj)
                    last_x += obj.get_width()

                    # check si il faut changer d'etage
                    if last_x >= bac_width:
                        last_x = ref_x
                        last_y += obj.get_height()
                    placed = True
                    break

        if not placed:
            print("Failed to place object:", obj)
            last_x += obj.get_width()
            if last_x >= bac_width:
                last_x = ref_x
                last_y += obj.get_height()

    return placed_objects

