#!/usr/bin/python3
#New python script generation
import sys
import termios
import contextlib
import select
from lib.keyboards.current import *


@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


print('exit with ^C or ^D')
with raw_mode(sys.stdin):
    try:
        while True:
            ch = sys.stdin.read(1)
            if not ch or ch == chr(4):
                break
            c = ord(ch)
            if c < 0x1b:
                if len(special_key_string[c - 1]) > 0:
                    print("You hit key:",special_key_string[c - 1])
                continue
            if c == 0x7f:
                print('You hit key:,','BackSpace') 
                continue
            elif c == 0x1b:
                s=''
                while len(s) < 5 :
                    cc = sys.stdin.read(1)
                    if ord(cc) == 0x1b:
                        continue
                    s += cc 
                    if s in function_keys:
                        print('You hit key:',function_key_strings[function_keys[s] - 1])
                        break
                
                if len(s) == 0:
                    print('ECHAP')
                    s = 'ESC'
                else:
                    s=''
                    continue
            print('You hit key:',ch)
    except (KeyboardInterrupt, EOFError):
        pass


