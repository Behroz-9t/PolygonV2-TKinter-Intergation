from Irreg_Polygon import IrregularPolygon
from Point_Class import Point

class Triangle(IrregularPolygon):
    """A triangle defined by 3 arbitrary vertices."""
    
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.")
        super().__init__(vertices)

    # Uses Shoelace area() and perimeter() from IrregularPolygon
    
    def __str__(self):
        # Note: It appears to return the representation from IrregularPolygon
        # but the class name will be 'Triangle' due to f-string in IrregularPolygon's __str__
        return f"Triangle with {self.n} vertices"
       
        
        # The corrected version of what the instructor likely intended:
        
        
# p1=Point(0,0)
# p2=Point(3,0)
# p3=Point(3,4)

# t=Triangle([p1,p2,p3])
# print(t.area())
# print(t.perimeter())
# print(t.vertices)
