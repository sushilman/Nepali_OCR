'''
Created on Apr 21, 2010

@author: sushil
'''

#calculates max,min pixels for row Image

import cv
import array

class PixelCounter(object):
    countArray_H=array.array('i')
    countArray_V=array.array('i')
    
    def __init__(self):
        self.countArray_H=array.array('i')
        self.countArray_V=array.array('i')
        '''
        Constructor
        '''

    def __countHorizontally(self,img,pixelValue):
        rows=img.height
        countArr=array.array('i')
        for row in range(rows):
            count=self.__countPixelsInRow(img, row, pixelValue)
#            if(count>self.maxPixelCount):
#                self.maxPixelCount=count
            countArr.insert(row, count)
#        self.countArrayRow=countArr
        return countArr
    
    def __countVertically(self,img,pixelValue):
        tempImg=cv.CreateImage((img.height,img.width), cv.IPL_DEPTH_8U, 1)    
        cv.Transpose(img, tempImg)
        countArr=self.__countHorizontally(tempImg, pixelValue)
        return countArr
    
    #returns list of x or y coordinates of n count of pixels in row or col resp
    def getOccurredPositionList(self,countArr,count):
        countList=list()
        counter=0;
        for eachCount in countArr:
            if(eachCount==count or eachCount==count-1 or eachCount==count+1):
                countList.append(counter)
            counter=counter+1
        return countList

    def getMostOccurred(self,countArr):
        #countArr=self.countArray_H
        #countArr=self.getCountArr_H(img, pixelValue)
        maxCount=0
        mostOccurringNumber=0
        for x in countArr:
            if(x!=0 and maxCount<countArr.count(x)):
                maxCount=countArr.count(x)
                mostOccurringNumber=x
        return mostOccurringNumber
                
#    def getMostOccurredAt(self,countArr,mode):
#        #countArr=self.getCountArr_H(img, pixelValue)
#        #mode=self.getMostOccurred(countArr)
#        countList=list()
#        rowNum=0;
#        for count in countArr:
#            if(count==mode):
#                countList.append(rowNum)
#            rowNum=rowNum+1
#        return countList      
    
    def getCountArr_H(self,img,pixelValue):
        self.countArray_H = self.__countHorizontally(img, pixelValue)
        return self.countArray_H

        
    def getMax(self,countArr):
        return max(max(countArr) for l in countArr)
    
    def getMin(self,countArr):
        min=self.getMax(countArr)
        for l in countArr:
            if(l!=0 and l < min):
                min=l
        return min
    
    #returns list
#    def getMaxAt(self,countArr,max):
#        countList=list()
#        counter=0;
#        for count in countArr:
#            if(count==max):
#                countList.append(counter)
#            counter=counter+1
#        return countList
            
    #returns list 
#    def getMinAt(self,countArr,min):
#        countList=list()
#        counter=0;
#        for count in countArr:
#            if(count==min or count==min+1 or count==min-1): #+1 or -1 is also counted as min
#                countList.append(counter)
#            counter=counter+1
#        return countList
        
    def getCountArr_V(self,img,pixelValue):
        self.countArray_V = self.__countVertically(img, pixelValue)
        return self.countArray_V
        
    def __countPixelsInRow(self,img,rowNum,pixelValue):
        count=0
        for x in range(img.width):
            if(cv.Get2D(img, rowNum, x)[0]==pixelValue):
                count=count+1    
        return count
