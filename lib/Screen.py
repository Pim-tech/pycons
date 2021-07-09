
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
    #x and y may be given these way:
    # Point(1,2)
    # t = (1,2)
    # Point(t)
    # or the tuple may be a literal tuple:
    # Point((1,2))
    # or in named parameters:
    # Point(x=1,y=2)
    # Additionnal parameter flagconst is falcultative
    # Point(1,2,'CLOSED')
    # or :
    # Point(1,2 flagconst = 'CLOSED')
    # also:
    # Point(x = 1, y = 2, flagconst = 'CLOSED')
    # Since you give a named parameter all the one that follow must be named too
    #
    def __init__(self,*args,**kws):

        self.flags = 0
        self.flagconst = ''
        self.prev = None
        self.next = None
        self.rect = None
        self.mis  = None
        self.direction = None

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
                        self.flagconst = args[2]
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
                elif name == 'flagconst':
                    if isinstance(kws[name],str):
                        self.flagconst = kws[name]
                    else:
                        raise ValueError('setflag must be of type str.')
                else:
                    raise ValueError("unknown named parameter '" + name + "'")

        except ValueError as v:
            exit(str(v))

        if self.flagconst:
            self.setflag(self.flagconst)
    
    #Rise a flag
    def setflag(self,flag):
        self.flags = eval('self.flags | ' + flag)
        if flag == 'CONVEXE':
            self.flags = self.flags & ( CONCAVE ^ FLAGMASK)
        if flag == 'CONCAVE':
            self.flags = self.flags & ( CONVEXE ^ FLAGMASK)
        if flag == 'LINE':
            self.flags = self.flags & (CONCAVE ^ FLAGMASK)
            self.flags = self.flags & (CONVEXE ^ FLAGMASK)
        return self.flags

    #disable a flag
    def unsetflag(self,flag: str):
        self.flags = eval('self.flags & (' + flag + ' ^ FLAGMASK )' )
        return self.flags

    #Return is True if flag is enabled otherwise False
    def hasflag(self,flag: str):
        return bool(eval('(self.flags & ' + flag + ')'))

    #Show flags and the last flagconst status
    def show(self):
        print('x:',self.x,'y:',self.y)
        if self.flagconst:
            print('flagconst:',self.flagconst)
        if self.flags:
            print('flags:',self.flags)

    #Return a string of x and y current coordinates
    def tostr():
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)

    #move the cursor point to its x and y position
    def fix(self):
        gotoxy(self.x,self.y)

class ScreenBuffer:

    def __init__(self):
        self.buffer = []
        self.xy     = []
        self.yx     = []

    def make_indices(self):
        self.xy     = []
        self.yx     = []

#        for tx in range(0,len(self.buffer)):
#            if self.buffer[tx]:
#                ally = self.buffer[tx]

        return
    def __setbuffer(self,x,y,value):
        for n in range(x):
            if len(self.buffer) <= n:
                self.buffer.append([]);
        for k in range(y):
            if len(self.buffer[n]) <= k:
                self.buffer[n].append(None)
        self.buffer[n][k]=value

    def load_value(self,*args,**kws): 
        x = None
        y = None
        p = None
        inext = 0
        value = None
        push = False
        try:
            if len(args) and isinstance(args[0],Point):
                p = args[0]
                inext +=  1
                x,y = p.x,p.y 
            elif len(args) and isinstance(args[0],int):
                x = args[0]
                inext += 1
                if len(args) > 1 and isinstance(args[1],int):
                    y =args[1]
                    inext += 1
            if len(args) > inext:
                value = args[inext]

            for name in kws:
                if name == 'x' or name == 'y':
                    if isinstance(kws[name],int):
                        if name == 'x':
                            x = kws['x']
                        elif name == 'y':
                            y = kws['y']
                    else:
                        raise ValueError('Positionals x and y must be int.')
                elif name == 'pt' or name == 'p':
                    p = kws[name] 
                    x,y =p.x,p.y
                elif name == 'value':
                    value = kws[name] #we cannot control type here

        except ValueError as v:
            exit(str(v))

        if p is None:
            p = Point(x,y)

        if value is None:
            self.__setbuffer(x,y,p)
        else:
            self.__setbuffer(x,y,value)
        

    def get_value(self,x: int,y: int):
        return self.buffer[x - 1, y - 1] 

    def for_xrange_aty(self):
        return 

    def for_yrange_atx(self):
        return

    def get_xy(self,x: int) -> int:
        return self.xy[x - 1]

    def get_yx(self,y: int) -> int:
        return self.yx[y - 1]
            
    def showbuf(self):
        print('buffer:',self.buffer)

