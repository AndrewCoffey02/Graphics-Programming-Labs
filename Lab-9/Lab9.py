import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ATU1.jpg', )

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray_scale',gray_scale)
cv2.waitKey(0)

