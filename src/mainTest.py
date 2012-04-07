'''
Created on 06/04/2012

@author: Jeferson
'''

import engine.ImageReader as ImageReader

if __name__ == '__main__':
    ir = ImageReader.ImageReader(None)
    ImageReader.ImageReader.readImages(ir, "C:\Users\Jeferson\Desktop\frg.jpg", "", "C:\Users\Jeferson\Desktop\bkg.jpg")