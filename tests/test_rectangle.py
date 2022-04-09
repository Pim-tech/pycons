#!/usr/bin/env python3
import time


from lib.rectangle import *
from lib.screen import *
from lib.message import *

r = Rectangle(3,3,120,70,has_border = True, box = SIMPLE, border_color = LBBLUE )

r.draw()

r1 = Rectangle(hlen = 160, vlen = 70, box = DOUBLE, motif="\N{DARK SHADE}",color = BLUE)
#
r1.draw()
#
#
nocursor()
r2 = Rectangle(Point(130,3), Point(290,80),LRED, border_color = LGREEN, box = 1)
#
r2.draw()

m1 = Message(message = 'CONFIRMEZ-MOI CA',textcolor = {'fg': (255,255,0),'bg':( 0,0,0),'mode':5} , motif="\N{DARK SHADE}",confirm='VAS-Y!', confirm_color = {'fg': (255,0,0),'bg': (0,255,0),'mode': 1})

m1.set_parent(r2)

m1.draw()
time.sleep(3)

cursor()

