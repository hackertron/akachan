#!/bin/bash

x0=1
y0=2
x=0
y=0
end=0

read -p "enter the coordinates (x,y)" x1 y1
#x=$(($originx + $x)) 
dx=$(($x1 - $x0))
dy=$(($y1 - $y0))
D=$((2 * $dy - $dx))

if [[ x0 -gt x1 ]]; then
	
	x=$x1
	y=$y1
	end=$x0

else
	x=$x0
	y=$y0
	end=$x1

fi
cd dump/dump
while [[ $x -lt $end ]]; do
	x=`expr $x + 1`
	if [[ $D -lt 0 ]]; then
		D=$(($D + 2 * $dy))

	else
		y=$(($y + 1))
		D=$(($D + 2 * ( $dy - $dx ) ))

	fi
	cp_file=$(printf "%03ox%03o.png" $x $y)
	cp $cp_file ../../images
done

cd ../../images
`convert   -delay 20   -loop 0   *.png   new_animated.gif`
