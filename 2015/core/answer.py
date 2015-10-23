#!/usr/bin/python

import time
import pyupm_buzzer as upmBuzzer

def answer(value):

    buzzer = upmBuzzer.Buzzer(5)

    if value:
        print buzzer.playSound(upmBuzzer.DO, 100000)
        time.sleep(.2)
        print buzzer.playSound(upmBuzzer.DO, 100000)        
    else:
        print buzzer.playSound(upmBuzzer.DO, 1000000)

# End of File
