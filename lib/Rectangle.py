
from lib.Misc import * 
from lib.Colors import *
from lib.Screen import *

class Border:
    __init__(self):
        self.motif = 'x'
        self.color = WHITE+BBLACK

class Rectangle:
    __init__(self,*args,*kws):
        self.motif = '*'
        self.color = WHITE+BBLACK
        self.has_border = False
        self.border_motif = '*'
        self.border_color = WHITE+BBLACK
        self.blox = 0
        self.points = []
        self.coords_color = []

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
            elif len(self.coords_color) == 4:
                self.xpos,self.ypos,self.hlen,self.vlen = self.coords_color
            elif len(self.coords_color) == 5:
                    self.xpos,self.ypos,self.hlen,self.vlen,self.color = self.coords_color

            for name in kws:
                if name == 'xpos':
                    if not isinstance(kws[name],int):
                        raise TypeError("Coords must be integers")
                    self.xpos = kws[name]
                elif name == 'ypos':
                    if not isinstance(kws[name],int):
                        raise TypeError("Coords must be integers")
                    self.ypos = kws[name]
                elif name == 'hlen':
                    if not isinstance(kws[name],int):
                        raise TypeError("Coords must be integers")
                    self.hlen = kws[name]
                elif name == 'vlen':
                    if not isinstance(kws[name],int):
                        raise TypeError("Coords must be integers")
                    self.vlen = kws[name]
                elif name == 'color':
                    if not isinstance(kws[name],int):
                        raise TypeError("Color must be an integer")
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
                    self.border_motif = kws[name]
                elif name == 'border_color':
                    if not isinstance(kws[name],int):
                        raise TypeError("border_color must be an integer")
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
                    self.box = kws[name]
        except TypeError as te:
            exit(str(te))
        except ValueError as ve:
            exit(str(ve))
        except:
            exit('Unknown Exception occured.')








                    

