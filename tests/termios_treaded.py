#!/usr/bin/python3
import _thread
import time

def read_key():
    import termios
    import sys
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] &= ~(termios.ICANON | termios.ECHO) # c_lflags
    c = None
    try:
        termios.tcsetattr(fd, termios.TCSANOW, new)
        c = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old)
    return c

def input_thread():
    read_key()
    thread.interrupt_main()

def countup():
    try:
        thread.start_new_thread(input_thread, ())
        for i in range(1000000):
            print('i:',i)
            time.sleep(1)
    except KeyboardInterrupt:
        Z = raw_input("restart timer? ")
        if Z == 'y' or Z == 'Y':
            countup()

