import Packing1D as p1d
from objects.PackingObject1D import PackingObject1D

objects = []

objects.append( PackingObject1D(5) )
objects.append( PackingObject1D(9) )
objects.append( PackingObject1D(3) )
objects.append( PackingObject1D(6) )
objects.append( PackingObject1D(4) )
objects.append( PackingObject1D(7) )
objects.append( PackingObject1D(1) )

p1d.worstFit1D(15,objects)

for obj in objects:
    print(obj)