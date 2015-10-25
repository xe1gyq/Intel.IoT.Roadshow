#!/usr/bin/python

import commands
import json
import logging
import re

from core.xvoice import xVoice
from core.xspeechrecognition import xSpeechRecognition
from core.xtalk import xtalk

class mPhraseRecognition(object):

    def __init__(self):

        self.output = ""
        self.xv = xVoice()
        self.xs = xSpeechRecognition()

    def presentation(self):
        xtalk('en-us', "Hi IoT Python Learners! Please say something!?")

    def decode(self):
        self.presentation()
        self.xv.record()
        output = self.xs.recognize()
        xtalk('en-us', "Thanks! I think you said " + output)

# Enf of File
