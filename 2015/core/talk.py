#!/usr/bin/python

import subprocess

def talk(message):

    command = ['core/voicerss.sh', 'en-us', message]
    proc = subprocess.call(command)

# End Of File
