'''
Created on 06/04/2012

@author: Jeferson
'''

from PIL import Image

class ImageReader(object):

    def __init__(self, params):
        '''
        Constructor
        '''

    def readImages(self, foregroundImageAddress, foregroundColorToRemove, backgroundImageAddress):
        foreground = Image.open(foregroundImageAddress, 'r')
        background = Image.open(backgroundImageAddress, 'r')
        newImage = Image.composite(foreground, background)
        test = Image.new()
        test.paste(newImage)
        test.save("output.png")
        
    def removeColor(self, image, colorToRemove):
        '''
        Code goes here
        '''