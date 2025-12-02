import math
from Point_Class import Point


class Polygon:  # Abstract base for polygons built from Point-like (x, y) tuples.
     
   
   
    def __init__(self, vertices):
   
        
        self.vertices = [v if isinstance(v, Point) else Point(*v) for v in vertices]

    @property
    def n(self):
        return len(self.vertices)

    @property
    def sides(self):
        # Compute sides lengths using coordinate pairs.
        if self.n < 2:
            return []
        
  
        
        return [math.hypot(
            self.vertices[(i + 1) % self.n]._x - self.vertices[i]._x,
            self.vertices[(i + 1) % self.n]._y - self.vertices[i]._y,
        ) for i in range(self.n)]

    def perimeter(self):
        
        return sum(self.sides)
    

    def __str__(self):
        return f"{self.__class__.__name__} with {self.n} sides"
    

