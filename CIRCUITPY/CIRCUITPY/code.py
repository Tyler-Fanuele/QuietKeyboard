# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)

# The keyboard object!
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# Open linux terminal with left control + left alt + T
def open_linux_terminal():
    keyboard.press(Keycode.LEFT_CONTROL)
    keyboard.press(Keycode.LEFT_ALT) 
    keyboard.press(Keycode.T)
    keyboard.release_all()
    
# Type a phrase as a keyboard
def type_phrase(phrase):
    keyboard_layout.write(phrase)
    
# Open linux terminal and run command then close it if bool is true
def exec_command_in_linux_terminal(command, close_bool):
    open_linux_terminal()
    time.sleep(1)
    type_phrase(command)
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()
    if close_bool == True: 
        time.sleep(.5) 
        keyboard.press(Keycode.LEFT_ALT, Keycode.SPACE) 
        keyboard.release_all()
        keyboard.press(Keycode.ENTER)
        keyboard.release_all()


button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

if button.value == True:
    while True:
        led.value = True
else:
    with open("/test.txt", "r") as fp:
        exec_command_in_linux_terminal(fp.readline(), True)
        #open_linux_terminal()
        while True:
            led.value = True
            time.sleep(.5)
            led.value = False
            time.sleep(.5)
