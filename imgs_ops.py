import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import time

class Images():

    def __init__(self, movement_th, output = False):

        self.MovementThreshold_ = movement_th

        self.output_ = output

        self.capturer_ = cv2.VideoCapture(0)
        time.sleep(0.2)

        _, self.prev_frame_ = self.capturer_.read()
        self.prev_frame_ = cv2.cvtColor(self.prev_frame_, cv2.COLOR_BGR2GRAY)
        self.prev_frame_filtered_ = self.high_pass_filter_(self.prev_frame_)
        self.current_frame_ = None
        self.current_frame_filtered_ = None

    #PUBLIC METHOD

    def update(self):

        #Capture current image
        _, self.current_frame_ = self.capturer_.read()
        self.current_frame_ = cv2.cvtColor(self.current_frame_, cv2.COLOR_BGR2GRAY)
        self.current_frame_filtered_ = self.high_pass_filter_(self.current_frame_)

        #Calculate difference
        diff_total = cv2.absdiff(self.current_frame_filtered_, self.prev_frame_filtered_)

        #Current image is prev image now
        self.prev_frame_filtered_ = self.current_frame_filtered_
        dep_value = self.dep_(diff_total)
        if(dep_value > self.MovementThreshold_ and self.output_):
            print("MOVIMIENTO!")
        #print(dep_value)

        cv2.imshow('current image', diff_total)
        cv2.waitKey(1)
        return dep_value

    #PRIAVTE METHODS

    def high_pass_filter_(self, img):
        data = np.array(img, dtype=float)
        lowpass = ndimage.gaussian_filter(data, 3)
        gauss_highpass = data - lowpass

        kernel = np.ones((2,2),np.uint8)

        #return cv2.dilate(gauss_highpass, kernel, iterations = 1)
        return gauss_highpass

    def dep_(self, img):
        r, c = img.shape
        sum = 0
        for i in range(0, r):
            for j in range(0, c):
                sum = sum + img[i][j]
        return sum / (r * c)
