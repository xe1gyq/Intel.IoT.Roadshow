#!/usr/bin/python

import argparse
import time

from core.rgblcd import RgbLcd
from core.answer import answer
from modules.mcolors import mColors
from modules.mtemperature import mTemperature
from modules.mweather import mWeather
from modules.mvoice import mVoice

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Bot')
    parser.add_argument('-c', '--core', help='Modules Mode')
    parser.add_argument('-m', '--modules', help='Project Mode')
    args = parser.parse_args()

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

# End of File
