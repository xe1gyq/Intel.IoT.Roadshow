#!/usr/bin/python

import argparse
import time

from core.rgblcd import RgbLcd
from core.answer import answer
from modules.mcolors import mColors
from modules.mweather import mWeather

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

    if args.core == 'voice':
        print 'Hello Module - Voice'
        voice = mWeather()
        voice.report()

    if args.modules == 'mcolors':
        print 'Hello Module Colors'
        mcolors =mColors()
        mcolors.show()

# End of File
