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
        im = Image.open(foregroundImageAddress)