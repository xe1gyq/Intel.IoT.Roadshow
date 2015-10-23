#!/usr/bin/python

from colour import Color

import matplotlib.colors as colors
import pyupm_i2clcd as lcd

class RgbLcd(object):

    def __init__(self):

        self.rgblcd = lcd.Jhd1313m1(1, 0x3E, 0x62)

    def __del__(self):
        pass

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return list(tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))

    def clear(self):
        self.rgblcd.clear()

    def setCursor(self, x, y):
        self.rgblcd.setCursor(x,y)

    def setColor(self, color):
        color = Color(color)
        colordecimal = self.hex_to_rgb(colors.rgb2hex(color.rgb))
        self.rgblcd.setColor(colordecimal[0], colordecimal[1], colordecimal[2])

    def setText(self, text):
        self.rgblcd.write(text)

# End of Text
