#!/usr/bin/python3

import time

from lib.rectangle import *
from lib.colors import *
from lib.screen import *

r = Rectangle(1,1,18,10,border_color = LWHITE+BRED, color = WHITE+BBLUE)
r.draw()

r2 = Rectangle(xpos = 100, ypos =1,hlen = 4, vlen = 4, color = LWHITE+BCYAN)
r2.draw()
 
r3 = Rectangle(100,20,10,10,box = SIMPLE, border_color = LWHITE+BCYAN, color = LWHITE+BBLUE);
r3.draw()

r4 = Rectangle(200,20,20,20,box = SIMPLE, border_color = LWHITE+BBLUE, color = LWHITE+BGREEN);
r4.draw()
 
r5 = Rectangle(Point(120,40),Point(160,80),box = DOUBLE, border_color = LWHITE+BBLUE, color = LWHITE+BGREEN);
r5.draw()
 
r6 = Rectangle(70,20,40,20,box = HEAVY, border_color = LWHITE+BCYAN, color = WHITE+BRED, motif = "\N{DARK SHADE}");
r6.draw()

r7 = Rectangle(Point(20,40),Point(60,80),box = HEAVY, border_color = LWHITE+BCYAN, color = WHITE+BRED,is_void = True, motif = "\N{DARK SHADE}");

r7.draw()

 
time.sleep(4)
