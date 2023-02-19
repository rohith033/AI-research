import cv2 
import os
imglist = os.listdir('C:/Users/rohit/Desktop/imageset/onlychock')
for i in imglist:
    img = cv2.imread(f'C:/Users/rohit/Desktop/imageset/onlychock/{i}')
    h = img.shape[0]
    w = img.shape[1]
    if(h<720 or w<720):
        x = 720-h
        if(x<0):
            x=0
        y = 720 - w
        if(y<0):
            y=0
        rep = cv2.copyMakeBorder(img,x,x,y,y,cv2.BORDER_REPLICATE)
        cv2.imwrite(f'padded/{i}',rep)
    else:
        cv2.imwrite(f'padded/{i}',img)
        
