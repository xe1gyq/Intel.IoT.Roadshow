#!/usr/bin/python

import argparse
import time

from core.xanswer import xanswer
from core.xcamera import xCamera
from core.xtweet import xtweet

from modules.mweather import mWeather
from modules.mtemperature import mTemperature
from modules.mwolfram import mWolfram

#from modules.mcolors import mColors
#from modules.mvoice import mVoice

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Bot')
    parser.add_argument('-c', '--core', help='Modules Mode')
    parser.add_argument('-m', '--modules', help='Project Mode')
    args = parser.parse_args()

    if args.modules == 'mweather':
        print 'Hello Module mWeather'
        mweather = mWeather()
        mweather.report()

    if args.modules == 'mtemperature':
        print 'Hello Module mTemperature'
        mtemperature =mTemperature()
        mtemperature.graph()

    if args.modules == 'mwolfram':
        print 'Hello Module mWolfram'
        mwolfram = mWolfram()
        mwolfram.ask()

    if args.modules == 'mcolors':
        print 'Hello Module mColors'
        mcolors = mColors()
        mcolors.show()

    if args.modules == 'mvoice':
        print 'Hello Module mVoice'
        mvoice = mVoice()
        mvoice.listen()

# End of File
