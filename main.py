#!/usr/bin/env python

import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class bresenham:
	def __init__(self, start, end):
		self.start = list(start)
		self.end = list(end)
		self.path = []
		
		self.steep = abs(self.end[1]-self.start[1]) > abs(self.end[0]-self.start[0])
		
		if self.steep:
			print 'Steep'
			self.start = self.swap(self.start[0],self.start[1])
			self.end = self.swap(self.end[0],self.end[1])
		
		if self.start[0] > self.end[0]:
			print 'flippin and floppin'
			_x0 = int(self.start[0])
			_x1 = int(self.end[0])
			self.start[0] = _x1
			self.end[0] = _x0
			
			_y0 = int(self.start[1])
			_y1 = int(self.end[1])
			self.start[1] = _y1
			self.end[1] = _y0
		
		dx = self.end[0] - self.start[0]
		dy = abs(self.end[1] - self.start[1])
		error = 0
		derr = dy/float(dx)
		
		ystep = 0
		y = self.start[1]
		
		if self.start[1] < self.end[1]: ystep = 1
		else: ystep = -1
		
		for x in range(self.start[0],self.end[0]+1):
			if self.steep:
				self.path.append((y,x))
			else:
				self.path.append((x,y))
			
			error += derr
			
			if error >= 0.5:
				y += ystep
				error -= 1.0
		
		print start
		print end
		print
		print self.start
		print self.end
	
	def swap(self,n1,n2):
		return [n2,n1]



def main():
	if os.path.exists("%s/permutations"%(DIR_PATH)):
		return
	
	os.system('mkdir %s/permutations'%(DIR_PATH))
	for i in range(0,100):
		for j in range(0,100):
			perm_name = "%03dx%03d.png"%(i,j)
			print perm_name
			os.system("composite -compose atop -geometry +%s+%s -gravity NorthWest \
				%s/media/emoji.ico %s/media/canvas.png %s/permutations/%s"%(i,j,DIR_PATH,DIR_PATH,DIR_PATH,perm_name))


def make_gif(x1=0,y1=0,x2=100,y2=100):
	assert (x1 >= 0 and y1 >=0 and x2 >= 0 and y2 >=0 and x1 < 100 and x2 < 100 and y1 < 100 and y2 < 100 ),"Coordinates must be between 0,0 to 99,99"

	if not os.path.exists("%s/animations"%(DIR_PATH)):
		os.system('mkdir %s/animations'%(DIR_PATH))

	if os.path.exists("%s/permutations/%03dx%03d-%03dx%03d.gif"%(DIR_PATH,x1,y1,x2,y2)):
		return "%s/permutations/%03dx%03d-%03dx%03d.gif"%(DIR_PATH,x1,y1,x2,y2)

	l = bresenham([x1,y1],[x2,y2])
	image_string = ''
	for i in l.path:
		image_string = image_string + ' permutations/%03dx%03d.png'%(i[0],i[1])
	
	cmd = 'convert -delay 10 %s -loop 0 animations/%03dx%03d-%03dx%03d.gif'%(image_string,x1,y1,x2,y2)
	os.system(cmd)

	
	
if __name__ == '__main__':
	main()
	make_gif()
	
