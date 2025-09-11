import cv2
import numpy as np

drawing = False # true if mouse is pressed
ix,iy = -1,-1
font = cv2.FONT_HERSHEY_SIMPLEX
img_origin = cv2.imread('cat.jpg',1)
img = img_origin.copy()
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,img
    img = img_origin.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        txt = 'Mouse Position('+str(x)+','+str(y)+')'+str(img[y,x])
        cv2.putText(img,txt,(30,30), font, 0.5,(255,255,255),2,cv2.LINE_AA)
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)

# mouse callback function
def nothing(x):
    pass
# Create a black image, a window and bind the function to window

cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)


cv2.setMouseCallback('image',draw_circle)
print(img[10, 10])
while(1):
    r = cv2.getTrackbarPos('R','image')
    print(r)
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()

"""




"""