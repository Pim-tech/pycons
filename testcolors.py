#!/usr/bin/env python3
from lib.Colors import *


c = Color()
mavar = c.sequence8(LRED+BBLUE,True)
print(mavar+'CECI EST LE TEXTE')
c._()
c.sequence8(BROWN);
print("BROWN");
c._()
c.sequence8(LGREEN);
print("LGREEN");
c.sequence8(LRED)
print("LRED")
c.sequence8(GREEN)
print("GREEN")
c.sequence8(RED)
print("RED")
c.sequence8(RED+BBLUE)
print("RED+BBLUE")
c.sequence8(BROWN + BBLACK)
print( "BROWN+BBLACK")
c.sequence8(BROWN +LBBLUE)
print( "BROWN+LBBLUE")
c.sequence8(BROWN + LBBLUE,mode=0)
print( "BROWN+LBBLUE+reset")
c.sequence8(RED+LBBLUE)
print( "RED+LBBLUE")
c.sequence8(BLACK+BBLUE)
print( "BLACK+BLUE")
c.sequence8(RED+BBLUE)
print( "RED+BLUE")
c.sequence8(LWHITE+BCYAN)
print( "LWHITE+BCYAN")
c.sequence8(LRED+LBCYAN)
print( "LRED+LBCYAN")
c._()
##Modes
c.sequence8(LRED+LBCYAN,mode=BOLD)
print("GRAS")
c.sequence8(LRED+LBCYAN,mode=LOW)
print("LOW")
c.sequence8(LRED+LBCYAN,mode=3)
print("italiques code 3")
c.sequence8(LRED+LBCYAN,mode=UNDERLINED)
print("UNDERLINED")
c.sequence8(LRED+LBCYAN,mode=BLINK)
print("LRED+LBCYAN, CLIGNOTANT")
#
c.sequence8(WHITE+BBLACK,mode=NO_UNDERLINE)
print("no Underlined")
c.sequence8(WHITE+BBLACK,False,NO_BLINK); 
print("no blink")
c.sequence8(WHITE,mode=0)
c.sequence8(WHITE,mode=6)
print("BLINK 2")
c.sequence8(WHITE,mode=0)
c.sequence8(LWHITE,mode=INVERSE)
print("INVERSED")
c.sequence8(LWHITE,mode=0)
c.sequence8(LWHITE,mode=8)
print("MASQUED")
c.sequence8(LWHITE,mode=0)
c.sequence8(LWHITE,mode=9)
print("TEXTE BARRE")
c._()


