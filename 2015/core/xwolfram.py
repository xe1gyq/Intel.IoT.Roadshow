#!/usr/bin/python

import ConfigParser
import logging
import re
import wolframalpha

class xWolfram(object):

    def __init__(self):
        pass
    
    def setup(self):
        self.conf = ConfigParser.ConfigParser()
        self.path = "configuration/credentials.config"
        self.conf.read(self.path)
        appid=self.conf.get("wolfram", "appid")
        self.client = wolframalpha.Client(appid)

    def question(self, question):
        self.setup()
        res = self.client.query(question)
        string = re.sub('[^0-9a-zA-Z]+', ' ', next(res.results).text)
        return string

if __name__ == "__main__":

    xw = xWolfram()
    ourquestion = "What is the capital of Mexico"
    print ourquestion
    print xw.question(ourquestion)

# End of File
