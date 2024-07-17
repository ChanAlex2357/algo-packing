import tkinter as tk
import Packing2D as pd2 
from tkinter import ttk
from bacs.Rectangle2D import  Rectangle2D
from objects.PackingObject2D import PackingObject2D

class PackingApp:
    def __init__(self, root,width:int=1280,height:int=720,objects:list=[]):
        self.root = root
        self.rectangle = Rectangle2D(50,50,width-50,height-50)
        self.root.title("2D Packing")
        self.init_frame_entry(root)
        self.init_object_form(root)
        self.init_canvas(root,width,height)
        self.init_entry()
        self.init_binding()
        # Initial drawing
        self.objects = objects
        self.update_treeview()
        self.draw_shape()

    def init_entry(self):
        # Create a variable for the shape
        self.shape_var = tk.StringVar(value="2D-BruteRotation")

        # Create a dropdown (combobox) for selecting shapes
        self.shape_selector = ttk.Combobox(self.entry_frame, textvariable=self.shape_var)
        self.shape_selector['values'] = ("2D-NFDH","2D-FFDH","2D-BF","2D-Brute","2D-BruteRotation")
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

    def clear_canvas(self):
        self.canvas.delete("all")
    def draw_rect(self,reset=True)->Rectangle2D:
        # Get the dimensions of the rectangle from the 
        marge_x,marge_y = 50,50
        if reset :
            self.clear_canvas()
        try:
            rect_width = int(self.width_entry.get())
        except ValueError:
            rect_width = self.rectangle.get_width()
        try:
            rect_height = int(self.height_entry.get())
        except ValueError:
            rect_height = self.rectangle.get_height()
        
        # Calculate the coordinates of the rectangle
        rect_x1, rect_y1 = marge_x, marge_y
        rect_x2 = rect_x1 + rect_width
        rect_y2 = rect_y1 + rect_height
        
        # Draw the rectangle
        self.canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, outline='black', width=2)
        self.rectangle = Rectangle2D(rect_x1,rect_y1,rect_width,rect_height)
    def init_object_form(self,root):
        # Frame for adding objects
        form_frame = tk.Frame(root)
        form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(form_frame, text="Add Packing Object").pack()

        tk.Label(form_frame, text="Width:").pack()
        self.new_width_entry = tk.Entry(form_frame)
        self.new_width_entry.pack()

        tk.Label(form_frame, text="Height:").pack()
        self.new_height_entry = tk.Entry(form_frame)
        self.new_height_entry.pack()

        tk.Button(form_frame, text="Add Object", command=self.add_object).pack()
        # Treeview to display the list of objects
        self.tree = ttk.Treeview(form_frame, columns=("Width", "Height"), show='headings')
        self.tree.heading("Width", text="Width")
        self.tree.heading("Height", text="Height")
        self.tree.pack()

        # Buttons to change the order of the objects
        button_frame = tk.Frame(form_frame)
        button_frame.pack()

        tk.Button(button_frame, text="Move Up", command=self.move_up).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Move Down", command=self.move_down).pack(side=tk.LEFT)

    def show_objects(self , color:str='gray'):
        for obj in self.rectangle.get_objects():
            obj.draw()
            print(f"Object at coordinates: {obj.get_coordinate()} with size ({obj.get_width()}x{obj.get_height()})")

    def draw_shape(self, event=None):        
        # Get the selected shape
        shape = self.shape_var.get()

        # Drawing rectangle
        self.draw_rect()
        try :
            # NEXT FIT DECREASING HEIGHT
            if shape ==  "2D-NFDH":
                self.rectangle.reset_objects()
                # print(f" -- {self.rectangle.get_width()} x {self.rectangle.get_height()} -- ")
                # NFDH
                pd2.next_fit_decreasing_height(self.objects, self.rectangle)
                self.show_objects()
    
            # FIRST FIT DECREASING HEIGHT
            elif shape == "2D-FFDH":
                self.rectangle.reset_objects()
                # FFDH
                pd2.first_fit_decreasing_height(self.objects, self.rectangle)
                self.show_objects()
            
            elif shape == "2D-BF":
                self.rectangle.reset_objects()
                # Best Fit
                pd2.best_fit(self.objects, self.rectangle)
                self.show_objects()
            elif shape == "2D-Brute":
                self.rectangle.reset_objects()
                # Brute Force
                bacs = pd2.brute_force(self.rectangle.get_width(),self.rectangle.get_height(),self.objects)
                self.rectangle.load_objects_from_bacs(bacs)
                self.show_objects()
            elif shape == "2D-BruteRotation":
                self.rectangle.reset_objects()
                # Brute Force
                bacs = pd2.brute_force_with_rotation(self.rectangle.get_width(),self.rectangle.get_height(),self.objects)
                self.rectangle.load_objects_from_bacs(bacs)
                self.show_objects()
        except Exception:
            print(Exception)


            

    def add_object(self):
        try:
            width = int(self.new_width_entry.get())
            height = int(self.new_height_entry.get())
            new_object = PackingObject2D(width, height)
            self.objects.append(new_object)
            self.update_treeview()
            self.draw_shape()
        except ValueError:
            print("Invalid width or height")

    def update_treeview(self):
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add all objects to the treeview
        for obj in self.objects:
            self.tree.insert('', 'end', values=(obj.get_width(), obj.get_height()))

    def move_up(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item[0])
            if index > 0:
                self.objects[index], self.objects[index - 1] = self.objects[index - 1], self.objects[index]
                self.update_treeview()
                self.draw_shape()

    def move_down(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item[0])
            if index < len(self.objects) - 1:
                self.objects[index], self.objects[index + 1] = self.objects[index + 1], self.objects[index]
                self.update_treeview()
                self.draw_shape()