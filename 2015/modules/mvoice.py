#!/usr/bin/python

import commands
import logging
import re

from core.voicerecognition import VoiceRecognition
from core.talk import talk

class mVoice(object):

    def __init__(self):

        self.output = ""
        self.voicerecognition = VoiceRecognition()

    def presentation(self):

        talk("Hi! How can I help you?")

    def decode(self, output):

        if re.search(r'red', output, re.M|re.I):
            talk('You said red!')
        else:
            talk("We did not understand your word of wisdom!")

    def listen(self):

        self.presentation()
        self.voicerecognition.record()
        output = self.voicerecognition.recognize('False')
        print output
        self.decode(output)

# Enf of File
