import cv2
import numpy as np
import random
#image location, file location
def toRGB(inimg, outfile): 
    img = cv2.imread(inimg, cv2.IMREAD_COLOR)
    np.savetxt(outfile, img.reshape((3,-1)), fmt="%s", header=str(img.shape))
    
toRGB("hac.png", "foo.txt")