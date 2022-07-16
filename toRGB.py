import cv2
import numpy as np

img = cv2.imread('hac.png', cv2.IMREAD_COLOR)
# one = np.fromstring(img, dtype=int)

np.savetxt("foo.txt", img.reshape((3,-1)), fmt="%s", header=str(img.shape))

# with open('rgb.txt', 'w') as f:
#     for line in out_arr:
#         f.write(line)
