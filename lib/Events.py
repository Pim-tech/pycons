
import sys
import termios
import contextlib


class Events:
    def __init__(self,events: dict,quit = 'Q'):
        self.e_dict = events
        self.key_exit = quit


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

    def add_event(self):
        return

    def wait(self):
        with raw_mode(sys.stdin):
            try:
                s=''
                while True:
                    ch = sys.stdin.read(1)
                    if not ch or ch == chr(4):
                        break
                    if ch == "\x1b":
                        continue 
                        s += ch
                    print('s:',s)


    

    def terminate(self):
        sys.exit(0)
