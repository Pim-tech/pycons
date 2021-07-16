#!/usr/bin/python3
import os 
import sys
import termios

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = ''
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            while result != -1:
                result += sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


EOT = '\x04'  # CTRL+D
ESC = '\x1b'
CSI = '['

c = wait_key()
s = ''
while c != EOT:
    if c == ESC :
        print('PASS 1')
        if wait_key() == CSI:
            print('PASS 2')
            s = CSI + wait_key()
    else:
        print('PASS 3')
        s+=c
    print('s:',s)
    s=''
    c = wait_key()
    

print('exiting...')
