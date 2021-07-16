#!/usr/bin/python3
#New python script generation

import sys
import select
import tty, termios
import threading
import time

def loop():

    while loop_bool:
        if switch:
            output = 'aaaa'
        else:
            output = 'bbbb'
        print output
        time.sleep(0.2)


def change():
    global switch
    global loop_bool
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        while loop_bool:
            tty.setraw(fd)
            i,o,e = select.select([sys.stdin],[],[],1)
            if len(i)!=0:
                if i[0] == sys.stdin:
                    input = sys.stdin.read(1)

                    if input =='q':
                        if switch:
                            switch = False
                        else:
                            switch =  True


        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except KeyboardInterrupt:

        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        loop_bool = False


try:
    switch = True
    loop_bool = True
    t1=threading.Thread(target=loop)
    t2=threading.Thread(target=change)

    t1.start()
    t2.start()

    t1.join(1)
    t2.join(1)
except KeyboardInterrupt:

    loop_bool = False
