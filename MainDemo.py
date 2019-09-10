from graphics import *
from Extra2DObjects import *
import math
import random

def main():
	
	NUM_WALLS = 4
	ANGLE_RES = 5
	HEIGHT = 500
	WIDTH = 500

	win = GraphWin("Raycasting Demo", WIDTH,HEIGHT)
	win.setBackground(color_rgb(0,0,0))

	#Create some walls
	Walls = []
	for i in range(0,NUM_WALLS):
		Walls.append(Wall(Point(random.randint(0,WIDTH),random.randint(0,HEIGHT)),Point(random.randint(0,WIDTH),random.randint(0,HEIGHT))))

	#Add the boundary walls
	Walls.append(Wall(Point(0,0),Point(0,HEIGHT)))
	Walls.append(Wall(Point(0,0),Point(WIDTH,0)))
	Walls.append(Wall(Point(0,HEIGHT),Point(WIDTH,HEIGHT)))
	Walls.append(Wall(Point(WIDTH,0),Point(WIDTH,HEIGHT)))

	#Draw the walls in thick red
	for w in Walls:
		w.setFill('red')
		w.setWidth(3)
		w.draw(win)

	RayPoint = Particle(Point(100,100),3)
	RayPoint.setFill('white')
	RayPoint.setRes(ANGLE_RES)

	RayPoint.draw(win)

	#Generate rays around RayPoint
	Rays = []
	for i in range(0,360,RayPoint.angle_resolution):
		Rays.append(Ray(RayPoint.getCenter().getX(),RayPoint.getCenter().getY(),[math.cos(math.radians(i)),math.sin(math.radians(i))]))

	#Generate initial RayLines
	RayLines = []
	for ray in Rays:
		intersectPt = ray.computeIntersect(Walls)
		RayLines.append(RayLine(ray.createPoint(),intersectPt))

	#Draw the RayLines
	for i in RayLines:
		i.setFill('white')
		i.draw(win)
	
	while(win.checkKey()!="x"):
		mousePos = win.checkMouse()
		if(mousePos):
			particleCentre = RayPoint.getCenter()
			dx = mousePos.getX()-particleCentre.getX()
			dy = mousePos.getY()-particleCentre.getY()
			#Move everything to new centre
			RayPoint.move(dx,dy)

			for r in RayLines:
				r.undraw()

			del RayLines
			RayLines = []

			for ray in Rays:
				ray.move(dx,dy)
				intersectPt = ray.computeIntersect(Walls)
				RayLines.append(RayLine(ray.createPoint(),intersectPt))

			for r in RayLines:
				r.setFill('white')
				r.draw(win)

			
	
	win.close()

main()