# -*- coding: utf-8 -*-
'''
Created on Apr 23, 2010

@author: sushil
'''
import cv
from opencv.cv import IplImage
from ConvertToBinaryImage import ConvertToBinaryImage
from ToLines import ToLines
from ToWords import ToWords
from ToCharacters import ToCharacters
from Segmenter import Segmenter
from Modifiers import Modifiers
from MergeImages import MergeImages
from AddSpace import AddSpace
class NepaliOCR(object):
    image=IplImage

    def __init__(self,imagePath=None):
        '''
        constructor
        '''
        if(imagePath):
            self.image=cv.LoadImage(imagePath,cv.CV_LOAD_IMAGE_GRAYSCALE)
        
    def setImage(self,imagePath):
        self.image=cv.LoadImage(imagePath,cv.CV_LOAD_IMAGE_GRAYSCALE)
    
    def run(self):
#        segmentLine=ToLines()
        img=cv.LoadImage("/home/sushil/input.jpg",cv.CV_LOAD_IMAGE_GRAYSCALE)
        
        #Converting to Binary Image
        convertToBinary=ConvertToBinaryImage()
        binaryImg=convertToBinary.convert(img,120)
        cv.ShowImage("Binary image", binaryImg)
        
        #Extracting line segments
        lineSegment=ToLines()
        lineSegment.segment(binaryImg)
        #cv.ShowImage("LineSegment",lineSegment.getLineSegment(3))
        lineImg=lineSegment.getLineSegment(1)
        lineImg2=lineSegment.getLineSegment(2)
        lineImg3=lineSegment.getLineSegment(3)
        totalLines=lineSegment.segment(lineImg)
        
        #for lineNum in range(totalLines):
        #    lineRowRange=lineSegment.getCoordinatesOfLineSegment(lineNum)
        
        charSegment=ToCharacters()            
        Img_split=charSegment.splitDika(binaryImg)
        cv.ShowImage("LineSegment2",Img_split)    
        
#        lineSegment.segment(binaryImg)
#        lineImg=lineSegment.getLineSegment(3)
        
        modifiers=Modifiers()
        #modifiers.locateDika(lineImg)
        modifiers.extractTop(lineImg)
        
        whiteSpace=cv.CreateImage((20,lineImg.height), lineImg.depth, lineImg.nChannels)
        cv.Set(whiteSpace,255)
        cv.ShowImage("White", whiteSpace)
        mergeImage=MergeImages()
        mergeImage2=MergeImages()
        
        mergedImg=mergeImage2.mergeVertically([lineImg,lineImg2])
        addSpace=AddSpace()
        mergedImg=addSpace.addWhiteSpace(lineImg, [10,20,40,50], 10)
        cv.ShowImage("MERGED", mergedImg)

        
if(__name__=="__main__"):
    nepaliOCR=NepaliOCR("/home/sushil/input.jpg")
    nepaliOCR.run()
    cv.WaitKey(0)
    
    