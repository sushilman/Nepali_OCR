'''
Created on Apr 23, 2010

@author: sushil
'''
import cv
from Segmenter import Segmenter
from PixelCounter import PixelCounter
from ToLines import ToLines

class ToCharacters(object):
    segmenter=Segmenter()
    def __init__(self):
        '''
        constructor
        '''
        self.segmenter=Segmenter()
    
    def segment(self,image):
        'returns Number of available character segments in a line'
        return self.segmenter.segmentHorizontally(image)
    
    #returns the same but manipulated line Image
    def splitDika(self,image):
        segmentLine=ToLines()
        totalLines=segmentLine.segment(image)
        pixelCounter = PixelCounter()

        for lineNum in range(totalLines):
            lineImg=segmentLine.getLineSegment(lineNum)
            lineRowRange=segmentLine.getCoordinatesOfLineSegment(lineNum)
            countArr=pixelCounter.getCountArr_V(lineImg, 0)
            #print countArr
            min=pixelCounter.getMin(countArr)
            #dika width is min vertically and it is most occurred horizontally
            
            for x in pixelCounter.getOccurredPositionList(countArr, min):
                for height in range(lineRowRange[0],(lineRowRange[1]+lineRowRange[0])/2):
                    cv.Set2D(image,height,x,255)
        return image 
        
    #def extractCharacters(self,lineImg):
        #splitDika + #ToWords.extractReadableWordSegment = extracCharacters
