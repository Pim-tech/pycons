#!/usr/bin/env python3

rstr=True
#prnt=None
prnt = (lambda a: a)  if rstr == True else lambda a: print(a,end='')
#if rstr:
#    prnt = lambda a: a
#else:
#    prnt = lambda a: print(a,end='')

#prnt('toto')
print(prnt('toto'))



        
