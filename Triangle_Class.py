from Irreg_Polygon import IrregularPolygon
from Point_Class import Point

class Triangle(IrregularPolygon):
    """A triangle defined by 3 arbitrary vertices."""
    
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.")
        super().__init__(vertices)

    
    
    def __str__(self):

        return f"Triangle with {self.n} vertices"
       
       
        
