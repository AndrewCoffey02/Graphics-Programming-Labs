import cv2
import numpy as np
from matplotlib import pyplot as plt

# variables for subplot
nrows = 2
ncols = 2

# original figure
img = cv2.imread('ATU.jpg',)
cv2.waitKey(0)

# grayscale figure
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

blur3 = cv2.GaussianBlur(img, (3,3), 0)
blur13 = cv2.GaussianBlur(img,(13,13), 0)

# image dimensions and output
plt.subplot(nrows, ncols, 1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols, 2),plt.imshow(gray_image, cmap = 'gray')
plt.title('Grayscale'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols, 3),plt.imshow(cv2.cvtColor(blur3, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols, 4),plt.imshow(cv2.cvtColor(blur13, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('13x13 Blur'), plt.xticks([]), plt.yticks([])
plt.show()
