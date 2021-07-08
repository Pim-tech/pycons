
from lib.Misc import *

LINE      = 0b0000000000000001
CONCAVE   = 0b0000000000000010
DIAGONALE = 0b0000000000000100
MIS       = 0b0000000000001000
RECTANGLE = 0b0000000000010000
CONVEXE   = 0b0000000000100000
MARKED    = 0b0000000001000000
OPEN      = 0b0000000010000000
CLOSED    = 0b0000000100000000
FLAGMASK  = 0b1111111111111111

class Point:
    def __init__(self,*args,**kws):
        self.flags = 0
        self.setflag = ''
        try:
            for n in range(0,len(args)):
                if isinstance(args[n], tuple):
                    for t in range(0,len(args[n])):
                        if isinstance(args[n][t],int):
                            if t == 0:
                                self.x = args[n][t]
                            elif t == 1:
                                self.y = args[n][t]
                            elif t > 1:
                                raise ValueError('Tuple must contain 2 elements max.')
                        else:
                            raise ValueError('Each type in tuple must be int.')
                elif n < 2:
                    if isinstance(args[n],int):
                        if n == 0:
                            self.x = args[0]
                        elif n == 1:
                            self.y = args[1]
                    else:
                        raise ValueError('x and y must be int.')
                elif n == 2:
                    if isinstance(args[2],str):
                        self.setflag = args[2]
                    else:
                        raise ValueError('Third parameter setflag must be typed str.')
                elif n > 2:
                    raise ValueError("Extra parameter '" + args[n] + "' given.")
        
            for name in kws:
                if name == 'x' or name == 'y':
                    if isinstance(kws[name],int):
                        if name == 'x':
                            self.x = kws['x']
                        elif name == 'y':
                            self.y = kws['y']
                    else:
                        raise ValueError('Positionals x and y must be int.')
                elif name == 'setflag':
                    if isinstance(kws[name],str):
                        self.setflag = kws[name]
                    else:
                        raise ValueError('setflag must be of type str.')
                else:
                    raise ValueError("unknown named parameter '" + name + "'")

        except ValueError as v:
            exit(str(v))

    def setflag(self,flag: str):
        self.flags = eval('self.flags | ' + flag )
        if flag == 'CONVEXE':
            self.flags = self.flags & ( CONCAVE ^ FLAGMASK)
        if flag == 'CONCAVE':
            self.flags = self.flags & ( CONVEXE ^ FLAGMASK)
        if flag == 'LINE':
            self.flags = self.flags & (CONCAVE ^ FLAGMASK)
            self.flags = self.flags & (CONVEXE ^ FLAGMASK)

    def unsetflag(flag: str):
        self.flags = eval('self.flags & (' + flag + ' ^ FLAGMASK )' )

    def hasflag(flag: str):
        return eval('(self.flags & ' + flag + ')')

    def show(self):
        print('x:',self.x,'y:',self.y)
        if self.setflag:
            print('setflag:',self.setflag)


    def tostr():
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)

    def fix():
        gotoxy(self.x,self.y)

