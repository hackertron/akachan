#!/usr/bin/env python

import flask, flask.views
from flask import request
from app import app

import os
from bresenham import bresenham

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
SERVER_URL = 'http://chestream.cloudapp.net:8080/akachan'


@app.route('/')
def home():
    x1 = request.args['x1'] or 0
    x2 = request.args['x1'] or 0
    y1 = request.args['y1'] or 12
    y2 = request.args['y2'] or 13
    return make_gif()

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


def make_gif(x1=0,y1=50,x2=10,y2=39):
    assert (x1 >= 0 and y1 >=0 and x2 >= 0 and y2 >=0 and x1 < 100 and x2 < 100 and y1 < 100 and y2 < 100 ),"Coordinates must be between [0,0]&[99,99]"

    if not os.path.exists("%s/animations"%(DIR_PATH)):
        os.system('mkdir %s/animations'%(DIR_PATH))

    if os.path.exists("%s/permutations/%03dx%03d-%03dx%03d.gif"%(DIR_PATH,x1,y1,x2,y2)):
        return "%s/%03dx%03d-%03dx%03d.gif"%(SERVER_URL,x1,y1,x2,y2)

    l = bresenham([x1,y1],[x2,y2])
    image_string = ''
    for i in l.path:
        image_string = image_string + ' %s/permutations/%03dx%03d.png'%(DIR_PATH,i[0],i[1])
    
    cmd = 'convert -delay 10 %s -loop 0 %s/animations/%03dx%03d-%03dx%03d.gif'%(image_string,DIR_PATH,x1,y1,x2,y2)
    os.system(cmd)

    return "%s/%03dx%03d-%03dx%03d.gif"%(SERVER_URL,x1,y1,x2,y2)
    


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')