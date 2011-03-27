'''
Created on May 9, 2010

@author: sushil
'''
#!/usr/local/bin/python
#-*- coding:utf8 -*-

import Image
import os
#from PIL import Image
fileList=os.listdir('.')

for file in fileList: 
    if(file=="jpg2tiff.py" or file=="tifs"):
        continue
    try:
        im = Image.open(file, 'r')
        im.save(file+".tif","TIFF")
        im.show()
    