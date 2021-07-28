#!/usr/bin/env python3
from lib.colors import *
print(BROWN)

MONMASQ = 0b00001111

class MColor:
    def sequence8(self,col):
        color = col & MONMASQ
        print(color)


c = MColor()
c.sequence8(12);
