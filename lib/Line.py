
from Screen import *
import lib.constant
import sys

class Line:

    def __init__(slef,*args,**kws):
        self.a = None
        self.b = None
        self.motif = None
        self.direction= None
        self.origin = None
        self.destination = None
        self.prec = None
        self.ia = None
        self.ib = None

        try:
            for n in range(0,len(args)):
                if isinstance(args[n],tuple)):
                    if len(args[n)) > 2:
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
               elif name == 'direction':
                    if not isinstance(kws[name],str):
                        raise TypeError('direction must be an str.')
                    self.direction = kws[name]
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

    def get_coords(self):
        return

    def str(self) -> str:
        return

    def has_point(pt) -> bool:
        return

    def draw():
        return

    def show():
        return

    def hide():
        return
