'''
Created on Apr 21, 2010

@author: sushil
'''
import cv

class ConvertToBinaryImage(object):
    def __init__(self):
        '''
        Constructor
        '''
        
    def convert(self,imgIn,threshold):
        binaryImg=cv.CreateImage(cv.GetSize(imgIn), cv.IPL_DEPTH_8U, 1)
        cv.Threshold(imgIn, binaryImg, threshold, 255, cv.CV_THRESH_BINARY)
        return binaryImg