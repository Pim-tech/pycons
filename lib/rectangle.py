
from lib.misc import * 
from lib.colors import *
from lib.screen import *
import sys


HLINE = 0
VLINE = 1
UPLEFT = 2
UPRIGHT = 3
DWNLEFT = 4
DWNRIGHT = 5

SIMPLE = 1
DOUBLE = 2
HEAVY  = 3
LIGHTARC = 4

class Border:
    def __init__(self):
        self.motif = 'x'
        self.color = WHITE+BBLACK

#[╭]  U+256D   &#9581;  BOX DRAWINGS LIGHT ARC DOWN AND RIGHT
#[╮]  U+256E   &#9582;  BOX DRAWINGS LIGHT ARC DOWN AND LEFT
#[╯]  U+256F   &#9583;  BOX DRAWINGS LIGHT ARC UP AND LEFT
#[╰]  U+2570   &#9584;  BOX DRAWINGS LIGHT ARC UP AND RIGHT


class Rectangle:
    def __init__(self,*args,**kws):
        self.motif = '*'
        self.has_border = False
        self.hasbox = False
        self.border_motif = '+'
        self.box = 0
        self.points = []
        self.coords_color = []
        self.hlen = self.vlen = None
        self.a = self.b = None
        self.is_void = False
        self.xpos = self.ypos = None
        self.oxpos= self.oypos = None
        self.parent = None

        self.boxes = [
        [
        "\N{BOX DRAWINGS LIGHT HORIZONTAL}",
        "\N{BOX DRAWINGS LIGHT VERTICAL}" ,
        "\N{BOX DRAWINGS LIGHT DOWN AND RIGHT}",
        "\N{BOX DRAWINGS LIGHT DOWN AND LEFT}",
        "\N{BOX DRAWINGS LIGHT UP AND RIGHT}",
        "\N{BOX DRAWINGS LIGHT UP AND LEFT}"
        ],
        [
        "\N{BOX DRAWINGS DOUBLE HORIZONTAL}",
        "\N{BOX DRAWINGS DOUBLE VERTICAL}" ,
        "\N{BOX DRAWINGS DOUBLE DOWN AND RIGHT}",
        "\N{BOX DRAWINGS DOUBLE DOWN AND LEFT}",
        "\N{BOX DRAWINGS DOUBLE UP AND RIGHT}",
        "\N{BOX DRAWINGS DOUBLE UP AND LEFT}"
        ],
        [
        "\N{BOX DRAWINGS HEAVY HORIZONTAL}",
        "\N{BOX DRAWINGS HEAVY VERTICAL}" ,
        "\N{BOX DRAWINGS HEAVY DOWN AND RIGHT}",
        "\N{BOX DRAWINGS HEAVY DOWN AND LEFT}",
        "\N{BOX DRAWINGS HEAVY UP AND RIGHT}",
        "\N{BOX DRAWINGS HEAVY UP AND LEFT}"
        ],
        [
        "\N{BOX DRAWINGS LIGHT HORIZONTAL}",
        "\N{BOX DRAWINGS LIGHT VERTICAL}" ,
        "\N{BOX DRAWINGS LIGHT ARC DOWN AND RIGHT}",
        "\N{BOX DRAWINGS LIGHT ARC DOWN AND LEFT}",
        "\N{BOX DRAWINGS LIGHT ARC UP AND RIGHT}",
        "\N{BOX DRAWINGS LIGHT ARC UP AND LEFT}"
        ],

        ]
        
        self.color_instance = Color()
        self.color = self.color_instance.sequence8(WHITE+BBLACK,True)
        self.border_color = WHITE+BBLACK
        try:
            for n in range(0,len(args)):
                if isinstance(args[n],Point):
                    self.points.append(args[n])
                elif isinstance(args[n],int):
                    self.coords_color.append(args[n])
                elif isinstance(args[n], bool):
                    self.has_border = args[n]

            if len(self.points) == 2:
                if len(self.coords_color) > 1:
                    raise ValueError('You may not give coords integers and points')
                elif len(self.coords_color) == 1:
                    self.color = self.color_instance.sequence8(self.coords_color[0],True)

                self.a,self.b = self.points
                self.xpos,self.ypos = self.a.x,self.a.y
                self.hlen = self.b.x - self.a.x
                self.vlen = self.b.y - self.a.y
                if self.hlen < 1:
                    raise ValueError('Coords of point b must be highter than coords of coords point a for hlen.')
                if self.vlen < 1:
                    raise ValueError('Coords of point b must be highter than coords of coords point a for vlen.')
            elif len(self.coords_color) == 4:
                self.xpos,self.ypos,self.hlen,self.vlen = self.coords_color
            elif len(self.coords_color) == 5:
                self.xpos,self.ypos,self.hlen,self.vlen = self.coords_color[:-1]
                self.color = self.coords_color[-1]
            foreground = background = {} 
            for name in kws:
                if name == 'xpos':
                    if not isinstance(kws[name],int):
                        raise TypeError("xpos must be an integer.")
                    self.xpos = kws[name]
                elif name == 'ypos':
                    if not isinstance(kws[name],int):
                        raise TypeError("ypos must be an integer.")
                    self.ypos = kws[name]
                elif name == 'hlen':
                    if not isinstance(kws[name],int):
                        raise TypeError("hlen must be an integer.")
                    self.hlen = kws[name]
                elif name == 'vlen':
                    if not isinstance(kws[name],int):
                        raise TypeError("vlen must be an integer.")
                    self.vlen = kws[name]
                elif name == 'color':
                    fg = {}
                    bg = {}
                    themode=0
                    if isinstance(kws[name],int):
                        self.color = self.color_instance.sequence8(kws[name],True)
                    elif isinstance(kws[name],dict):
                        if 'fg' in kws[name].keys():
                            foreground = kws[name]['fg']
                        if 'bg' in kws[name].keys():
                            background = kws[name]['bg']
                        if 'mode' in kws[name].keys():
                            themode = kws[name]['mode']
                    if isinstance(foreground, int) and isinstance(background,int):
                        self.color = self.color_instance.sequence256bf(foreground,background,True)
                    elif isinstance(foreground,int):
                        self.color = self.color_instance.sequence256bf(foreground,None,True)
                    elif isinstance(background,int):
                        self.color = self.color_instance.sequence256bf(None,background,True)
                    elif isinstance(foreground, tuple) and len(foreground) > 0  and isinstance(background,tuple) and len(background) > 0:
                    #elif isinstance(foreground, tuple) and isinstance(background,tuple): 
                        
                        fg['r'],fg['v'],fg['b'] = foreground
                        bg['r'],bg['v'],bg['b'] = background

                        self.color = self.color_instance.sequencervb(fg,bg,True,mode=themode)
                    elif isinstance(foreground, tuple) and foreground == True:
                        fg['r'],fg['v'],fg['b'] = foreground
                        bg = {}
                        self.color = self.color_instance.sequencervb(fg,bg,True,mode=themode)
                    elif isinstance(background, tuple) and background == True:
                        fg = {}
                        bg['r'],fg['v'],fg['b'] = backround
                        self.color = self.color_instance.sequencervb(fg,bg,True)
                elif name == 'motif':
                    if not isinstance(kws[name],str):
                        raise TypeError("motif must be type str")
                    self.motif = kws[name]
                elif name == 'has_border':
                    if not isinstance(kws[name],bool):
                        raise TypeError("has_border must be a boolean.")
                    self.has_border = kws[name]
                elif name == 'is_void':
                    if not isinstance(kws[name],bool):
                        raise TypeError("is_void must be a boolean.")
                    self.is_void = kws[name]
                elif name == 'border_motif':
                    if not isinstance(kws[name],str):
                        raise TypeError("border_motif must be type str")
                    self.has_border = True
                    self.border_motif = kws[name]
                elif name == 'border_color':
                    if not isinstance(kws[name],int):
                        raise TypeError("border_color must be an integer")
                    self.has_border = True
                    self.border_color = kws[name]
                elif name == 'a':
                    if not isinstance(kws[name],Point):
                        raise TypeError("a must be a Point.")
                    self.a = kws[name]
                elif name == 'b':
                    if not isinstance(kws[name],Point):
                        raise TypeError("b must be a Point.")
                    self.b = kws[name]
                elif name == 'box':
                    if not isinstance(kws[name],int):
                        raise TypeError("box must be an integer.")
                    self.hasbox = True
                    self.box = kws[name] - 1
                elif name == 'parent':
                    if not isinstance(kws[name],Rectangle):
                        raise TypeError("parent box must be of type class Rectangle.")
                    self.parent =kws[name]
                else:
                    raise ValueError("unknow named parameter: '" + name + "' given.")

            if self.hasbox:
                self.has_border = False
                if self.border_motif != '+':
                    raise ValueError('You may not have border_motif with boxes.')

        except TypeError as te:
            raise
        except ValueError as ve:
            raise
        except:
            raise

        lines,cols = None,None
        addx,addy = 0,0 
        if self.parent is None:
            lines,cols = getTerminalSize()
        else :
            lines,cols = self.parent.vlen,self.parent.hlen
            addx,addy=self.parent.xpos,self.parent.ypos
        assert isinstance(lines,int),True
        assert isinstance(cols,int),True

        if self.hlen is None:
            self.hlen = cols
        if self.vlen is None:
            self.vlen = lines
        if self.xpos is None:
            self.xpos = cols//2 - self.hlen//2
        if self.ypos is None:
            self.ypos  = lines//2 - self.vlen//2 
        
        self.oxpos = self.xpos
        self.oypos = self.ypos
        if addx > 0:
            self.xpos += addx
        if addy > 0:
            self.ypos += addy


    def properties(self):
        print('xpos:',self.xpos)
        print('ypos:',self.ypos)
        print('hlen:',self.hlen)
        print('vlen:',self.vlen)
        print('motif:',self.motif)
        print('color:',self.color)
        print('box:',self.box)
        if self.has_border:
            print('border_motif:',self.border_motif)
            print('border_color:',self.border_color)

    def getproperties():
        pass

    def set_parent(self,parent):
        assert isinstance(parent,Rectangle),True
        assert isinstance(parent.hlen,int),True
        assert isinstance(parent.vlen,int),True
        assert isinstance(parent.xpos,int),True
        assert isinstance(parent.ypos,int),True
        
        lines,cols = parent.vlen,parent.hlen
        self.parent = parent

        if self.hlen is None:
            self.hlen = cols
        if self.vlen is None:
            self.vlen = lines
        if self.xpos is None:
            self.xpos = cols//2 - self.hlen//2
        if self.ypos is None:
            self.ypos  = lines//2 - self.vlen//2 


        self.xpos =  parent.xpos + int( (cols/2) - (self.hlen / 2) ) 
        self.ypos =  parent.ypos + int( (lines/2) - (self.vlen / 2) )

    def draw(self):
        gotoxy(self.xpos ,self.ypos )

        xpos,ypos,hlen,vlen = self.xpos,self.ypos,self.hlen,self.vlen
        c,b_color,s = None,None,None
        if self.has_border or self.hasbox:
            c = Color()
            b_color = c.sequence8(self.border_color,rstr = True)

        if self.has_border:
            h_border = self.border_motif * self.hlen
            v_border_right = (movedown_and_left(True) + self.border_motif) * (self.vlen - 1)
            v_border_left  = (self.border_motif + movedown_and_left(True) ) * (self.vlen - 1)
            s = (b_color + h_border + v_border_right + gotoxy(self.xpos,self.ypos,True) + v_border_left + h_border + c._(True))
        elif self.hasbox:
            h_border_top = self.boxes[self.box][UPLEFT] + self.boxes[self.box][HLINE] * (self.hlen - 2 ) + self.boxes[self.box][UPRIGHT]
            h_border_bottom = self.boxes[self.box][DWNLEFT] + self.boxes[self.box][HLINE] * (self.hlen - 2) + self.boxes[self.box][DWNRIGHT]
            v_border_right = (movedown_and_left(True) + self.boxes[self.box][VLINE]) * (self.vlen - 2)
            v_border_left = (self.boxes[self.box][VLINE] + movedown_and_left(True)) * (self.vlen - 2)
            s = (b_color + h_border_top + v_border_right + gotoxy(self.xpos,self.ypos + 1,True) + v_border_left + h_border_bottom + c._(True))

        if self.has_border or self.hasbox :
            print(s,end='')
            if self.is_void:
                return
            gotoxy(self.xpos + 1, self.ypos + 1)
            hlen -= 2
            vlen -= 2
            xpos += 1
            ypos += 1

        line = self.motif * hlen
        #bc = Color()
        #bc_color = bc.sequence8(self.color,True)
        #print('color:',self.color)

        bloc = self.color + line
        for n in range(1,vlen):
            bloc += (gotoxy(xpos,ypos + n,True) + line)
        bloc += self.color_instance._(True)
        print(bloc,end='',flush=True)

    def hide(self):
        return

    def show(self):
        return

