#!/usr/bin/python

from random import randint

from core.xcamera import xCamera
from core.xtweet import xtweet

class mSelfie(object):

    def __init__(self):
        self.xc = xCamera()

    def share(self):
        self.xc.capture()
        picture = self.xc.filepath()
        id = str(randint(0,99))
        xtweet("0x" + id + " #IoT #IoTLearningInit #IoTLearningInitiative IoTPy Selfie Project!", picture)

# End of File
