'''
Created on 06/04/2012

@author: Jeferson
'''

import engine.ImageReader as ImageReader
from Tkinter import *
import tkFileDialog

if __name__ == '__main__':
    ir = ImageReader.ImageReader(None)
    root = Tk()
    root.withdraw()
    
    backgroundDir = tkFileDialog.askopenfile(initialdir="/",title='Please select the background file')
    foregroundDir = tkFileDialog.askopenfile(initialdir=backgroundDir,title='Please select the foreground file')
    whereToSave = tkFileDialog.askdirectory(initialdir="/",title='Select a directory to save you output')
    
    ir.readImages(foregroundDir.name, (255, 255, 255), backgroundDir.name, whereToSave)