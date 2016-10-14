


import re
import urllib2

coordinates=raw_input()


#regex = re.compile("x1:([0-9]{1,3})")
x1 = re.search( r'x1:([0-9]{1,3})', coordinates, re.M|re.I|re.U)
x1 = x1.group(1)
print x1

y1 = re.search( r'y1:([0-9]{1,3})', coordinates, re.M|re.I|re.U)
y1 = y1.group(1)
print y1

x2 = re.search( r'x2:([0-9]{1,3})', coordinates, re.M|re.I|re.U)
x2 = x2.group(1)
print x2

y2 = re.search( r'y2:([0-9]{1,3})', coordinates, re.M|re.I|re.U)
y2 = y2.group(1)
print y2

url = "http://chestream.cloudapp.net:5000/?" + "x1=" + x1 + "&y1=" + y1 + "&x2=" + x2 + "&y2=" + y2

print url

## don't know where to send gif so just reading it and printing it  ##
content = urllib2.urlopen(url).read()
print content

