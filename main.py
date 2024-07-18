import tkinter as tk
from tkinter import ttk
from objects.PackingObject2D import PackingObject2D
from objects.Cercle import Cercle
from objects.Triangle import Triangle
from PackingGui.PackingApp import PackingApp

objects = [
#     PackingObject2D(100, 200),
#     PackingObject2D(200, 150),
#     PackingObject2D(150, 300),
#     PackingObject2D(120, 180),
#     PackingObject2D(300, 100)
]
# objects = [
#     PackingObject2D(100, 200),
#     Cercle(50),
#     Triangle(50,50)
# ]
# print(objects)

root = tk.Tk()
app = PackingApp(root,objects=objects)
root.mainloop()