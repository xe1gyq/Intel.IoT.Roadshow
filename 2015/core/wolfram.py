#!/usr/bin/python

import ConfigParser
import logging
import re
import wolframalpha

class Wolfram(object):

    def __init__(self):

        logging.info('Wolfram')
        self.conf = ConfigParser.ConfigParser()
        self.path = "configuration/credentials.config"
        self.conf.read(self.path)
        appid=self.conf.get("wolfram", "appid")
        self.client = wolframalpha.Client(appid)

    def question(self, question):
        print 'Wolfram Question'
        res = self.client.query(question)
        print(next(res.results).text)
        print((next(res.results).text))
        string = re.sub('[^0-9a-zA-Z]+', ' ', next(res.results).text)
        print(string)
        return string

if __name__ == "__main__":

    wf = Wolfram()
    wf.question("what is the capital of mexico")

# End of File
