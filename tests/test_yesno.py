#!/usr/bin/python3
#script de test pour la classe yesno.

from lib.rectangle import *
from lib.yesno import *


r = Rectangle(3,3,110,77,has_border = True, box = SIMPLE, border_color = LBBLUE )
r.draw()

yesno = YesNo(yes = 'OK',no = 'Cancel', textcolor = 34304,  parent = r, attryes = 112, attrno = 231,
        message = 'Are you Ok to' ,gap_yesno = 10,c256 = True)
yesno.draw()
