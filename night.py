# import cv2
# import numpy as np

# # Load the input image
# img = cv2.imread("night/d34e862b-e0ae-4674-b5b6-b83de1f4cc94.jpg")

# # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply gamma correction to adjust the brightness
# gamma = 2.2
# gray_corrected = np.power(gray/255.0, gamma)
# gray_corrected = (gray_corrected*255.0).astype(np.uint8)

# # Apply color tint to simulate a blueish night look
# blue = 20
# green = 0
# red = 20
# color_mask = np.zeros(img.shape, img.dtype)
# color_mask[:] = (blue, green, red)
# night_img = cv2.addWeighted(img, 0.6, color_mask, 0.4, 0)

# # Apply final adjustments to the image
# final_img = cv2.addWeighted(night_img, 0.7, cv2.cvtColor(gray_corrected, cv2.COLOR_GRAY2BGR), 0.3, 0)

# # Save the output image
# cv2.imwrite("night_image.jpg", final_img)
# import cv2
# import numpy as np
# import os 
# # imglist = os.listdir(r'C:\Users\rohit\Desktop\imageset\night')

# # for i in imglist:
# # Load the input image
# img = cv2.imread('chock wheel images with truck/4aac1d4c-82e9-4cab-bcf1-45a0393644eb.jpg')

#     # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Apply gamma correction to adjust the brightness
# gamma = 0.1
# gray_corrected = np.power(gray/255.0, gamma)
# gray_corrected = (gray_corrected*255.0).astype(np.uint8)

# # Apply color tint to simulate a blueish night look
# blue = 20
# green = 0
# red = 30
# color_mask = np.zeros(img.shape, img.dtype)
# color_mask[:] = (blue, green, red)
# night_img = cv2.addWeighted(img, 0.6, color_mask, 0.4, 0)

# # Apply final adjustments to the image to make it darker
# brightness = -40
# contrast = 10
# final_img = np.int16(night_img)
# final_img = np.clip((contrast/127+1)*(final_img-127)+127-brightness, 0, 255)
# final_img = np.uint8(final_img)

# cv2.imwrite(f"test.jpg", final_img)
import cv2
import numpy as np
import os
def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

#location of the image
imglist = os.listdir('chock wheel images with truck')
for x in imglist:
   original = cv2.imread(f'chock wheel images with truck/{x}')
   gamma =  0.5   # change the value here to get different result
   adjusted = adjust_gamma(original, gamma=gamma)
   brightness = 60
   contrast = 40
   final_img = np.int16(adjusted)
   final_img = np.clip((contrast/127+1)*(final_img-127)+127-brightness, 0, 255)
   final_img = np.uint8(final_img)
   cv2.imwrite(f"oknight/{x}.jpg",final_img)

   