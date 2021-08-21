
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
            self.attr_yes = kws.pop('attrno')
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
        self._write_inside_and_yesno()

    def _write_inside_and_yesno(self):
        if self.confirm is None:
            self.xpos_message = self.xpos + int(self.hlen // 2) - int(len(self.message)//2)
            self.ypos_message = self.ypos + int(self.vlen // 2) 
        else:
            self.xpos_message = self.xpos + int(self.hlen // 2) - int(len(self.message)//2)
            self.ypos_message = self.ypos + int(self.vlen // 2) - 1
            self.xpos_yes = self.xpos + int(self.hlen // 4) - int(len(self.yes//2))
            self.ypos_yes = self.ypos+self.vlen - 2
            self.xpos_no = int(self.xpos + self.hlen  - (self.hlen //4) + len(self.no//2))
            self.ypos_no = self.ypos+self.vlen - 2
            

    def set_parent(self,parent):
        super().set_parent(parent)
        self._write_inside_and_yesno()


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
            
