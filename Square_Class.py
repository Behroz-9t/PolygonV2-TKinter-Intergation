from Reg_Polygon import RegularPolygon
import math
from Point_Class import Point


class Square(RegularPolygon):
    """A square is a regular polygon with 4 equal sides."""

    def __init__(self,  center=Point(0, 0),side=1, rotation=45):
        # side = radius * 2 / sqrt(2) -> radius = side * sqrt(2) / 2
        radius = side / math.sqrt(2)
        
        # n=4 for a square
        super().__init__(n=4, radius=radius, center=center, rotation=rotation)
        self.side = side  # optional: keep for convenience

    def area(self):
        # Override with simpler formula
        return self.side ** 2

    def __str__(self):
        return f"Square(sides={self.side:.2f})"
    
    
