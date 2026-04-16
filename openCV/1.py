import cv2
import numpy as np

image_path = "C:\\Users\\lenovo\\Pictures\\uni logo.png"


img = cv2.imread(image_path)  



rows,col = img.shape[:2]
q_rows , q_col = rows/4 , col/4
T = np.float32([[1,0,q_col],[0,1,q_rows]])
M = cv2.getRotationMatrix2D((col/2,rows/2),45,1)
img = cv2.warpAffine(img,T,(col,rows))
img = cv2.warpAffine(img,M,(col,rows))

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('univesity logo',img_gray)
cv2.waitKey(0)

img = cv2.imread(image_path)
img = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)

cv2.imshow('univesity logo',img)
cv2.waitKey(0)

"cv2.imwrite('saved.jpg',img_gray)"