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
        foreground = foreground.convert('RGBA')
        
        background = Image.open(backgroundImageAddress, 'r')
        background = background.convert('RGBA')
        
        self.removeColor(foreground)
        background.paste(foreground, (0, 0), foreground)
        
        background.save('output.png')
        
    def removeColor(self, image):
        newData = list()
        imagePixels = image.getdata()
        for item in imagePixels:
            if item[0] == 255 and item [1] == 255  and item[3] == 255:
                newData.append(0)
            else:
                newData.append(item)

        image.putdata(newData)
        image.save('newOutput.png')