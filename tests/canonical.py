

@contextlib.contextmanager
def decanonize(fd):
    old_settings = termios.tcgetattr(fd)
    new_settings = old_settings[:]
    new_settings[3] &= ~termios.ICANON
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_settings)
    yield
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_settings)


def change():
    global switch
    global loop_bool

    with decanonize(sys.stdin.fileno()):
        try:
            while loop_bool:
                i,o,e = select.select([sys.stdin],[],[],1)
                if i and i[0] == sys.stdin:
                    input = sys.stdin.read(1)
                    if input =='q':
                        switch = not switch
        except KeyboardInterrupt:
            loop_bool = False
