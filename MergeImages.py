'''
Created on Jun 16, 2010

@author: sushil
'''
import cv
class MergeImages:
    
    def __init__(self):
        ''
    def __rotateImage(self,image):
        transImg=cv.CreateImage((image.height,image.width), cv.IPL_DEPTH_8U, 1)    
        cv.Transpose(image, transImg)
        return transImg
    
    def mergeVertically(self,imageList):
        mergedImage=self.__rotateImage(imageList[0])
        for image in imageList[1:]:
            mergedImage=self.__mergeTwoImagesHorizontally(mergedImage, self.__rotateImage(image))
        return self.__rotateImage(mergedImage)
    

    def mergeHorizontally(self,imageList):
        mergedImage=imageList[0]
        for image in imageList[1:]:
            mergedImage=self.__mergeTwoImagesHorizontally(mergedImage, image)
        return mergedImage
    
    def __mergeTwoImagesHorizontally(self,img1,img2):
        (width1,height1)=cv.GetSize(img1)
        (width2,height2)=cv.GetSize(img2)
        newWidth=width1 +width2
        
        mergedImage = cv.CreateImage((newWidth,height1), img1.depth, img1.nChannels)
        mergedImage.origin = img1.origin
        
        # copy the left image
        cv.SetImageROI(mergedImage, (0, 0, width1, height1))
        cv.Copy(img1, mergedImage)
        
        # copy the right image
        cv.SetImageROI(mergedImage, (width1, 0, width1 +width2, height1))
        cv.Copy(img2, mergedImage);
        print "height",height1
        print "width",width1," width2",width2
        cv.ResetImageROI(mergedImage); 
        return mergedImage