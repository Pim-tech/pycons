#!/usr/bin/python3
from lib.colors import *

c = Color()

s = c.say('ABCDEFGHIJKLMNOPQRSTUVWXYZ',LWHITE+LBRED,fixed_width= 180, spacing = 4 , rstr = True)
print("Interview")
c.print("Ceci est le message",LWHITE+LBBLUE,spacing = 10, fixed_width = 200)
print("")
c.say256c('INTERVIEWS',4178,fixed_width = 180)
print("est");
c.say256bf('AND THEN',12,124,fixed_width = 180)
print('quoi')
c.say256c('fjdlsfjkds',127751,spacing = 20)
print('entre')
c.say256bf('QUE SE PASSE-TIL',5,10,spacing = 50, fixed_width = 280)
print('The End')
print(s)

for a in range(0,255):
    c.sequence256bf(a,0)
    print(a,flush=True,end=' ')
    if (a % 60) == 0:
        print('')
    

c._()


