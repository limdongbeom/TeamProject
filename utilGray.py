import cv2
import numpy as np

def getContours(img, cThr=[100, 100], showCanny=False):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, cThr[0], cThr[1])



    imgCanny = cv2.resize(imgCanny,(0,0), None,0.5,0.5)


    if showCanny:cv2.imshow('Canny', imgCanny)
