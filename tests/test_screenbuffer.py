#!/usr/bin/env python3
from lib.screen import *

scrn = ScreenBuffer()

scrn.load_value(3,3)

scrn.load_value(1,4,'toto')

scrn.load_value(x = 1,y = 10, value = 'interview')
scrn.load_value(1,1,'jfdks')
scrn.load_value(1,2)

scrn.showbuf()

x = scrn.get_value(1,1)


scrn.make_indices()
