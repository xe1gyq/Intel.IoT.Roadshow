#!/usr/bin/python

import ConfigParser
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import pyupm_grove as grove

class mTemperature(object):

    def __init__(self):

        self.configuration = ConfigParser.ConfigParser()
        self.configuration.read('configuration/credentials.config')
        self.username = self.configuration.get('plotly','username')
        self.apikey = self.configuration.get('plotly','apikey')
        self.streamtoken = self.configuration.get('plotly','streamtoken')

        py.sign_in(self.username, self.apikey)

        self.temp = grove.GroveTemp(0)

    def graph(self):

        stream_temperature = Scatter(
            x=[],
            y=[],
            stream=dict(
                token=self.streamtoken,
            )
        )

        layout = Layout(
            title="IntelMakerMX Temperature"
        )

        this = Figure(data=[stream_temperature], layout=layout)
        py.plot(this, filename='IntelMakerMX Temperature', auto_open=False)

        stream = py.Stream(self.streamtoken)
        stream.open()
        time.sleep(5)

        counter = 0

        while True:
            temperaturedata = self.temp.value()()
            stream.write({'x': counter, 'y': temperaturedata})
            counter += 1
            time.sleep(0.25)

# End of File
