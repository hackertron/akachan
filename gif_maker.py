import os
import sys

coordinates = raw_input()

x0 , y0 , x1 , y1 = coordinates.split()

print x0 , y0 , x1 , y1

dx = (int(x1) - int(x0))
dy = (int(y1) - int(y0))
D =  (2 * int(dy) - int(dx))

print dx , dy , D

if x0 > x1:
	
	x=int(x1)
	y=int(y1)
	end=int(x0)

else:

	x=int(x0)
	y=int(y0)
	end=int(x1)



os.chdir("dump/dump")

# print os.getcwd()

while x < end:
	x = int(x) + 1

	if D < 0:
		D=(int(D) + 2 * int(dy))

	else:
		y=((int(y) + 1))
		D=(int(D) + 2 * ( int(dy) - int(dx))) 


	cp_file = str('%03dx%03d.png'%(x,y))

	os.system("cp cp_file , ../../images")

os.chdir("../../images")

os.system("convert   -delay 10   -loop 0   *.png   new_animated.gif")
