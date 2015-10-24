#!/usr/bin/python

import argparse
import time

from core.xcamera  import xCamera

from core.rgblcd import RgbLcd
from core.answer import answer
from core.voice import Voice
from modules.mcolors import mColors
from modules.mtemperature import mTemperature
from modules.mweather import mWeather
from modules.mvoice import mVoice
from modules.mwolfram import mWolfram

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Bot')
    parser.add_argument('-c', '--core', help='Modules Mode')
    parser.add_argument('-m', '--modules', help='Project Mode')
    args = parser.parse_args()

    if args.core == 'xcamera':
        print 'Hello xCamera!'
        xcamera = xCamera()
        xcamera.capture()

    if args.core == 'hello':
        print 'Hello Edison!'

    if args.core == 'rgblcd':
        print 'Hello Grove - LCD RGB Backlight!'
        rgblcd = RgbLcd()
        rgblcd.setCursor(0,0)
        rgblcd.setText("Hi")
        rgblcd.setColor("red")

    if args.core == 'buzzer':
        print 'Hello Grove - Buzzer'
        answer(True)
        answer(False)

    if args.core == 'voice':
        print 'Hello Core Voice'
        voice = Voice()
        voice.record()
        voice.play()

    if args.modules == 'mweather':
        print 'Hello Module mWeather'
        mweather = mWeather()
        mweather.report()

    if args.modules == 'mweather':
        print 'Hello Module mWeather'
        mweather = mWeather()
        mweather.report()

    if args.modules == 'mcolors':
        print 'Hello Module mColors'
        mcolors = mColors()
        mcolors.show()

    if args.modules == 'mtemperature':
        print 'Hello Module mTemperature'
        mtemperature =mTemperature()
        mtemperature.show()

    if args.modules == 'mvoice':
        print 'Hello Module mVoice'
        mvoice = mVoice()
        mvoice.listen()

    if args.modules == 'mwolfram':
        print 'Hello Module mWolfram'
        mwolfram = mWolfram()
        mwolfram.ask()

# End of File
