#!/usr/bin/env python3

def handle_keypress(key):
    if (key == "q"):
        print("Quit thread")
        exit(0)
    elif (key == "s"):
        print("would you like to change the step size? This has not been implemented yet.\n")
    else:
        print("you pressed another key, how nice! Unfortunately, there are not anymore options available yet.\n")

def job(threadname, q):
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
            handle_keypress(ch)

def get_input(threadname, q):
    #get one character, this code is adapted from https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
    import sys, tty, termios
    while True:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        q.put(ch)

def run_program():
    from threading import Thread
    from queue import Queue
    queue = Queue()
    thread1 = Thread( target=get_input, args=("Thread-1", queue) )
    thread2 = Thread( target=job, args=("Thread-2", queue) )
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


run_program()
