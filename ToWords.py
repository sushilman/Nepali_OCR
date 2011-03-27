'''
Created on Apr 23, 2010

@author: sushil
'''
import cv
from Segmenter import Segmenter

class ToWords(object):
    segmenter=Segmenter()
    def __init__(self):
        '''
        constructor
        '''
        self.segmenter=Segmenter()
        
    def segment(self,image):
        transImg=cv.CreateImage((image.height,image.width), cv.IPL_DEPTH_8U, 1)    
        cv.Transpose(image, transImg)
        'returns Number of available line segments'
        return self.segmenter.segmentHorizontally(transImg)
    
    def getWordSegment(self,wordNumber):
        'returns line segment Image'
        image=self.segmenter.getSegment(wordNumber)    
        return image
    
    def getReadableWordSegment(self,wordNumber):
        'returns transposed form of line segment Image'
        image=self.segmenter.getSegment(wordNumber)
        transImg=cv.CreateImage((image.height,image.width), cv.IPL_DEPTH_8U, 1)    
        cv.Transpose(image, transImg)
        return transImg  