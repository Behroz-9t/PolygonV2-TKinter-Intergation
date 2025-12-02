import math 
from .PolyGon import Polygon
from .Point_Class import Point


class RegularPolygon(Polygon):
    """A regular polygon constructed by equal angular spacing around a center."""

    def __init__(self, n, radius, center=Point(0, 0), rotation=0):
        if n < 3:
            raise ValueError("A polygon must have at least 3 sides.")

    
        
        self._num_sides = n
        self.radius = radius
        # center is a Point object
        self.center = center if isinstance(center, Point) else Point(*center)
        self.rotation = math.radians(rotation)

        # Compute vertices like in n-gon
        self.vertices = self._compute_vertices()

        # Call the Polygon initializer
        super().__init__(self.vertices)

    def _compute_vertices(self):
        """Generate vertex coordinates using angle increments."""
        cx, cy = self.center._x, self.center._y
        vertices = []
        angle_inc = 2 * math.pi / self._num_sides
        angle = self.rotation

        for _ in range(self._num_sides):
            x = cx + self.radius * math.cos(angle)
            y = cy + self.radius * math.sin(angle)
            vertices.append(Point(x, y))
            angle += angle_inc
        return vertices

    # Inherit perimeter from Polygon (already computes from vertices)
    def area(self):
        """Area formula for a regular polygon."""
        s = self.sides[0]
        n = self.n

        return n * s * (s / (4 * math.tan(math.pi / n)))