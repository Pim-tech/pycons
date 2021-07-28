#!/usr/bin/env python3

from lib.rectangle import *
from lib.screen import *

r = Rectangle(3,3,12,20,has_border = True, border_motif = 'Z', border_color = BLUE )

r.show()

r1 = Rectangle(xpos = 1, ypos = 2,hlen = 3, vlen = 4, has_border = True)
r1.show()

r2 = Rectangle(Point(2,7), Point(12,12),9,has_border=True,  border_color = 10, box = 1)

r2.show()
