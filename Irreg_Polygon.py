from PolyGon import Polygon

class IrregularPolygon(Polygon):
    """A polygon defined by arbitrary vertices (Point objects or (x, y) tuples)."""

    def __init__(self, vertices):
        """
        Accepts either:
        - A list of Point objects, or
        - A list of (x, y) coordinate tuples.
        Normalization to Point objects is handled by Polygon.
        """
        
      
        super().__init__(vertices)  

    def area(self):
        """Compute the polygon's area using the Shoelace theorem:
        A = 1/2 * |Σ (x_i*y_i+1 - y_i*x_i+1)|
        """
        n = self.n
        # Extract x, y for p in self.vertices
        x = [p._x for p in self.vertices]
        y = [p._y for p in self.vertices]
        
        # Shoelace formula:
        # 0.5 * sum(x[i] * y[(i+1)%n] - y[i] * x[(i+1)%n]) for i in range(n)
        return 0.5 * abs(
            sum(x[i] * y[(i + 1) % n] - y[i] * x[(i + 1) % n] for i in range(n))
        )

    def __str__(self):
        """Readable summary for display or polymorphism demo."""
      
        return f"IrregularPolygon with {self.n} vertices, " \
               f"Area={self.area():.2f}, " \
               f"Perimeter={self.perimeter():.2f}"
               
               
