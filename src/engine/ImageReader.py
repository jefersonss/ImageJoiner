'''
Created on 06/04/2012

@author: Jeferson
'''

from PIL import Image
from domain.ImageDomain import ImageDomain

class ImageReader(object):

    def __init__(self, params):
        '''
        Constructor
        '''

    def readImages(self, foregroundImageAddress, foregroundColorToRemove, backgroundImageAddress):
        foreground = Image.open(foregroundImageAddress, 'r')
        background = Image.open(backgroundImageAddress, 'r')
        fgImage, bgImage = self.populateImages(foreground, background)
        self.removeColor(fgImage, fgImage.getPixel(0, 0))
        img = Image.new(foreground.mode, foreground.size)
        
    def fillNewImage(self, imageToFill, pixels):
        imageToFill.putpixel()
    
    def populateImages(self, foreground, background):
        fgWidth, fgHeight = foreground.size
        bgWidth, bgHeight = background.size
        
        fgImage = ImageDomain(fgWidth, fgHeight)
        bgImage = ImageDomain(bgWidth, bgHeight)
        
        fgImage = self.fillPixels(foreground.load(), fgWidth, fgHeight, fgImage)
        bgImage = self.fillPixels(background.load(), bgWidth, bgHeight, bgImage)
        
        return fgImage, bgImage
    
    def fillPixels(self, rgbColors, imWidth, imHeight, domainImage):
        for h in range(0, imHeight):
            for w in range(0, imWidth):
                domainImage.setPixel(rgbColors[w, h], w, h)
        
        return domainImage
    
    def removeColor(self, image, colorToRemove):
        for w in range(0, image.getWidth()):
            for h in range(0, image.getHeight()):
                if(image.getPixel(h, w) == colorToRemove):
                    image.setPixel((0, 0, 0), w, h)