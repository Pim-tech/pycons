from lib.rectangle import *

class Message(Rectangle):

    def __init__(self,*args,**kws):
        self.textcolor = None
        self.confirm   = None
        self.c256 = False
        self.ypos_confirm =  self.xpos_confirm = None
        self.message = kws.pop('message') 
        if 'textcolor' in kws.keys():
            self.textcolor = kws.pop('textcolor')
        if 'c256' in kws.keys():
            self.c256 = kws.pop('c256') 
        if 'confirm' in kws.keys():
            self.confirm = kws.pop('confirm') 
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
        if self.confirm is None:
            self.xpos_text = self.xpos + int(self.hlen // 2) - int(len(self.message)//2)
            self.ypos_text = self.ypos + int(self.vlen // 2) 
        else:
            self.xpos_text = self.xpos + int(self.hlen // 2) - int(len(self.message)//2)
            self.ypos_text = self.ypos + int(self.vlen // 2) - 1
            self.xpos_confirm = self.xpos + int(self.hlen // 2) - int(len(self.confirm)//2)
            self.ypos_confirm = self.ypos+self.vlen - 2


    def draw(self):
        super().draw()
        gotoxy(self.xpos_text,self.ypos_text)
        color = Color()
        if self.textcolor is not None:
            if self.c256:
                if isinstance(self.textcolor,int):
                    color.print256c(self.message,self.textcolor)
                elif isinstance(self.textcolor,dict):
                    bg = self.textcolor['bg']
                    fg = self.textcolor['fg']
                    color.print256bf(self.message,fg,bg)
            else:
                assert isinstance(self.textcolor,int), True 
                color.print(self.message,self.textcolor)
        else:
            print(self.message,flush=True,end='')

        gotoxy(self.xpos_confirm,self.ypos_confirm)
        if self.confirm:
            if isinstance(self.confirm,str):
                assert isinstance(self.xpos_confirm,int),True
                assert isinstance(self.ypos_confirm,int),True
                color.print(self.confirm,LWHITE+BRED)
            elif  isinstance(self.confirm,dict):
                if 'm' in self.confirm.keys():
                    assert isinstance(self.confirm['m'],str),True
                    if 'color' in self.confirm.keys():
                        assert isinstance(self.confirm['color'],int),True
                        color.print256c(self.confirm['m'],self.confirm['color'])
                    elif 'bg' in self.confirm.keys() and 'fg' in self.confirm.keys():
                        color.print256bf(self.confirm['m'],self.confirm['fg'],self.confirm['bg'])

            



