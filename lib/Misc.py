import sys
from  lib import constant

def sprint(s):
    return s

def nocursor(rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + '?25l')

def cursor(rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + '?25h')

def gotoxy(x: int, y: int,rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + str(y) + ';' + str(x) + 'H')

def move_up(n: int,rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + str(n) + 'A')
 
def move_down(n: int,rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + str(n) + 'B')
 
def move_right(n: int,rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + str(n) + 'C')

def move_left(n: int,rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + str(n) + 'D')

def clear_screen(rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + '2J')

def erase(n: int,rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + str(n) + 'X')

def moveup_and_left(rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + '1A' + constant.STARTSEQ + '1D')

def move_up_and_left(up: int,left: int,rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + str(up) + 'A' + constant.STARTSEQ + str(left) + 'D')

def movedown_and_left(rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + '1B' + constant.STARTSEQ + '1D')

def move_down_and_left(down: int,left: int,rstr=False) -> str:
    prnt=(lambda a: a) if rstr else (lambda a: print(a,end=''))
    return prnt(constant.STARTSEQ + str(down) + 'B' + constant.STARTSEQ + str(left) + 'D')
