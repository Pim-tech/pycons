#!/usr/bin/env python3
from pynput import keyboard
import sys

def on_activate_page_up():
    print('Page UP')

def on_activate_page_down():
    print('Page DOWN')

def on_activate_letter_a():
    print('Letter a')

def quit_prg():
    print('On sort!')
    sys.exit(0)

def r_sub():
    print("This is r_sub.")

with keyboard.GlobalHotKeys({
    '<page_up>' : on_activate_page_up,
    '<page_down>': on_activate_page_down,
    '<esc>'      : quit_prg,
    'a'        : on_activate_letter_a,
    'r'        : r_sub
    }) as h:
    h.join()

