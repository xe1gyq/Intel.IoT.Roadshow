#!/usr/bin/python

import argparse
import time

from core.xcamera import xCamera
from core.xtwitter import xTwitter

#from modules.mcolors import mColors
from modules.mphraserecognition import mPhraseRecognition
from modules.mselfie import mSelfie
from modules.msystem import mSystem
from modules.mtemperature import mTemperature
from modules.mweather import mWeather
from modules.mwolfram import mWolfram

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Bot')
    parser.add_argument('-c', '--core', help='Modules Mode')
    parser.add_argument('-m', '--modules', help='Project Mode')
    args = parser.parse_args()

    if args.modules == 'mphraserecognition':
        print 'Hello Module mPhraseRecognition'
        mpr = mPhraseRecognition()
        mpr.decode()

    if args.modules == 'mselfie':
        print 'Hello Module mSelfie'
        mselfie = mSelfie()
        mselfie.share()

    if args.modules == 'msystem':
        print 'Hello Module mSystem'
        msystem = mSystem()
        msystem.graph()

    if args.modules == 'mtemperature':
        print 'Hello Module mTemperature'
        mtemperature =mTemperature()
        mtemperature.graph()

    if args.modules == 'mweather':
        print 'Hello Module mWeather'
        mweather = mWeather()
        mweather.report()

    if args.modules == 'mwolfram':
        print 'Hello Module mWolfram'
        mwolfram = mWolfram()
        mwolfram.ask()

    if args.modules == 'mcolors':
        print 'Hello Module mColors'
        mcolors = mColors()
        mcolors.show()

# End of File
