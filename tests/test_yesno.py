#!/usr/bin/python3
#script de test pour la classe yesno.

from lib.rectangle import *
from lib.yesno import *


r = Rectangle(3,3,120,70,has_border = True, box = SIMPLE, border_color = LBBLUE )
r.draw()

yesno = YesNo(yes = 'OK',no = 'Cancel', textcolor = LWHITE+BCYAN, parent = r, 
        message = 'Do you really want to do that?') 
#yesno.set_parent(r)
yesno.draw()
