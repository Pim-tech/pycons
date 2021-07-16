#!/usr/bin/python3
#New python script generation

from lib.Events import *
from lib.Rectangle import *
from lib.Colors import *

r6 = Rectangle(Point(20,40),Point(60,80),box = HEAVY, border_color = LWHITE+BCYAN, color = WHITE+BRED, motif = "\N{DARK SHADE}");
def on_activate_page_up():
    print('Page UP')

def on_activate_page_down():
    print('Page DOWN')

def on_activate_letter_a():
    print('Letter a')

def quit_prg():
    print('On sort!')
    sys.exit(0)

def r_sub():
    print("This is r_sub.")


evts = { '<page_up>' : on_activate_page_up,
    '<page_down>': on_activate_page_down,
    'a'        : on_activate_letter_a,
    'r'        : r_sub
    }

e = Events(evts)

#e.add_event('R',r6,'draw')


#e.listen()
