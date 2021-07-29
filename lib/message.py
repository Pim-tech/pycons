from lib.rectangle import *

class Message(Rectangle):

    def __init__(self,*args,**kws):
        self.textcolor = None
        self.c256 = False
        self.message = kws.pop('message') 
        if 'textcolor' in kws.keys():
            self.textcolor = kws.pop('textcolor')
        if 'c256' in kws.keys():
            self.c256 = kws.pop('c256') 
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
        super().draw()
        gotoxy(self.xpos_text,self.ypos_text)
        if self.textcolor is not None:
            if self.c256:
                if isinstance(self.textcolor,int):
                    Color().print256c(self.message,self.textcolor)
                elif isinstance(self.textcolor,dict):
                    bg = self.textcolor['bg']
                    fg = self.textcolor['fg']
                    Color().print256bf(self.message,fg,bg)
            else:
                #print('PASSS')
                assert isinstance(self.textcolor,int), True 
                Color().print(self.message,self.textcolor)
        else:
            print(self.message,flush=True,end='')


