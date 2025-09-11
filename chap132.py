import cv2
import numpy as np

def nothing(x):
    pass


img1 = cv2.imread('catl.jpg')
img2 = cv2.imread('opencv.png')
dst = cv2.addWeighted(img1,0.9,img2,0.1,0)

cv2.namedWindow('image')
cv2.createTrackbar('weight','image',0,100,nothing)
while(1):
    w = cv2.getTrackbarPos('weight','image')/100.
    print(w)
    dst = cv2.addWeighted(img1,w,img2,1-w,0)
    cv2.imshow('image',dst)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
