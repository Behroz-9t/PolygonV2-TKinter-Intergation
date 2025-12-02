# # DRAWS

# from Point_Class import Point
# from canvas import TKpanel

# class Pen:

#    class Pen:

#     def __init__(self,canvas:TKpanel):

#         self._canvas=canvas # stores canvas in _canvas 
#         self._cp=Point() # obj created and gave value to Point where x and y are 0 initially

#     def move_to(self,x,y):

#         self._cp=Point(x,y) # now move to tells _cp to change the value of x and y to something other than 0,0

#     def draw_to(self,x,y): # it stores new point value which is where the line is to be created

#         new_point=Point(x,y) # instantiated and created obj new point and gave value to Point(x,y)
#         self._canvas.add_line(self._cp,new_point) # here canvas adds line from _cp to the new point
#         self._cp=new_point # and then the cursor or the point from which the line will extend forwards so updated the _cp to new value

#     def get_position(self):
       
#         return self._cp # returns the value of new _cp

