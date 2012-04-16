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

    def readImages(self, foregroundImageAddress, colorToRemove, backgroundImageAddress, whereToSave):
        foreground = Image.open(foregroundImageAddress, 'r')
        foreground = foreground.convert('RGBA')
        
        background = Image.open(backgroundImageAddress, 'r')
        background = background.convert('RGBA')
        
        self.createNewImage(colorToRemove, whereToSave, foreground, background)
        
    def createNewImage(self, colorToRemove, whereToSave, foreground, background):
        self.removeColor(foreground, colorToRemove)
        background.paste(foreground, ((background.size[0] - foreground.size[0]), (background.size[1] - foreground.size[1])), foreground)
        background.save(whereToSave + '/output.png')
        
    def removeColor(self, image, colorToRemove):
        newData = list()
        imagePixels = image.getdata()
        for item in imagePixels:
            if (colorToRemove[0] - item[0]) < 15 and (colorToRemove[1] - item [1]) < 15  and (colorToRemove[2] - item[3]) < 15:
                newData.append(0)
            else:
                newData.append(item)

        image.putdata(newData)