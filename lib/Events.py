
import sys
import termios
import contextlib
from lib.keyboards.current import *

class KbEvents:
    def __init__(self,events: dict,quit = 'Q',show_key = False,threads=False):
        self.e_dict = events
        self.key_exit = quit
        self.show_key = show_key
        self.threads = threads 
        if self.threads == False:
            self.wait_key(None)
        else:
            self.run_threads()

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

    def _get_key(self):
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

    def wait_key(self,threadname,q):
        with self.raw_mode(sys.stdin):
            ik = self._get_key() 
            while ik:
                if self.show_key:
                    print('You pressed:',ik)
                if self.key_exit and ik == self.key_exit:
                    break
                if ik in self.e_dict:
                    if self.threads == True:
                        q.put(ik)
                    else:
                        sub = self.e_dict[ik]
                        sub()
                ik = self._get_key() 

    def dothejob(self,threadname, q):
        from queue import Empty
        from time import sleep
        c = 0
        while True:
            sleep(0.1) #slow the loop down
            c += 1
            #print(c)
            #Below is the changed part
            ch = None
            try:
                ch = q.get(block=False)
            except Empty:
                pass
            if ch is not None:
                if self.show_key:
                    print('Catched key:',ch)
                if ch in self.e_dict:
                    sub = self.e_dict[ch]
                    sub()


    def run_threads(self):
        from threading import Thread
        from queue import Queue
        queue = Queue()
        thread1 = Thread( target=self.wait_key,args=("Thread-1",queue) )
        thread2 = Thread( target = self.dothejob,args=('Thread-2',queue) )

        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()



