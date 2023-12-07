import cv2
import numpy as np
from matplotlib import pyplot as plt


# figure 1
img = cv2.imread('ATU.jpg',)
cv2.waitKey(0)

# grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blurred images
blur3 = cv2.GaussianBlur(img, (3,3), 0)
blur13 = cv2.GaussianBlur(img,(13,13), 0)

# image output
plt.subplot(2, 2, 1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = 'gray') # main image
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2),plt.imshow(gray_image, cmap = 'gray') # grayscale image
plt.title('Grayscale'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3),plt.imshow(cv2.cvtColor(blur3, cv2.COLOR_BGR2RGB), cmap = 'gray') # blurred image 3x
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4),plt.imshow(cv2.cvtColor(blur13, cv2.COLOR_BGR2RGB), cmap = 'gray') # blurred image 13x
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

# canny detection
canny = cv2.edges = cv2.Canny(img_blur, threshold1=100, threshold2=200)

# show output of images
plt.subplot(2, 3, 1),plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), cmap = 'gray') # main image
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 2),plt.imshow(gray2, cmap = 'gray') # grayscale image
plt.title('Grayscale'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 3),plt.imshow(sobelx, cmap = 'gray') # sobel x image
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 4),plt.imshow(sobely, cmap = 'gray') # sobel y image
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 5),plt.imshow(sobelxy, cmap = 'gray') # sobel x and y image
plt.title('Sobel X and Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 6),plt.imshow(canny, cmap = 'gray') # canny image
plt.title('Canny Detection'), plt.xticks([]), plt.yticks([])
plt.show()

