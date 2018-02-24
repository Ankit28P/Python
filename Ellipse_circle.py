# -*- coding: utf-8 -*-
"""

"""


import math

class Ellipse:
    def __init__(self, x0, y0, x, y):
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.y =y
        
    def area(self):
        x,y = self.x,self.y
        return math.pi*x*y
    
    def circumference(self):
        x,y = self.x, self.y
        return math.pi*(3*(x+y)-math.sqrt((3*x+y)*(x+3*y)))
    
class circle(Ellipse):
    def __init__(self, x0, y0, r):
        Ellipse.__init__(self, x0, y0, r, r)
        
C = circle(4,6,2)
print C.area()
print C.circumference()
