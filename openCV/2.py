import cv2
import numpy as np


mg1_path =  "E:\\python\\openCV\\black.jpg"
mg2_path = "E:\\python\\openCV\\circle.jpg"

mg1 = cv2.imread(mg1_path)
mg2 = cv2.imread(mg2_path)

print(mg1 is None,mg2 is None)

xor_image = cv2.bitwise_xor(mg1,mg2,mask=None)

cv2.imshow('univesity logo',xor_image)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()