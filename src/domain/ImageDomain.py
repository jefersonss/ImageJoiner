'''
Created on 06/04/2012

@author: Jeferson
'''

from array import array

class ImageDomain(object):

    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.pixels = array("i", xrange(self.width*self.height))

    def setPixel(self, rgbColor, x, y):
        self.pixels[x+y*self.width] = rgbColor
    
    def getPixel(self, x, y):
        return self.pixels[x+y*self.width]
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height