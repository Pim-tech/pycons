#!/usr/bin/env python3
from pynput import keyboard

def on_activate_page_up():
    print('Page UP')

def on_activate_page_down():
    print('Page DOWN')

def on_activate_letter_a():
    print('Letter a')

def quit_prg():
    print('On sort!')
    exit(0)

with keyboard.GlobalHotKeys({
    '<page_up>' : on_activate_page_up,
    '<page_down>': on_activate_page_down,
    '<esc>'      : quit_prg,
    'a'        : on_activate_letter_a
    'r'        : self.r()
    }) as h:
    h.join()

