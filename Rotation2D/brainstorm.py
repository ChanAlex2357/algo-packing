import math







# Vérifier si un cercle peut être placé à une position donnée
def can_place_circle(placed_objects, x, y, radius, canvas_width, canvas_height):
    if x - radius < 0 or x + radius > canvas_width or y - radius < 0 or y + radius > canvas_height:
        return False
    for px, py, obj in placed_objects:
        if isinstance(obj, Circle):
            if math.hypot(px - x, py - y) < obj.radius + radius:
                return False
        elif isinstance(obj, Rectangle):
            if (x + radius > px and x - radius < px + obj.width and 
                y + radius > py and y - radius < py + obj.height):
                return False
        elif isinstance(obj, IsoscelesTriangle):
            if (x + radius > px - obj.get_base()/2 and x - radius < px + obj.get_base()/2 and 
                y + radius > py and y - radius < py + obj.height):
                return False
    return True

# Vérifier si un rectangle peut être placé à une position donnée
def can_place_rectangle(placed_objects, x, y, width, height, canvas_width, canvas_height):
    if x < 0 or x + width > canvas_width or y < 0 or y + height > canvas_height:
        return False
    for px, py, obj in placed_objects:
        if isinstance(obj, Circle):
            if (px - obj.radius < x + width and px + obj.radius > x and 
                py - obj.radius < y + height and py + obj.radius > y):
                return False
        elif isinstance(obj, Rectangle):
            if (x < px + obj.width and x + width > px and 
                y < py + obj.height and y + height > py):
                return False
        elif isinstance(obj, IsoscelesTriangle):
            if (x < px + obj.get_base()/2 and x + width > px - obj.get_base()/2 and 
                y < py + obj.height and y + height > py):
                return False
    return True

# Vérifier si un triangle isocèle peut être placé à une position donnée
def can_place_triangle(placed_objects, x, y, base, height, canvas_width, canvas_height):
    if x - get_base()/2 < 0 or x + get_base()/2 > canvas_width or y < 0 or y + height > canvas_height:
        return False
    for px, py, obj in placed_objects:
        if isinstance(obj, Circle):
            if (px - obj.radius < x + get_base()/2 and px + obj.radius > x - get_base()/2 and 
                py - obj.radius < y + height and py + obj.radius > y):
                return False
        elif isinstance(obj, Rectangle):
            if (x < px + obj.width and x + base > px and 
                y < py + obj.height and y + height > py):
                return False
        elif isinstance(obj, IsoscelesTriangle):
            if (x < px + obj.get_base()/2 and x + base > px - obj.get_base()/2 and 
                y < py + obj.height and y + height > py):
                return False
    return True

# Fonction de placement heuristique
def place_objects_heuristically(objects, canvas_width, canvas_height):
    placed_objects = []
    for obj in objects:
        placed = False
        if isinstance(obj, Circle):
            for x in range(canvas_width):
                for y in range(canvas_height):
                    if can_place_circle(placed_objects, x, y, obj.radius, canvas_width, canvas_height):
                        placed_objects.append((x, y, obj))
                        placed = True
                        break
                if placed:
                    break
        elif isinstance(obj, Rectangle):
            for rotation in [(obj.width, obj.height), (obj.height, obj.width)]:
                for x in range(canvas_width):
                    for y in range(canvas_height):
                        if can_place_rectangle(placed_objects, x, y, rotation[0], rotation[1], canvas_width, canvas_height):
                            placed_objects.append((x, y, Rectangle(rotation[0], rotation[1])))
                            placed = True
                            break
                    if placed:
                        break
                if placed:
                    break
        elif isinstance(obj, IsoscelesTriangle):
            for x in range(canvas_width):
                for y in range(canvas_height):
                    if can_place_triangle(placed_objects, x, y, obj.base, obj.height, canvas_width, canvas_height):
                        placed_objects.append((x, y, obj))
                        placed = True
                        break
                if placed:
                    break
        if not placed:
            print("Failed to place object:", obj)
    return placed_objects
