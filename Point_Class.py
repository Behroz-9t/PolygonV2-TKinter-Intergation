import math

class Point:
    """Represents a 2D point with encapsulated coordinates."""

    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    # --- Property for x:
    @property
    def get_x(self):
        """Get the X-coordinate."""
        return self._x

    @get_x.setter
    def get_x(self, value):
        """Set the X-coordinate (must be numeric)."""
        if not isinstance(value, (int, float)):
            raise TypeError("X-coordinate must be numeric.")
        self._x = float(value)

    # --- Property for y:
    @property
    def get_y(self):
        """Get the Y-coordinate."""
        return self._y

    @get_y.setter
    def get_y(self, value):
        """Set the Y-coordinate (must be numeric)."""
        if not isinstance(value, (int, float)):
            raise TypeError("Y-coordinate must be numeric.")
        self._y = float(value)

    # --- Distance method
    def distance_to(self, other):
        """Compute euclidean distance to another Point."""
        if not isinstance(other, Point):
            raise TypeError("distance_to() expects a Point instance.")
        return math.hypot(self._x - other._x, self._y - other._y)

    # --- String representations
    def __repr__(self):
        """Unambiguous representation for debugging."""
        return f"Point(x={self._x:.2f}, y={self._y:.2f})"

    # --- Equality check
    def __eq__(self, other):
        """Compare two points for equality."""
        return (
            isinstance(other, Point)
            and math.isclose(self.x, other.x)
            and math.isclose(self.y, other.y)
        )