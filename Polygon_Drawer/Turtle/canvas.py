#LIKE PAPER

import tkinter as tk
from ..Point_Class import Point
from .line import Line

class TKpanel(tk.Canvas):
    def __init__(self, master=None, width=400, height=400, **kwargs):# here **kwargs are used for the input (bg) because it takes input as tuple
        
        super().__init__(master, width=width, height=height, bg='black', **kwargs)
        self.lines = []


    def add_line(self, P: Point, Q: Point):
        
        self.lines.append(Line(P, Q))
        print(f"\nLine from ({P.get_x}, {P.get_y}) to ({Q.get_x}, {Q.get_y})\n")
        self.draw()  


    def draw(self):
        
        self.delete("all")  # Clear previous drawings
        for line in self.lines:
            self.create_line(line.start.get_x, line.start.get_y, line.end.get_x, line.end.get_y,
                             fill='white', width=5)
            

    