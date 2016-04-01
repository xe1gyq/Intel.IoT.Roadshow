#!/usr/bin/python

from random import randint

from core.xcamera import xCamera
from core.xtwitter import xTwitter

class mSelfie(object):

    def __init__(self):
        self.xc = xCamera()
        self.tw = xTwitter()

    def share(self):
        self.xc.capture()
        picture = self.xc.filepath()
        id = str(randint(0,99))
        self.tw.tweet("0x" + id + " #IoT #IoTLearningInit #IoTLearningInitiative IoTPy Selfie Project!", picture)

# End of File
