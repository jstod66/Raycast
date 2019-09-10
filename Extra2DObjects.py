from graphics import *

class Particle:
 pos = [0,0]
 angle_resolution = 10 #degrees

 def __init__(self,x,y,theta):
 	self.pos = [x,y]
 	self.angle_resolution = theta

 def draw(self,win):
 	c = Circle(Point(self.pos[0],self.pos[1]),5)
 	c.setFill('white')
 	c.draw(win)

class Ray:
 source = [0,0]
 dir = [0,1]

 def __init__(self,source,dir):
 	self.source = source
 	self.dir = dir

 def updateSource(self,source):
 	self.source = source

 def draw(self,intersect,win):
 	RayLine = Line(Point(self.source[0],self.source[1]),Point(intersect[0],intersect[1]))
 	RayLine.setFill('white')
 	RayLine.draw(win)

class Wall:
 start = [0,0]
 end = [0,0]

 def __init__(self,start,end):
 	self.start = start
 	self.end = end

 def draw(self,win):
 	WallLine = Line(Point(self.start[0],self.start[1]),Point(self.end[0],self.end[1]))
 	WallLine.setFill('red')
 	WallLine.setWidth(2)
 	WallLine.draw(win)

