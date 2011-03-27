'''
Created on Apr 23, 2010

@author: sushil
'''

import cv
from Segmenter import Segmenter

class ToLines(object):
    segmenter=Segmenter()
    def __init__(self):
        '''
        constructor
        '''
        self.segmenter=Segmenter()
        
    def segment(self,image):
        'returns Number of available line segments'
        return self.segmenter.segmentHorizontally(image)
    
    def getLineSegment(self,lineNumber):
        'returns line segment Image'
        return self.segmenter.getSegment(lineNumber)
    
    def getCoordinatesOfLineSegment(self,lineNumber):
        return self.segmenter.getRowRange(lineNumber)
    
    def getPixelCountsOfLineSegment(self,lineNumber):
        #print self.segmenter.getPixelCountsOfSegment(lineNumber)
        return self.segmenter.getPixelCountsOfSegment(lineNumber)