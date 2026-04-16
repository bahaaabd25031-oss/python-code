import cv2

video_path = r"C:\Users\lenovo\Videos\0118.mp4"

video = cv2.VideoCapture(video_path)

ret = True

while ret:
    ret , frame  = video.read()
    hight , width = frame.shape[:2]
    ratio = 1250/width
    if ret:
        frame = cv2.resize(frame,(1275,int(1080*ratio)))
        cv2.imshow('frame',frame)
        cv2.waitKey(33)
        
video.release()
cv2.destroyAllWindows()