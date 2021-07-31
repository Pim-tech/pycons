#!/usr/bin/env python3
import time

from lib.rectangle import *
from lib.screen import *
from lib.message import *

r = Rectangle(3,3,12,20,has_border = True, border_motif = 'Z', border_color = BLUE )

#r.draw()

r1 = Rectangle(hlen = 160, vlen = 70, box = DOUBLE, motif="\N{DARK SHADE}",color = BLUE)

#r1.draw()

#with ratio : 6.32
#high ration: 8

nocursor()
r2 = Rectangle(Point(130,3), Point(290,80),LRED, border_color = LGREEN, box = 1)

#r2.draw()

m1 = Message(message = 'Attention',textcolor = {'fg':11,'bg': 20} , motif="\N{DARK SHADE}",c256 = True,confirm={'m':'YESS','fg': 11,'bg':20},parent = r)

#m1.set_parent(r2)

m1.draw()
time.sleep(3)

cursor()

