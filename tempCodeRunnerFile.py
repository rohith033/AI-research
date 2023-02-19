rot = 0
# for i in imglist:
#     rot+=5
#     if(rot>=60):
#         rot = 0
#     print(i)
#     input = cv2.imread(f'C:/Users/rohit/Desktop/imageset/oknight/{i}')

#     # Get input size
#     height, width = input.shape[:2]

#     # Desired "pixelated" size
#     w, h = (250,250)
    
#     # Resize input to "pixelated" size
#     temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
#     temp = ndimage.rotate(temp, rot)
#     # Initialize output image
#     output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

#     cv2.imwrite(f'realbluredimages/{i}.jpg',output)