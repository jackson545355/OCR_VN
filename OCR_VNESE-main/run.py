import pytesseract
import cv2
import os
# from skimage import io
import numpy as np
from imutils import paths
from textblob import TextBlob

inputDir = 'input_image/'
outputDir = 'new_output/'


for filename in os.listdir(inputDir):
    f = os.path.join(inputDir, filename)
    os.system(r'tesseract '+ f +' stdout --oem 3 --psm 0')

for filename in os.listdir(inputDir):
    f = os.path.join(inputDir, filename)
    os.system('tesseract ' + f +' ' + outputDir+'/'+filename+' -l vie --oem 3 --psm 3')
