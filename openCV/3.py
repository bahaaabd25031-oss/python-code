import cv2
import numpy as np

image_path = "C:\\Users\\lenovo\\Pictures\\uni logo.png"


img = cv2.imread(image_path,0) 

equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))

cv2.imshow('univesity logo',res)
cv2.waitKey(0)