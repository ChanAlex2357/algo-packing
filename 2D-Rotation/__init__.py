from bacs.Bac2D import Bac2D
from packingException import IncompatibleBacException
from objects.Cercle import Cercle
from objects.Triangle import Triangle
from objects.Rectangle import Rectangle

def brute_force(objects, canvas_width, canvas_height):
    placed_objects = []
    for obj in objects:
        placed = False

        if isinstance(obj, Rectangle):
            # teste chaque rotation 
            for rotation in [(obj.width, obj.height), (obj.height, obj.width)]:

                for x in range(canvas_width):
                    for y in range(canvas_height):
                        obj.height = rotation[1]
                        obj.width = rotation[0]
                        if obj.can_be_placed(placed_objects, x, y, canvas_width, canvas_height):
                            placed_objects.append((x, y, Rectangle(rotation[0], rotation[1])))
                            placed = True
                            break
                    if placed:
                        break
                if placed:
                    break

        elif isinstance(obj, Triangle):
            # teste chaque rotation
            for rotation in [(obj.base, obj.height), (obj.height, obj.base)]:
                for x in range(canvas_width):
                    for y in range(canvas_height):
                        obj.height = rotation[1]
                        obj.base = rotation[0]
                        if obj.can_be_placed(placed_objects, x, y, canvas_width, canvas_height):
                            placed_objects.append((x, y, Triangle(rotation[0], rotation[1])))
                            placed = True
                            break
                    if placed:
                        break
                if placed:
                    break

        else:
            for x in range(canvas_width):
                for y in range(canvas_height):
                    if obj.can_be_placed(placed_objects, x, y, canvas_width, canvas_height):
                        placed_objects.append((x, y, obj))
                        placed = True
                        break
                if placed:
                    break

        if not placed:
            print("Failed to place object:", obj)
    return placed_objects


def placer_objet(objects, bac_width, bac_height):
    placed_objects = []
    last_x, last_y = 0, 0

    for obj in objects:
        placed = False

        if isinstance(obj, Rectangle):
            for rotation in [(obj.width, obj.height), (obj.height, obj.width)]:
                obj.width, obj.height = rotation
                if obj.can_be_placed(placed_objects, last_x, last_y, bac_width, bac_height):
                    placed_objects.append((last_x, last_y, Rectangle(obj.width, obj.height)))
                    last_x += obj.width

                    # check si il faut changer d'etage
                    if last_x >= bac_width:
                        last_x = 0
                        last_y += obj.height
                    placed = True
                    break

        elif isinstance(obj, Triangle):
            for rotation in [(obj.base, obj.height), (obj.height, obj.base)]:
                obj.base, obj.height = rotation
                if obj.can_be_placed(placed_objects, last_x, last_y, bac_width, bac_height):
                    placed_objects.append((last_x, last_y, Triangle(obj.base, obj.height)))
                    last_x += obj.base

                    if last_x >= bac_width:
                        last_x = 0
                        last_y += obj.height
                    placed = True
                    break
        else:
            
            if obj.can_be_placed(placed_objects, last_x, last_y, bac_width, bac_height):
                placed_objects.append((last_x, last_y, obj))
                last_x += obj.radius*2
                if last_x >= bac_width:
                    last_x = 0
                    last_y += obj.radius*2
                placed = True
                break
        

        if not placed:
            print("Failed to place object:", obj)
            last_x += obj.width
            if last_x >= bac_width:
                last_x = 0
                last_y += obj.height

    return placed_objects

