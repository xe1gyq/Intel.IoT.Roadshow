#!/usr/bin/python

import random
import signal
import subprocess
import sys
import time

import pyupm_grove as grove
from core.rgblcd import RgbLcd
from random import getrandbits 

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def nonBlockingRawInput(prompt='', timeout=3):
    button = grove.GroveButton(2)
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        while True:
             if button.value() == 1:
                 return True
        signal.alarm(0)
        return text
    except AlarmException:
        print 'Button Timeout!'
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return False

class mColors(object):

    def __init__(self):
        pass

    def show(self):
        print "Module Colors"
        colors = ['Black', 'White', 'Red', 'Blue', 'Yellow',
                  'Gray', 'Green', 'Purple']

        rgblcd = RgbLcd()

        if getrandbits(1):
            colorlcd = random.choice(colors)
            colortext = random.choice(colors)
            anstemp = False
        else:
            colorlcd = random.choice(colors)
            colortext = colorlcd
            anstemp = True

        rgblcd.clear()
        rgblcd.setColor(colorlcd)
        rgblcd.setCursor(0,0)
        rgblcd.setText("Press Button if")
        rgblcd.setCursor(1,0)
        rgblcd.setText("color is " + colortext)
        time.sleep(.5)
        ansfin = nonBlockingRawInput()

        if anstemp is not ansfin:
             message = "Wrong Answer"
             colorlcd = "red"
        else:
             message = "Good Answer"
             colorlcd = "green"

        rgblcd.clear()
        rgblcd.setColor(colorlcd)
        rgblcd.setCursor(0,0)
        rgblcd.setText(message)
        time.sleep(1)

        #command = ['libraries/voicerss.sh', 'en-us', message]
        #proc = subprocess.call(command)

# End of File
