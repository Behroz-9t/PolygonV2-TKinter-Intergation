from ..Point_Class import Point

class Line:
    def __init__(self,start:Point,end:Point): #--> Here (:Point) shows the type of the start and end arguments
        self.start=start
        self.end=end

    def length(self): # func for length of the line
        return self.start.distance_to(self.end)
    
    def __str__(self):
        return f"Line => ({self.start} -------- {self.end})"

