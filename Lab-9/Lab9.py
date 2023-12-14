import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy

img = cv2.imread('ATU1.jpg', )

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.cornerHarris(gray_scale, 2, 3, 0.04)

imgHarris = copy.deepcopy(img)

threshold = 0.5
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris,(j,i),3,(255, 0, 0),-1)

cv2.imshow('dst', imgHarris)
cv2.waitKey(0)

