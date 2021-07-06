import sys
from  lib import constant

def sprint(s):
    return s

def nocursor(rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + '?25l')

def cursor(rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + '?25h')

def gotoxy(x: int, y: int,rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + str(y) + ';' + str(x) + 'H')

def move_up(n: int,rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + str(n) + 'A')
 
def move_down(n: int,rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + str(n) + 'B')
 
def move_right(n: int,rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + str(n) + 'C')

def move_left(n: int,rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + str(n) + 'D')

def clear_screen(rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + '2J')

def erase(n: int,rstr=False) -> str:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + str(n) + 'X')

def moveup_and_left(rstr=False) -> int:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + '1A' + constant.STARTSEQ + '1D')

def move_up_and_left(up: int,left: int,rstr=False) -> int:
    prnt = lambda a: print(a) if not rstr else lambda a: a
    return prnt(constant.STARTSEQ + str(up) + 'A' + constant.STARTSEQ + str(left) + 'D')

#def move_down_and_left(Bool $rstr=False) {
#    my $print = ($rstr == False) ?? &printf !! &sprintf;
#    return $print(STARTSEQ ~ "1B" ~ STARTSEQ ~ "1D");
#}
#
#multi move_down_and_left(Int $down,Int $left,Bool $rstr=False){
#    my $print = ($rstr == False) ?? &printf !! &sprintf;
#    return $print( STARTSEQ ~ "%dB" ~ STARTSEQ ~ "%dD",$down,$left);
#}
#
#sub print_the_string( Str $s ) {
#     print $s;
#}
#sub return_the_string(Str $s ) {
#    return $s;
#} 

