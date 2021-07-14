
from lib.Screen import *
import lib.constant
from lib.Misc import *


class Line:

    #You may give points:
    #Line(a = Point(a),b = Point(b),[motif = 'x'])
    #or
    #Line(Point(a),Point(b),[motif='x'])
    
    #You may give tuples: like this
    #Line(ia = (x1,y1),ib = (x2,y2))
    #or
    #Line((x1,y1),(x2,y2),[motif ='x'] )
    #
    def __init__(self,*args,**kws):
        self.a = None
        self.b = None
        self.motif = '*' 
        self.direction= None
        self.origin = None
        self.destination = None
        self.prec = None
        self.ia = None
        self.ib = None

        try:
            for n in range(0,len(args)):
                if isinstance(args[n],tuple):
                    if len(args[n]) > 2:
                        raise ValueError('Tuple must contain 2 elements max.')
                    if n == 0:
                        self.ia = args[n];
                        if not isinstance(args[n][0],int):
                            raise TypeError('Tuple first argument must be an int.')
                        if not isinstance(args[n][1],int):
                            raise TypeError('Tuple second argument must be an int.')
                        self.a = Point(args[n][0],args[n][1])
                    elif n == 1:
                        self.ib = args[n]
                        if not isinstance(args[n][0],int):
                            raise TypeError('Tuple first argument must be an int.')
                        if not isinstance(args[n][1],int):
                            raise TypeError('Tuple second argument must be an int.')
                        self.b = Point(args[n][0],args[n][1])
                elif isinstance(args[n], Point):
                    if n == 0:
                        self.a = args[n] 
                    elif n == 1:
                        self.b = args[n]

            for name in kws:
                if name == 'a':
                    if not isinstance(kws[name],Point):
                        raise TypeError("a must be a Point.")
                    self.a = kws[name]
                elif name == 'b':
                    if not isinstance(kws[name],Point):
                        raise TypeError("b must be a Point.")
                    self.a = kws[name]
                elif name == 'prec':
                    if not isinstance(kws[name],Line):
                        raise TypeError('prec must be a Line object.')
                    self.prec = kws[name]
                elif name == 'ia':
                    if not isinstance(kws[name],list):
                        raise TypeError('ia must be a list of 2 int.')
                    self.ia =kws[name]
                elif name == 'ib':
                    if not isinstance(kws[name],list):
                        raise TypeError('ib must be a list of 2 int.')
                    self.ib =kws[name]
                elif name == 'origin':
                    if not isinstance(kws[name],Point):
                        raise TypeError("origin must be a Point.")
                    self.origin = kws[name]
                elif name == 'destination':
                    if not isinstance(kws[name],Point):
                        raise TypeError("destination must be a Point.")
                    self.destination = kws[name]
                elif name == 'motif':
                    if not isinstance(kws[name],str):
                        raise TypeError("'motif' must ben a str.")
                    self.motif = kws[name]

        except TypeError as te:
            raise
        except ValueError as ve:
            raise
        except:
            raise

        if self.a.x != self.b.x:
            self.direction = 'h'
            assert(self.a.y != self.b.y)
            if self.a.y > self.b.y: 
                self.origin = self.b
                self.destination = self.a
            elif self.b.y > self.a.y:
                self.origin = self.a
                self.destination = self.b
        elif self.b.y != self.a.y:
            self.direction = 'v'
            if self.a.y > self.b.y:
                self.origin = self.b
                self.destination = self.a
            elif self.b.y > self.a.y:
                self.origin = self.a
                self.destination = self.b

    def print_coords(self):
        print('xa:',self.a.x,'ya:',self.a.y,'xb:',self.b.x,'yb:',self.b.y)
        print('direction:',self.direction)
        print('origin:',self.origin.x,self.origin.y)
        print('destination:',self.destination.x,self.destination.y)

    def str(self) -> str:
        return

    def has_point(pt) -> bool:
        

        return

    def draw(self):
        n = 0
        s = ''
        self.origin.fix()
        if self.direction == 'h':
            n = self.destination.x - self.origin.x
            s = self.motif * (n - 1)
        elif self.direction == 'v':
            n = self.destination.y - self.origin.y
            s = (self.motif + movedown_and_left(True)) * (n + 1)
        print(s,end='')

    def show():
        return

    def hide():
        return
