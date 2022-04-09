#!/usr/bin/python3

import time

from lib.rectangle import *
from lib.colors import *
from lib.screen import *

clear_screen()
r = Rectangle(1,1,18,10,border_color = LWHITE+BRED, color = {'bg': ( 100 ,100,100), 'fg': (0,0,255)})
r.draw()

r2 = Rectangle(xpos = 100, ypos =1,hlen = 4, vlen = 4, color = {'bg':129 ,'fg':1112})
r2.draw()
 
r3 = Rectangle(100,20,10,10,box = SIMPLE, border_color = LWHITE+BCYAN, color = LWHITE+BBLUE);
r3.draw()

r4 = Rectangle(200,20,20,20,box = SIMPLE, border_color = LWHITE+BBLUE, color = LWHITE+BGREEN);
r4.draw()
 
r5 = Rectangle(Point(250,40),Point(290,80),box = DOUBLE, border_color = LWHITE+BBLUE, color = LWHITE+BGREEN);
r5.draw()
 
r6 = Rectangle(50,20,40,20,box = HEAVY, border_color = LWHITE+BCYAN, color = WHITE+BRED, motif = "\N{DARK SHADE}");
r6.draw()

r7 = Rectangle(Point(120,20),Point(160,50),box = HEAVY, border_color = LWHITE+BCYAN, color = WHITE+BRED,is_void = True, motif = "\N{DARK SHADE}");

r7.draw()

 
time.sleep(4)
