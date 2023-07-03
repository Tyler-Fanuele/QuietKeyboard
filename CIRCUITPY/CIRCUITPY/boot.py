import storage
import digitalio
import board
import time
# Boot device without storage drive visible to user, run only when in needed use
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT

if button.value == True:
    time.sleep(.1)
    led.value = True
    time.sleep(.1)
    led.value = False
    
    time.sleep(.1)
    led.value = True
    time.sleep(.1)
    led.value = False
    
    print("In button")
else:
    time.sleep(.2)
    led.value = True
    time.sleep(.2)
    led.value = False
    print("not in button")
    storage.disable_usb_drive()
