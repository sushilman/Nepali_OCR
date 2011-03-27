'''
Created on Apr 20, 2010

@author: sushil
'''
import cv
from ConvertToBinaryImage import ConvertToBinaryImage
from PixelCounter import PixelCounter
from opencv.cv import CvRect, IplImage

class Segmenter(object):
    usefulRowRangesList=list()
    image=IplImage
    def __init__(self):
        '''
        Constructor
        '''
        self.image=IplImage
        self.usefulRowRangesList=list()
         
    def segmentHorizontally(self,img):
        self.image=img
        pixelCounter=PixelCounter()
        pixelCountArr=pixelCounter.getCountArr_H(img,0)
        
        startCountingRows=0
        startRowNum=0
        rowNumCounter=0
        
        for row in range(len(pixelCountArr)):
            if(pixelCountArr[row]!=0):
                if(not startCountingRows):
                    startCountingRows=1
                    startRowNum=row
                rowNumCounter=rowNumCounter+1
            else:   
                if(startCountingRows):    
                    usefulRowRangesTuple=(startRowNum,startRowNum+rowNumCounter)
                    self.usefulRowRangesList.append(usefulRowRangesTuple)
                startCountingRows=0
                rowNumCounter=0
                #cv.SetZero(cv.GetRow(img, row))
        return len(self.usefulRowRangesList)

    def getSegment(self,segmentNumber):
        element=self.usefulRowRangesList[segmentNumber]
        rect=CvRect()
        rect.x=0
        rect.y=element[0]
        rect.width=self.image.width
        rect.height=element[1]-rect.y
        
        segmentImg=cv.CreateImage((rect.width,rect.height), cv.IPL_DEPTH_8U, 1)
        cv.SetImageROI(self.image, (rect.x,rect.y,rect.width,rect.height));
        cv.Resize(self.image, segmentImg)
        cv.ResetImageROI(self.image)
        
        return segmentImg
    
    def getRowRange(self,lineNumber):
        return self.usefulRowRangesList[lineNumber]