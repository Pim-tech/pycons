#!/usr/bin/python3
import time
from lib.alert import *

r = Alert(message = 'hou la la',textcolor = LWHITE+BBLUE, motif='o')
nocursor()
r.draw()


time.sleep(5)

cursor()

