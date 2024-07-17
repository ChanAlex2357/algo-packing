import tkinter as tk
from tkinter import ttk
from bacs.Rectangle2D import  Rectangle2D

class PackingApp:
    def __init__(self, root,width:int=1280,height:int=720,objects:list=[]):
        self.root = root
        self.root.title("Shape Selector")
        self.init_frame_entry(root)
        self.init_canvas(root,width,height)
        self.init_entry()
        self.init_binding()
        self.rectangle = None
        # Initial drawing
        self.draw_shape()

    def init_entry(self):
        # Create a variable for the shape
        self.shape_var = tk.StringVar(value="")

        # Create a dropdown (combobox) for selecting shapes
        self.shape_selector = ttk.Combobox(self.entry_frame, textvariable=self.shape_var)
        self.shape_selector['values'] = ("NFDH")
        self.shape_selector.pack()
        # Width entry
        tk.Label(self.entry_frame, text="Width:").pack(side=tk.LEFT)
        self.width_entry = tk.Entry(self.entry_frame)
        self.width_entry.pack(side=tk.LEFT)

        # Height entry
        tk.Label(self.entry_frame, text="Height:").pack(side=tk.LEFT)
        self.height_entry = tk.Entry(self.entry_frame)
        self.height_entry.pack(side=tk.LEFT)

    def init_canvas(self,root,w,h):
        # Create a canvas
        self.canvas = tk.Canvas(root, width=w, height=h)
        self.canvas.pack()
    def init_frame_entry(self,root):
        # Create a frame for the entries
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack()
    def init_binding(self):
        # Bind the dropdown selection event to the draw_shape function
        self.shape_selector.bind("<<ComboboxSelected>>", self.draw_shape)

        # Bind the entry fields to the draw_shape function
        self.width_entry.bind("<KeyRelease>", self.draw_shape)
        self.height_entry.bind("<KeyRelease>", self.draw_shape)

    def draw_rect(self)->Rectangle2D:
        # Get the dimensions of the rectangle from the entries
        try:
            rect_width = int(self.width_entry.get())
            rect_height = int(self.height_entry.get())
        except ValueError:
            rect_width = 200
            rect_height = 100
        
        # Calculate the coordinates of the rectangle
        rect_x1, rect_y1 = 50, 50
        rect_x2 = rect_x1 + rect_width
        rect_y2 = rect_y1 + rect_height
        
        # Draw the rectangle
        self.canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline='black', width=2)
        
        # Calculate the center of the rectangle
        center_x = (rect_x1 + rect_x2) // 2
        center_y = (rect_y1 + rect_y2) // 2
        
        self.rectangle = Rectangle2D(rect_x1,rect_y1,rect_x2,rect_y2)

    def draw_shape(self, event=None):
        # Clear the canvas
        self.canvas.delete("all")
        
        # Get the selected shape
        shape = self.shape_var.get()

        # Drawing rectangle
        
        if shape ==  "NFDH":
        
