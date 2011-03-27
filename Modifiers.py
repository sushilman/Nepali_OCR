'''
Created on Jun 16, 2010

@author: sushil
'''

import cv
from Segmenter import Segmenter
from PixelCounter import PixelCounter 
from opencv.cv import CvRect

class Modifiers:
    segmenter=Segmenter()
    pixelCounter=PixelCounter()
    def __init__(self):
        'Constructor'
        
    #returns horizontal starting row and ending row of dika
    def locateDika(self,lineImg):
        countArr_V=self.pixelCounter.getCountArr_V(lineImg, 0)
        countArr_H=self.pixelCounter.getCountArr_H(lineImg, 0)
        dikaWidth=self.pixelCounter.getMin(countArr_V)
        
        max=self.pixelCounter.getMax(countArr_H)
        #print max
        maxAt=self.pixelCounter.getOccurredPositionList(countArr_H, max)
        #print maxAt

        return maxAt
        
        #get horizontally occurred pixel count
        #+1 or -1 or set some threshold 
        # OR
        # get horizontally most occurred pixel count => say 'x'
        # find width of dika
        # ?? is this really needed?? position from x-widthDika to x+widthDika can be considered to be dika??
        # or may be count the pixels in that row and decide according to certain threshold
        
          
        ''
        
    def extractTop(self,lineImg):
        ''
        dikaList=self.locateDika(lineImg)
        
        rect=CvRect
        rect.x=0
        rect.y=0
        rect.width=lineImg.width
        rect.height=dikaList[0]-2 # -2 is to eliminate disturbances from bha tha dha etc 
        
        segmentImg=cv.CreateImage((rect.width,rect.height), cv.IPL_DEPTH_8U, 1)
        cv.SetImageROI(lineImg, (rect.x,rect.y,rect.width,rect.height));
        cv.Resize(lineImg, segmentImg)
        cv.ResetImageROI(lineImg)
        
        cv.ShowImage("TOP", segmentImg)
        
        # locate horizontal dika position
        # set roi upper than dika 
        # extract the roi
          
    def extractMainElement(self,lineImg):
        ''
        #strip top
        #strip bottom
        #set roi to remaining
        #extract roi
        #OR
        #using height of purnabiram extract all letters of that height
        
    def extractBottom(self,lineImg):
        ''
        #???
        # use the top-stripped line Image
        # find out using purnaBiram's height?
        