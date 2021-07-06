from lib.Misc import *
from lib import constant

BLACK = 0
RED = 1
GREEN = 2
BROWN = 3
BLUE = 4;         #couleurs de bases
MAGENTA = 5
CYAN = 6
WHITE = 7
    
LBLACK = 8
LRED = 9
LGREEN = 10
LYELLOW = 11
LBLUE = 12;        
LMAGENTA = 13;        #couleurs claires
LCYAN = 14; 
LWHITE = 15
    
    
BBLACK = 0;         # Les couleurs de fond commencent  a  16
BRED = 16
BGREEN = 32;       
BYELLOW = 48;        #couleurs de fond
BBLUE = 64
BMAGENTA = 80
BCYAN = 96
BWHITE = 112
    
LBBLACK = 128
LBRED = 144
LBGREEN = 160
LBYELLOW = 176
LBBLUE = 192
LBMAGENTA = 208
LBCYAN = 224
LBWHITE = 240
    
NOCOLOR = 129
    
BOLD = 1
LOW = 2
ITALIC = 3
UNDERLINED = 4
CONSFGLIGHT = 5; #clignote sur xterm, en console couleur claire d'avant plant
BLINK = 6;       #clignote sur xterm seulement
INVERSE = 7
MASQUED = 8
STRIKE  = 9
REINIT = 10;       
NULLC = 11;     #needded to display chars to build boxes
NULLCCMETA = 12
NORMAL1 = 21
NORMAL2 = 22
NO_UNDERLINE = 24
NO_BLINK = 25
NOINVERSE = 27
GRMOD = "\016"

DRKCOLMSK = 0b00000111
LICOLMSK  = 0b00001000
DRKBGMSK  = 0b01110000
LIBGMSK   = 0b10000000
COLOR_256_MASQ = 0b0000000011111111
BGND_256_MASQ  = 0b1111111100000000


COLOR_ANSI = 1
COLOR_256 = 2
COLOR_TRUECOLOR = 3

class Color:
    def __init__(self):
        self.current_color = 0
        self.current_bg = -1
        self.current_mode = 0
        self.current_li = False
        self.current_color_256 = 0
        self.current_bgcolor_256 = 0
        self.format = None

    def sequence8(self,attr: int, rstr=False, mode=None) -> str:
        prnt = lambda a: print(a,end='') if not rstr else lambda a: a
        color = attr & DRKCOLMSK
        is_licolor = bool(( attr & LICOLMSK) >> 3)
        bgcolor = (attr & DRKBGMSK) >> 4
        is_libgcolor = bool((attr & LIBGMSK) >> 7)
        seq=[]
        reset = False
        if (self.current_li == True and is_licolor == False) or (mode is not None and mode == 0):
            reset = True
            seq.append('0')
        else:
            reset = False;
            if is_licolor == True and self.current_li == False:
                seq.append('1') 
        if reset == True or color != self.current_color:
            seq.append( str(color + 30) )
        n_light = 100 if is_libgcolor else 40
        bg = bgcolor + n_light
        if reset == True or bg != self.current_bg:
            seq.append(str(bg))
        if mode is not None and mode > 0 and mode != self.current_mode:
            seq.append(str(mode))

        self.current_color = color
        self.current_bg = bg
        self.current_li = is_licolor
        if mode is not None:
            self.current_mode = mode
        seqstr = constant.STARTSEQ + ';'.join(seq) + 'm'
        #seqstr = '[' + ';'.join(seq) + 'm'
        return prnt(seqstr)
    
    def sequence256():
        return

    def sequence_256():
        return

    def print():
        return

    def say():
        return
    
    def print256c():
        return

    def print_256bf():

    def say256c():
        return

    def say256bf():
        return

    def _(self,rstr = False) -> str:
        prnt = lambda a: print(a,end='') if not rstr else lambda a: a
        self.current_li = False;
        return prnt(chr(27) + "[0m")


