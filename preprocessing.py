# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from PIL import Image

from resizeimage import resizeimage
import glob

source_dir = 'C:\\Users\\Tuan Pham\\Capstone\\images\\'
target_dir = 'C:\\Users\\Tuan Pham\\Capstone_Data\\'

def resize_dataset(className):
    ind = 0
#    image_list = []
    for filename in glob.glob(source_dir + str(className) + '\*.JPG'): #assuming gif
        im=Image.open(filename)
        #cover = resizeimage.resize_cover(im, [256, 256])
        #cover = resizeimage.resize_contain(im, [256, 256])
        thumbnail = resizeimage.resize_thumbnail(im, [512, 512])
        thumbnail = thumbnail.save(target_dir + str(className) + '\\' + str(className) + '_' + str(ind) + '.jpeg', im.format)
        ind = ind + 1
        #image_list.append(im)
        
resize_dataset("algebra")
print("\n--- Algebra ---")

resize_dataset("calculus")
print("\n--- Calculus ---")

resize_dataset("geometry")
print("\n--- Geometry ---")

resize_dataset("trigonometry")
print("\n--- Trigonometry---")
    