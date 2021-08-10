
from lib.rectangle import *
from lib.message import *


class Alert(Message):

    def __init__(self,*args,**kws):
        kws['message'] = '! ' + kws.pop('message').upper() + ' !'

        super(Alert,self).__init__(*args,**kws)

