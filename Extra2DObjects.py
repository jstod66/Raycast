from graphics import *
import math

class Particle(Circle):
	angle_resolution = 10 #degrees

	def setRes(self,theta):
		self.angle_resolution = theta

class Ray(Point):
	dir = [0,1]

	def __init__(self,x,y,dir):
 		self.dir = dir
 		Point.__init__(self,x,y)

	def updateDir(self,dir):
 		self.dir = dir

	def createPoint(self):
		return Point(self.getX(),self.getY())

	def computeIntersect(self,Walls):
 		x3 = self.getX()
 		x4 = x3 + self.dir[0]
 		y3 = self.getY()
 		y4 = y3 + self.dir[1]

 		closestPt = Point(0,0)
 		ShortestDist = float("inf")
 		collision = False

 		for wall in Walls:

	 		x1 = wall.getP1().getX()
	 		x2 = wall.getP2().getX()
	 		y1 = wall.getP1().getY()
	 		y2 = wall.getP2().getY()

	 		den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)

	 		if(den==0):
	 			continue

	 		t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4))/den
	 		u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3))/den

	 		if( ((t<0) | (t>1)) | (u<0) ):
	 			continue

	 		collision = True
	 		pt_x = x1+t*(x2-x1)
	 		pt_y = y1+t*(y2-y1)
	 		dist = math.sqrt((pt_x-x3)**2 + (pt_y-y3)**2)

	 		if(dist<ShortestDist):
	 			ShortestDist = dist
	 			closestPt = Point(pt_x,pt_y)

	 	if(collision):
	 		return closestPt

	 	return

class Wall(Line):

	pass

class RayLine(Line):

	def _move(self,dx1,dy1,dx2,dy2):
		self.p1.x = dx1
        # self.p1.y = dy1
        # self.p2.x = dx2
        # self.p2.y = dy2