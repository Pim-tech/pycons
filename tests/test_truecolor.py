#!/usr/bin/python3

from lib.colors import *

c = Color()

c.sequencervb({'r': 255,'v':255,'b':0},{'r': 0 ,'v': 0 ,'b': 0})
print('interview 0') 
c.sequencervb({'r': 255,'v':255,'b':0},{'r': 1 ,'v': 1 ,'b': 1},mode = 1)
print('interview 1') 
c.sequencervb({'r': 255 ,'v': 255 ,'b': 255},{'r': 0,'v':0,'b':255}, mode=0)
print('NKLKLKLJ 0') 
c.sequencervb({'r': 255 ,'v': 255 ,'b': 255},{'r': 0,'v':0,'b':255}, mode = 1)
print('NKLKLKLJ 1') 
c._()

c.sayrvb("LES POULES: j'adore!",{'r':255,'v':255,'b':255},{'r': 0,'v':0,'b':255},fixed_width = 200,spacing = 10,mode = 1)
