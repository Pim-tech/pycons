#!/usr/bin/python3
def terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return w, h,hp,wp

w,h,hp,wp = terminal_size()
print('w:',w,'h:',h)
