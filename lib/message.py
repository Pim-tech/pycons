from lib.rectangle import *

class Message(Rectangle):

    def __init__(self,*args,**kws):
        self.message = kws.pop('message') 
        if not 'hlen' in  kws.keys():
            lines,cols = getTerminalSize()
            kws['hlen'] = int(cols//6.32)
        if not 'vlen' in kws.keys():
            lines,cols = getTerminalSize()
            kws['vlen'] = int(lines//7)
        if not 'box' in kws.keys():
            kws['box'] = SIMPLE
        if not 'motif' in kws.keys():
            kws['is_void'] = True
        super(Message,self).__init__(*args,**kws)
        self.xpos_text = self.xpos + int(self.hlen // 2) - int(len(self.message)//2)
        self.ypos_text = self.ypos + int(self.vlen // 2) 


    def draw(self):
        gotoxy(self.xpos_text,self.ypos_text)
        print(self.message,end='')
        super().draw()


