'''
Created on Jun 16, 2010

@author: sushil
'''

import cv
from MergeImages import MergeImages
from opencv.cv import cvZero, cvInvert

class AddSpace:
    
    def __init__(self):
        ''
        
    def addWhiteSpace(self,lineImg,positionList,width):
        mergedImage=lineImg
        splitImage=list()
        mergeImages=MergeImages()
        index=0
        positionList.append(positionList[-1]);
        for position in positionList:
            if(index==0):
                startpos=0
            else:
                startpos=positionList[index-1]
                
            #print position,"-",startpos," ",position-startpos
            
            tempImg=cv.CreateImage((position-startpos,lineImg.height), lineImg.depth, lineImg.nChannels)
            whiteSpace=cv.CreateImage((width,lineImg.height), lineImg.depth, lineImg.nChannels)
            cv.Set(whiteSpace,255)
            #create new image variable

            cv.SetImageROI(lineImg, (startpos,0,position-startpos,lineImg.height)) #startpos, startpos, width, height
            #print cv.GetImageROI(lineImg)
            #print "ht=",tempImg.height
            #print "wd=",tempImg.width
            
            #copy roi in that new image variable
            cv.Copy(lineImg, tempImg)
            
            splitImage.append(tempImg)
            splitImage.append(whiteSpace)
            cv.ResetImageROI(lineImg)
            index=index+1
        cv.ShowImage("SPLIT", splitImage[0])
        merged=mergeImages.mergeHorizontally(splitImage);
        return merged