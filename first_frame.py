import cv2
from scipy import ndimage
import numpy as np

#data is of form [filename, upper radius limit, radius range]
def first_frame(data):
	print("Processing: " + data[0])

	upper_lim = data[1]
	img = cv2.imread(data[0],0)

	threshold = 40;
	min_rad = upper_lim - 5;
	max_rad = upper_lim;
	edge_thresh = 70;

	hist, thresh = cv2.threshold(img,30,255,cv2.THRESH_BINARY)

	com = ndimage.measurements.center_of_mass(thresh)

	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
	                            param1=edge_thresh,param2=threshold,minRadius=int(min_rad),maxRadius=int(max_rad))

	while circles is None:
		min_rad -= 5
		max_rad -= 5

		if (min_rad < upper_lim - data[2]):
			min_rad = upper_lim - 5;
			max_rad = upper_lim;
			threshold -= 5;

			if threshold < 10:
				edge_thresh -= 5
				threshold = 40

		circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
	                            param1=edge_thresh,param2=threshold,minRadius=int(min_rad),maxRadius=int(max_rad))

	circles = np.uint16(np.around(circles))

	radius = circles[0,0][2];

	return (radius , circles[0,0], com);
