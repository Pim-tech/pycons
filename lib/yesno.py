
from lib.rectangle import *
from lib.message import *

class YesNo(Rectangle):

    def __init__(self,*args,**kws):
        self.textcolor = None
        self.yes = 'Yes'
        self.no  = 'No'
        self.attr_yes = LWHITE + BRED
        self.attr_no  = LWHITE + BBLUE
        self.ypos_yes =  self.xpos_yes = None
        self.ypos_no =  self.xpos_no = None
        self.message = kws.pop('message') 
        self.confirm = None
        self.c256   = False
        self.textcolor = None
        self.gap_yesno = 2


        if 'textcolor' in kws.keys():
            self.textcolor = kws.pop('textcolor')
        if 'c256' in kws.keys():
            self.c256 = kws.pop('c256') 
        if 'yes' in kws.keys():
            self.yes = kws.pop('yes') 
        if 'no' in kws.keys():
            self.no = kws.pop('no') 
        if 'attryes' in kws.keys():
            self.attr_yes = kws.pop('attryes')
        if 'attrno' in kws.keys():
            self.attr_no = kws.pop('attrno')
        if 'gap_yesno' in kws.keys():
            self.gap_yesno = kws.pop('gap_yesno')
        if not 'box' in kws.keys():
            kws['box'] = SIMPLE
        if not 'motif' in kws.keys():
            kws['motif'] = ' '
        
        if not 'parent' in kws.keys():
            lines,cols = getTerminalSize()
            if not 'hlen' in  kws.keys():
                kws['hlen'] = int(cols//6.32)
            if not 'vlen' in kws.keys():
                kws['vlen'] = int(lines//7)
            if not 'xpos' in  kws.keys():
                kws['xpos'] = int(cols//2 - kws['hlen'] // 2)
            if not 'ypos' in  kws.keys():
                kws['ypos'] = int(lines//2 - kws['vlen'] // 2) 
        else:
            if not 'hlen' in kws.keys():
                kws['hlen'] = int(kws['parent'].hlen//3)
            if not 'vlen' in kws.keys():
                kws['vlen'] = int(kws['parent'].vlen//6)
            if not 'xpos' in kws.keys():
                kws['xpos'] = int(kws['parent'].hlen//2 - kws['hlen'] //2)
            if not 'xpos' in kws.keys():
                kws['xpos'] = int(kws['parent'].vlen//2 - kws['vlen'] //2)
            
        super(YesNo,self).__init__(*args,**kws)
        try:
            len_msg = len(self.message)
            self.xpos_message = int(self.xpos + (self.hlen//2) - len_msg//2)
            self.ypos_message = int(self.ypos + (self.vlen//2) - (self.vlen//5) )
            if len_msg > (self.hlen - 3):
                raise ValueError("Message does not fit into window!")
            self.ypos_yes = self.ypos_no = self.ypos + self.vlen - 3
            if (self.ypos_yes ) > ((self.ypos + self.vlen) - 2):
                raise ValueError("Box not high enought to contain message and yesno buttons!")
            self.xpos_yes = self.xpos + self.gap_yesno 
            self.xpos_no  = self.xpos + self.hlen  - ( self.gap_yesno + len(self.no))

        except TypeError as  te:
            raise
        except ValueError as ve:
            raise
        

    def draw(self):
        super().draw()
        gotoxy(self.xpos_message,self.ypos_message)
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
        
        if self.c256:
            gotoxy(self.xpos_yes,self.ypos_yes)
            color.print256c(self.yes,self.attr_yes)
            gotoxy(self.xpos_no,self.ypos_no)
            color.print256c(self.no,self.attr_no)
        else:
            gotoxy(self.xpos_yes,self.ypos_yes)
            color.print(self.yes,self.attr_yes)
            gotoxy(self.xpos_no,self.ypos_no)
            color.print(self.no,self.attr_no)
            
