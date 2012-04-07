'''
Created on 06/04/2012

@author: Jeferson
'''

class ImageDomain(object):

    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.pixels = [ [ [] for i in range(width) ] for j in range(height) ]

    def setPixel(self, rgbColor, width, height):
        self.pixels[height][width] = rgbColor
    
    def getPixel(self, width, height):
        return self.pixels[width][height]
    
    def getPixels(self):
        return self.pixels
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height