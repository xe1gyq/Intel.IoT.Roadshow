#!/usr/bin/python

import commands
import json
import logging
import re

from gosttpy import gosttpy
from core.voicerecognition import VoiceRecognition
from core.talk import talk

class mVoice(object):

    def __init__(self):

        self.output = ""
        self.voicerecognition = VoiceRecognition()
        self.speech = gosttpy.gosttpy()
        self.apiKey = 'AIzaSyD1o305c7liSJzZUS46OIOxig92ViUCbAQ'

    def presentation(self):
        talk("Hi Mexico Intel Makers! Please say something!")

    def decode(self, output):
        #if re.search(r'red', output, re.M|re.I):
        talk("I think you said " + output)

    def listen(self):

        self.voicerecognition.record()
        output = self.voicerecognition.recognize('True')
        self.decode(output)

# Enf of File
