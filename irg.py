import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("installing dependancies")
install("opencv-python")
install("numpy")

import numpy as np
import cv2
import math
import sys
import os

def loadimg(name):
    return cv2.imread(name, cv2.IMREAD_UNCHANGED)

def processFile(path):
    print("processing " + path)
    #convert images to signed double (int16)
    inputFile=loadimg(path)
    ir = inputFile[:,:,0]
    green = inputFile[:,:,1]
    red = inputFile[:,:,2]

    irMat = np.float32(ir)

    gMat = np.float32(green)
    gMat = cv2.subtract(gMat,irMat*.8)


    rMat = np.float32(red)
    rMat = cv2.subtract(rMat,irMat+.65)
   
    output = cv2.normalize(cv2.merge((gMat, rMat, irMat*.6)), None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8UC1)

    path = os.path.split(path)

    cv2.imwrite(os.path.join(path[0], "out-"+path[1]), output)

for i in range (1, len(sys.argv)):
    processFile(sys.argv[i])
