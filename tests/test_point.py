#!/usr/bin/env python3

from lib.Screen import *
p = Point(222,333,flagconst = 'CLOSED')
p2 = Point((444,555))
p2.show()
p3 = Point(x = 66,y = 777,flagconst = 'CLOSED')
p3.show()
p4 = Point(22,33)
p4.show()

p.show()
p.setflag('LINE')
n = p.unsetflag('CLOSED')
p.show()





            






