
from lib.Misc import * 
from lib.Colors import *
from lib.Screen import *
import sys

class Border:
    def __init__(self):
        self.motif = 'x'
        self.color = WHITE+BBLACK

class Rectangle:
    def __init__(self,*args,**kws):
        self.motif = '*'
        self.color = WHITE+BBLACK
        self.has_border = False
        self.border_motif = '+'
        self.border_color = WHITE+BBLACK
        self.box = 0
        self.points = []
        self.coords_color = []
        self.hlen = None
        self.vlen = None
        self.a = None
        self.b = None

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
        ]
        ]
        
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
                    self.color = self.coords_color[0]

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
                    self.xpos,self.ypos,self.hlen,self.vlen,self.color = self.coords_color

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
                    if not isinstance(kws[name],int):
                        raise TypeError("color must be an integer.")
                    self.color = kws[name]
                elif name == 'motif':
                    if not isinstance(kws[name],str):
                        raise TypeError("motif must be type str")
                    self.motif = kws[name]
                elif name == 'has_border':
                    if not isinstance(kws[name],bool):
                        raise TypeError("has_border must be a boolean.")
                    self.has_border = kws[name]
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
                    if self.border_motif != '+':
                        raise ValueError('You may not have border_motif with boxes.')
                    self.box = kws[name]
                else:
                    raise ValueError("unknow named parameter: '" + name + "' given.")
        except TypeError as te:
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            string = 'Exception occured in {} at line {}: ' .format(f.f_code.co_filename,tb.tb_lineno,exc_obj)
            exit(string + str(te))
        except ValueError as ve:
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            string = 'Exception occured in {} at line {}:' .format(f.f_code.co_filename,tb.tb_lineno,exc_obj)
            exit(string + str(ve))
        except:
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            string = 'Unknown Exception occured in {} at line {}: ' .format(f.f_code.co_filename,tb.tb_lineno,exc_obj)
            exit(string)

    def show(self):
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
    def draw(self):
        gotoxy(self.xpos ,self.ypos )

        xpos,ypos,hlen,vlen = self.xpos,self.ypos,self.hlen,self.vlen
        c,b_color,s = None,None,None
        if self.has_border or self.box > 0:
            c = Colors()
            b_color = c.sequence8(self.border_color,rstr = True)
        if self.has_border:
            h_border = self.border_motif * self.hlen
            v_border_right = (move_down_and_left(True) + self.border_motif) * (self.vlen - 1)
            v_border_left  = (self.border_motif + move_down_and_left(True) ) * (self.vlen - 1)
            s = (b_color + h_border + v_border_right + gotoxy(self.xpos,self.ypos,True) + v_border_left + h_border + c._(True))
        elif self.box > 0:
