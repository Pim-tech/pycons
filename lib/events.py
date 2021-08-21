
import sys
import termios
import signal
import contextlib

#This is the keyboard map, this could/will be customized later
from lib.keyboards.current import *

class KbEvents:
    def __init__(self,events: dict,quit = '',show_key = False,withthreads=False):
        self.e_dict = events
        self.key_exit = quit
        self.show_key = show_key
        self.close_properly = False
        self.withthreads = False
        self.treads = []
        
        if withthreads:
            self.withthreads = withthreads 
        
        signal.signal(signal.SIGINT,self.signal_handler)

        if self.withthreads:
            self.run_threads()
        else:
            self.wait_key(None,None)


    @contextlib.contextmanager
    def raw_mode(self,sfile):
        self.sfile = sfile
        self.old_attrs = termios.tcgetattr(self.sfile.fileno())
        new_attrs = self.old_attrs[:]
        new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(self.sfile.fileno(), termios.TCSADRAIN, new_attrs)
            yield
        finally:
            termios.tcsetattr(self.sfile.fileno(), termios.TCSADRAIN, self.old_attrs)

    #TODO: to add an event afterwords.
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

    def signal_handler(self,sig, frame):
        print('You pressed Ctrl+C!')
        termios.tcsetattr(self.sfile.fileno(), termios.TCSADRAIN, self.old_attrs)
        sys.exit(0)
        

    def wait_key(self,threadname,q):
        with self.raw_mode(sys.stdin):
            ik = self._get_key() 
            while ik:
                if self.show_key:
                    print('You pressed:',ik)
                if self.key_exit and ik == self.key_exit:
                    if self.withthreads == True:
                        q.put('EXIT')
                    break
                if ik in self.e_dict:
                    if self.withthreads == True:
                        q.put(ik)
                    else:
                        sub = self.e_dict[ik]
                        sub()
                ik = self._get_key() 
                if ik is None:
                    q.put('EXIT')
                    break


    def dothejob(self,threadname, q):
        from queue import Empty
        from time import sleep
        #c = 0
        self.q=q
        while True:
            sleep(0.1) #slow the loop down
            ch = None
            try:
                ch = q.get(block=False)
            except Empty:
                pass
            except (KeyboardInterrupt):
                pass
            
            if ch is not None:
                if self.show_key:
                    print('Catched key:',ch)
                if self.close_properly or ch == 'EXIT':
                    break
                if ch in self.e_dict:
                    sub = self.e_dict[ch]
                    sub()


    def run_threads(self):
        from threading import Thread
        from queue import Queue
        queue = Queue()
        self.thread1 = Thread( target=self.wait_key,args=("WaitKey",queue) )
        self.thread2 = Thread( target = self.dothejob,args=('JobTask',queue) )

        self.thread2.daemon = True
        self.thread1.daemon = True
        self.thread1.start()
        self.thread2.start()
        self.thread1.join()
        self.thread2.join()



