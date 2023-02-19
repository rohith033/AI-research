import cv2
import os 
imglist = os.listdir('Tires with Chock wheel on both sides')
for i in imglist:
    img = cv2.imread(f'Tires with Chock wheel on both sides/{i}')
    w = img.shape[0]
    h = img.shape[1]
    if(w<720 or h < 720):
        fac1 = 720/w
        fac2 = 720/h
        img = cv2.resize(img,(int(w * fac1),int(h * fac2)))
        cv2.imwrite(f'Tires with Chock wheel on both sides/{i}',img)