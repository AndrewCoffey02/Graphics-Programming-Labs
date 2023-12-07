import cv2
import numpy as np
from matplotlib import pyplot as plt


# figure 1
img = cv2.imread('ATU.jpg',)
cv2.waitKey(0)

# grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur3 = cv2.GaussianBlur(img, (3,3), 0)
blur13 = cv2.GaussianBlur(img,(13,13), 0)

# image dimensions and output
plt.subplot(2, 2, 1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2),plt.imshow(gray_image, cmap = 'gray')
plt.title('Grayscale'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3),plt.imshow(cv2.cvtColor(blur3, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4),plt.imshow(cv2.cvtColor(blur13, cv2.COLOR_BGR2RGB), cmap = 'gray') 
plt.title('13x13 Blur'), plt.xticks([]), plt.yticks([])
plt.show()

# figure 2 
img2 = cv2.imread('ATU.jpg',)
cv2.waitKey(0)
# image 2 grayscale
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#grayscale to blur for detection
img_blur = cv2.GaussianBlur(gray2, (3,3), 0)

sobelx = cv2.Sobel(img_blur,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5) # x direction for sobel detection
sobely = cv2.Sobel(img_blur,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5) # y direction for sobel detection
sobelxy = cv2.Sobel(img_blur,ddepth=cv2.CV_64F,dx=1,dy=1,ksize=5) # x and y direction for sobel detection



# show output of images
plt.subplot(3, 3, 1),plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 2),plt.imshow(gray2, cmap = 'gray')
plt.title('Grayscale'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 3),plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel Horizontal'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 4),plt.imshow(sobely, cmap = 'gray')
plt.title('Sobel Vertical'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 3, 5),plt.imshow(sobelxy, cmap = 'gray')
plt.title('Sobel Vertical'), plt.xticks([]), plt.yticks([])

plt.show()

