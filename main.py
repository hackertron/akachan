
import os


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
	os.system('mkdir dump')
	for i in range(0,100):
		for j in range(0,100):
			print i,j
			os.system("composite -compose atop -geometry +%s+%s -gravity NorthWest emoji.ico canvas.png dump/%03dx%03d.png"%(i,j,i,j))


def make_gif2(x1=1,y1=2,x2=50,y2=83):
	l = bresenham([x1,y1],[x2,y2])
	image_string = ''
	for i in l.path:
		image_string = image_string + ' dump/%03dx%03d.png'%(i[0],i[1])
	
	print image_string

	cmd = 'convert -delay 10 %s -loop 0 animation2.gif'%(image_string)
	os.system(cmd)


def make_gif():
	os.system("convert -delay 10 -loop 0 dump/*.png animation.gif")
	
	
if __name__ == '__main__':
	make_gif2()
	#main()
	#pass
