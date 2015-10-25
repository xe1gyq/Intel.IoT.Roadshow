#!/usr/bin/python

import json
import logging
import sys

from core.xspeechrecognition import xSpeechRecognition
from core.xtalk import xtalk
from core.xvoice import xVoice
from core.xwolfram import xWolfram

class mWolfram(object):

    def __init__(self):

        self.xvoice = xVoice()
        self.xspeechr = xSpeechRecognition()
        self.xwolfram = xWolfram()

    def ask(self):

        xtalk('en-us', 'Yes! What is your question for Wolfram Alpha?')
        self.xvoice.record()

        question = self.xspeechr.recognize()
        questionmessage = 'Question? ' + question
        xtalk('en-us', questionmessage)

        answer = self.xwolfram.question(question)

        if answer != None:
            answermessage = 'Answer? ' + answer
            xtalk('en-us', answermessage)
        else:
            answermessage = 'Answer? Sorry! Something went wrong!'
            xtalk('en-us', answermessage)

# End of File
