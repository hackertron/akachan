
import os

def main():
	os.system('mkdir dump')
	for i in range(0,205,5):
		for j in range(0,205,5):
			print i,j
			os.system("composite -compose atop -geometry +%s+%s -gravity NorthWest emoji.ico canvas.png dump/%03dx%03d.png"%(i,j,i,j))
			

def make_gif():
	os.system("convert -delay 10 -loop 0 dump/*.png animation.gif")
	
	
if __name__ == '__main__':
	make_gif()
	#main()
