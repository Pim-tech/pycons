
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
        except IndexError as ie:
            exit(str(ie))
        except:
            exit('An exception occured.')

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
        for tx in range(len(self.buffer)):
            if self.buffer[tx] is not None:
                for ty in range(len(self.buffer[tx])):
                    if self.buffer[tx][ty] is not None:
                        self.__setbuffer(self.xy,tx,ty)
                        self.__setbuffer(self.yx,ty,tx)

    def __setbuffer(self,thebuffer,a,value):
        for i in range(a+1):
            if len(thebuffer) <= i:
                thebuffer.append(None)
        thebuffer[i] = value

    def __set2dbuffer(self,x,y,value,thebuffer = None):
        if thebuffer is None:
            thebuffer = self.buffer
        for n in range(x):
            if len(thebuffer) <= n:
                thebuffer.append([]);
        for k in range(y):
            if len(thebuffer[n]) <= k:
                thebuffer[n].append(None)
        thebuffer[n][k]=value

    def load_value(self,*args,**kws) -> bool: 
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

        except IndexError as ie:
            exit(str(ie))
        except ValueError as v:
            exit(str(v))
        except:
            exit("Unexpected error:")

        if p is None:
            p = Point(x,y)

        if value is None:
            self.__set2dbuffer(x,y,p)
        else:
            self.__set2dbuffer(x,y,value)

        return True
        

    def get_value(self,x: int,y: int):
        if not len(self.buffer) >= x or not len(self.buffer[x - 1]) >= y :
            return None
        return self.buffer[x - 1][ y - 1] 

    def for_xrange_aty(self,y: int,x1: int,x2 = None,sens = 1):
        try:
            yindices = self.yx[y - 1]
            nextindice = yindices.index(x - 1) + sens
            xnextindice = yindices[nextindice]
            if x2 is not None:
                if self.buffer[xnextindice][y - 1] is not None and (x2 - 1) > xnextindice:
                    return self.buffer[xnextindice][y - 1]
                else:
                    return None
            else:
                if self.buffer[xnextindice][y - 1] is not None:
                    return self.buffer[xnextindice][y - 1]
                else:
                    return None
        except IndexError as ie:
            exit(str(ie))
        except ValueError as v:
            exit(str(v))
        except:
            exit("Unexpected error")

    def for_yrange_atx(self):
        try:
            xpoints = self.buffer[x - 1]
            nextone = self.xy[x - 1].index(y - 1) + 1
            next_indice = self.xy[nextone]
            if y2 is not None:
                if ypoints[next_indice] and (y2 - 1) > next_indice:
                    return ypoints[next_indice]
                return None;
            if ypoints[next_indice] is not None:
                return ypoints[next_indice]
        except IndexError as ie:
            exit(str(ie))
        except ValueError as v:
            exit(str(v))
        except:
            exit('Unexpected Error.')
         

    def showbuf(self):
        print('buffer:',self.buffer)

