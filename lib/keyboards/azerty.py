
######################### WARNING #####################
# Each array in this file MUST MAP each other.
# For example : KEY_INSERT which is the
# 9th key in function_key_strings array MUST be the
# 9th corresponding key in function_keys array. 


######################## Warning ######################
# Also the special_key_string array index must be the int value
# of the character. 
# The first index 0 is not taken in account so the 1st special_key_string et at index 1 and so on
#

KEY_UP      =  1
KEY_DOWN    =  2
KEY_LEFT    =  3
KEY_RIGHT   =  4
KEY_PGUP    =  5
KEY_PGDOWN  =  6
KEY_START   =  7
KEY_END     =  8
KEY_INSERT  =  9
KEY_DELETE  =  10
KEY_ENTER   =  11
KEY_BACK    =  12

KEY_F1       = 13
KEY_F2       = 14
KEY_F3       = 15
KEY_F4       = 16
KEY_F5       = 17
KEY_F6       = 18
KEY_F7       = 19
KEY_F8       = 20
KEY_F9       = 21
KEY_F10      = 22
KEY_F11      = 23
KEY_F12      = 24

KEY_BACKSPACE = 25 
KEY_TAB       = 26

special_key_string = [
        '',
        '',
        '',
        '',
        '',
        '',
        'BEL',
        'BS',
        'TAB',
        'LF',
        'LF',
        'LF',
        'CR',
        'SO',
        'S1',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        'CAN',
        '',
        '',
        'ESC',
        ]


function_key_strings = [
        'KEY_UP',
        'KEY_DOWN',
        'KEY_LEFT',
        'KEY_RIGHT',
        'KEY_PGUP',
        'KEY_PGDOWN',
        'KEY_START',
        'KEY_END',
        'KEY_INSERT',
        'KEY_DELETE',
        'KEY_ENTER',
        'KEY_BACK',
        
        'KEY_F1',
        'KEY_F2',
        'KEY_F3',
        'KEY_F4',
        'KEY_F5',
        'KEY_F6',
        'KEY_F7',
        'KEY_F8',
        'KEY_F9',
        'KEY_F10',
        'KEY_F11',
        'KEY_F12',
        
        'KEY_BACKSPACE',
        'KEY_TAB'
]


function_keys  = {
        '[A'   :  KEY_UP ,
        '[B'   :  KEY_DOWN, 
        '[C'   :  KEY_LEFT,
        '[D'   :  KEY_RIGHT,
        '[5~'  : KEY_PGUP,
        '[6~'  : KEY_PGDOWN,
        '[H'   : KEY_START,
        '[F'   : KEY_END,
        '[2~'  : KEY_INSERT,
        '[3~'  : KEY_DELETE,
        'OP'   : KEY_F1,
        'OQ'   : KEY_F2,
        'OR'   : KEY_F3,
        'OS'   : KEY_F4,
        '[15~' : KEY_F5,
        '[17~' : KEY_F6,
        '[18~' : KEY_F7,
        '[19~' : KEY_F8,
        '[20~' : KEY_F9,
        '[21~' : KEY_F10,
        '[23~' : KEY_F11,
        '[24~' : KEY_F12
        }



