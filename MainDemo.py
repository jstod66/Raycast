from graphics import *
from Extra2DObjects import *
import math
import random

def main():
	
	NUM_WALLS = 4
	HEIGHT = 500
	WIDTH = 500

	win = GraphWin("Raycasting Demo", WIDTH,HEIGHT)
	win.setBackground(color_rgb(0,0,0))

	#Create some walls
	Walls = []
	for i in range(0,NUM_WALLS):
		Walls.append(Wall([random.randint(0,WIDTH),random.randint(0,HEIGHT)],[random.randint(0,WIDTH),random.randint(0,HEIGHT)]))

	for w in Walls:
		w.draw(win)

	RayPoint = Particle(100,100,10)

	RayPoint.draw(win)

	#create tuple of rays
	Rays = []
	for i in range(0,360,RayPoint.angle_resolution):
		direction = [math.sin(math.radians(i)), math.cos(math.radians(i))]
		Rays.append(Ray(RayPoint.pos,direction))

	print(len(Rays))

	#draw all the rays
	for ray in Rays:
		ray.draw([ray.source[0] + 100*ray.dir[0],ray.source[1]+100*ray.dir[1]],win)
	


	win.getMouse()
	win.close()

main()