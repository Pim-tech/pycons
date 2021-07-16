#!/usr/bin/python3
#New python script generation
import keyboard

keyboard.press_and_release('shift+s, space')
keyboard.add_hotkey('page_up',lambda e: print(e.name)) 
#keyboard.add_hotkey('a',lambda e: print(e.name)) 

keyboard.wait('esc')
