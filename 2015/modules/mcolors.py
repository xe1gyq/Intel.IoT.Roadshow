#!/usr/bin/python

import random
import signal
import sys
import time

import pyupm_grove as grove
from core.rgblcd import RgbLcd
from core.talk import talk
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
        talk("Press Button if color is " + colortext)
        time.sleep(.5)
        ansfin = nonBlockingRawInput()

        if anstemp is not ansfin:
             message = "This is a wrong answer! This color is " + colorlcd
        else:
             message = "This is a good answer! This color is " + colorlcd

        try:
            talk(message)
        except:
            pass

# End of File
