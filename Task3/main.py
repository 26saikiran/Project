import cv2
import numpy as np
img=cv2.imread(r"C:\Project\Task3\fruit.jpg")

#color to gray
# cv2.imshow('image',img)
# img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray_img',img_gray)

#rgb color channel
# img[:,:,0]=0
# img[:,:,1]=0
# imgBlue=img[:,:,0]
# imgGreen=img[:,:,1]
# imgRed=img[:,:,2]
# new_img=np.hstack((imgBlue,imgGreen,imgRed))
# cv2.imshow('new_image',new_img)

#resizing
# img_resize= cv2.resize(img,(256,256))
# cv2.imshow('resize_image',img_resize)

#flip
# img_flip=cv2.flip(img,0)
# cv2.imshow("flip_img",img_flip)

#croping using slicing
# img_crop=img[100:300,200:500]
# cv2.imshow("crop_img",img_crop)
#saving image
# cv2.imwrite('fruits_small.png',img_crop)
# img=np.zeros((512,512,3))
#rectangle
# cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=-1)
#circle
# cv2.circle(img,center=(100,400),radius=50,color=(0,0,255),thickness=-1)
#line
# cv2.line(img,pt1=(0,0),pt2=(512,512),thickness=2,color=(0,255,0))
#text
drawing= False
ix=-1
iy=-1
def draw(event,x,y,flags,params):
    global flag,ix,iy
    if event ==4:
        flag =True
        ix=x
        iy=y
    elif event ==0:
        if flag ==True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)
    elif event ==4:
        flag= False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)

cv2.namedWindow(winname='window')
cv2.setMouseCallback("window",draw)
img=np.zeros((512,512,3))
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1)& 0xFF == ord('x'):
        break
cv2.destroyAllWindows()
# cv2.waitKey(0)