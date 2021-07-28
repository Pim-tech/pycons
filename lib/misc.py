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

def getTerminalSize():
    """
    returns (lines:int, cols:int)
    """
    import os, struct
    def ioctl_GWINSZ(fd):
        import fcntl, termios
        return struct.unpack("hh", fcntl.ioctl(fd, termios.TIOCGWINSZ, "1234"))
    # try stdin, stdout, stderr
    for fd in (0, 1, 2):
        try:
            return ioctl_GWINSZ(fd)
        except:
            pass
    # try os.ctermid()
    try:
        fd = os.open(os.ctermid(), os.O_RDONLY)
        try:
            return ioctl_GWINSZ(fd)
        finally:
            os.close(fd)
    except:
        pass
    # try `stty size`
    try:
        return tuple(int(x) for x in os.popen("stty size", "r").read().split())
    except:
        pass
    # try environment variables
    try:
        return tuple(int(os.getenv(var)) for var in ("LINES", "COLUMNS"))
    except:
        pass
    # i give up. return default.
    return (25, 80)
