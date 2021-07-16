
import sys
import termios
import contextlib
from lib.keyboards.current import *

class Events:
    def __init__(self,events: dict,quit = 'Q',show_key = False):
        self.e_dict = events
        self.key_exit = quit
        self.show_key = show_key
        self.wait()

    @contextlib.contextmanager
    def raw_mode(self,sfile):
        old_attrs = termios.tcgetattr(sfile.fileno())
        new_attrs = old_attrs[:]
        new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(sfile.fileno(), termios.TCSADRAIN, new_attrs)
            yield
        finally:
            termios.tcsetattr(sfile.fileno(), termios.TCSADRAIN, old_attrs)

    def add_event(self):
        return

    def get_key(self):
        try:
            ch = sys.stdin.read(1)
            if not ch or ch == chr(4):
                return None 
            c = ord(ch)
            if c < 0x1b:
                if len(special_key_string[c - 1]) > 0:
                    return special_key_string[c - 1]
            if c == 0x7f:
                return function_key_strings[24] 
            if c == 0x1b:
                s=''
                while len(s) < 5:
                    cc = sys.stdin.read(1)
                    if ord(cc) == 0x1b:
                        continue
                    s += cc 
                    if s in function_keys:
                        return function_key_strings[function_keys[s] - 1] 
                        s=''
                        break
                s=''
            return ch
        except (KeyboardInterrupt, EOFError):
            pass

    def wait(self):
        with self.raw_mode(sys.stdin):
            ik = self.get_key() 
            while ik:
                if self.show_key:
                    print('You pressed:',ik)
                if self.key_exit and ik == self.key_exit:
                    break
                if ik in self.e_dict:
                    sub = self.e_dict[ik]
                    sub()
                ik = self.get_key() 

    def terminate(self):
        sys.exit(0)
