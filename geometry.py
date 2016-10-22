#Geometry Definitions (WIP)

import math

def ps_area(w, h):
    return (w * h)

def point_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(y2-y1), math.pow(x2-x1))

def aabb_area(x1, y1, x2, y2):
    return ps_area(y2-y1, x2-x1)

def toCartesian_x(dist,deg):
    return float(math.sin(math.radians(deg))*dist)

def toCartesian_y(dist,deg):
    return float(math.cos(math.radians(deg))*dist)

def distance_point(x1,y1,x2,y2):
    xd = float(x2) - float(x1)
    yd = float(y2) - float(y1)
    return float(math.sqrt(pow(xd,2)+pow(yd,2)))

def circumference(r):
    return float(2 * math.pi * r)

def circle_area(r):
    return float(math.pi * math.pow(r,2))
