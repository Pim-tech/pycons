from lib.rectangle import *

class Message(Rectangle):

    def __init__(self,*args,**kws):
        self.color_sequence = ''
        self.confirm_sequence = ''
        self.textcolor = None
        self.confirm_color = None
        self.confirm_mode = None
        self.textmode = 0
        self.confirm   = None
        self.color_instance = None
        self.ypos_confirm =  self.xpos_confirm = None
        self.message = kws.pop('message') 
        c=Color()
        if 'textcolor' in kws.keys():
            self.color_instance = c
            self.textcolor = kws.pop('textcolor')
            if 'textmode' in kws.keys():
                self.textmode = kws.pop('textmode')
            if isinstance(self.textcolor,int):
                self.color_sequence = c.sequence8(self.textcolor,True,mode = self.textmode)
            elif isinstance(self.textcolor,dict):
                if {'fg','bg'} <= self.textcolor.keys():
                    fg = {}
                    bg = {}
                    if 'mode' in self.textcolor.keys():
                        assert isinstance(self.textcolor['mode'],int),True
                        self.textmode = self.textcolor['mode']
                    if isinstance(self.textcolor['fg'],int) and isinstance(self.textcolor['bg'],int):
                        self.color_sequence = c.sequence256bf(self.textcolor['fg'],self.textcolor['bg'],True)
                    elif isinstance(self.textcolor['fg'],tuple) and isinstance(self.textcolor['bg'],tuple):
                        assert isinstance(self.textcolor['fg'],tuple),True
                        assert isinstance(self.textcolor['bg'],tuple),True
                        fg['r'],fg['v'],fg['b'] = self.textcolor['fg']
                        bg['r'],bg['v'],bg['b'] = self.textcolor['bg']
                        assert isinstance(fg['r'],int),True
                        assert isinstance(fg['v'],int),True
                        assert isinstance(fg['b'],int),True
                        assert isinstance(bg['r'],int),True
                        assert isinstance(bg['v'],int),True
                        assert isinstance(bg['b'],int),True
                        self.color_sequence=c.sequencervb(fg,bg,True,self.textmode)
        if 'confirm' in kws.keys():
            self.confirm = kws.pop('confirm') 
            if 'confirm_color' in kws.keys():
                self.confirm_color = kws.pop('confirm_color')
            if 'confirm_mode' in kws.keys():
                self.confirm_mode = kws.pop('confirm_mode')
            if isinstance(self.confirm_color,int):
                self.confirm_sequence = c.sequence8(self.confirm_color,True,mode=self.confirm_mode)
            elif isinstance(self.confirm_color,dict):
                if {'fg','bg'} <= self.confirm_color.keys():
                    fg = {}
                    bg = {}
                    if 'mode' in self.confirm_color.keys():
                        assert isinstance(self.confirm_color['mode'],int),True
                        self.confirm_mode = self.confirm_color['mode']
                    if isinstance(self.confirm_color['fg'],int) and isinstance(self.confirm_color['bg'],int):
                        self.confirm_sequence = c.sequence256bf(self.confirm_color['fg'],self.confirm_color['bg'],True)
                    elif isinstance(self.confirm_color['fg'],tuple) and isinstance(self.confirm_color['bg'],tuple):
                        assert isinstance(self.confirm_color['fg'],tuple),True
                        assert isinstance(self.confirm_color['bg'],tuple),True
                        fg['r'],fg['v'],fg['b'] = self.confirm_color['fg']
                        bg['r'],bg['v'],bg['b'] = self.confirm_color['bg']
                        assert isinstance(fg['r'],int),True
                        assert isinstance(fg['v'],int),True
                        assert isinstance(fg['b'],int),True
                        assert isinstance(bg['r'],int),True
                        assert isinstance(bg['v'],int),True
                        assert isinstance(bg['b'],int),True
                        self.confirm_sequence=c.sequencervb(fg,bg,True,self.confirm_mode)
        if not 'hlen' in  kws.keys():
            lines,cols = getTerminalSize()
            kws['hlen'] = int(cols//6.32)
        if not 'vlen' in kws.keys():
            lines,cols = getTerminalSize()
            kws['vlen'] = int(lines//7)
        if not 'box' in kws.keys():
            kws['box'] = SIMPLE
        if not 'motif' in kws.keys():
            kws['motif'] = ' '

     
        super(Message,self).__init__(*args,**kws)
        if 'parent' in kws.keys():
            super().set_parent(kws['parent'])

        if self.confirm is None:
            self.xpos_message = self.xpos + int(self.hlen // 2) - int(len(self.message)//2)
            self.ypos_message = self.ypos + int(self.vlen // 2) 
        else:
            self.xpos_message = self.xpos + int(self.hlen // 2) - int(len(self.message)//2)
            self.ypos_message = self.ypos + int(self.vlen // 2) - 1
            self.xpos_confirm = self.xpos + int(self.hlen // 2) - int(len(self.confirm)//2)
            self.ypos_confirm = int(self.ypos+self.vlen - (self.vlen//3 + 1))


    def draw(self):
        super().draw()
        gotoxy(self.xpos_message,self.ypos_message)
        print(self.color_sequence + self.message,flush=True,end='')
        self.color_instance._()

        gotoxy(self.xpos_confirm,self.ypos_confirm)
        if self.confirm:
            print(self.confirm_sequence + self.confirm, flush =True, end='')
            self.color_instance._()

            



