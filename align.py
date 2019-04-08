import cv2
import os
import glob
import numpy as np
import progressbar
from multiprocessing import Pool
from rot_align import angle_offset

PADDING = 100;
 
imgs = glob.glob('imgs/' +'*.tif',recursive=True)
imgs.sort()


stored_circles = [];
target_radius = 0
upper_lim = 1700


def loopBody(data = [0, 1700]):
	print("Frame: " + str(data[0]))
	upper_lim = data[1]

	raw_img = cv2.imread(imgs[data[0]],cv2.IMREAD_COLOR)

	img = cv2.imread(imgs[data[0]],0)

	threshold = 50;
	min_rad = upper_lim - 5;
	max_rad = upper_lim;
	edge_thresh = 40;
	 
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
	                            param1=edge_thresh,param2=edge_thresh,minRadius=int(min_rad),maxRadius=int(max_rad))

	while circles is None:
		min_rad -= 5
		max_rad -= 5

		if (min_rad < target_radius - 25):
			min_rad = upper_lim - 5;
			max_rad = upper_lim;
			threshold *= 0.5;

			if threshold < 10:
				edge_thresh -= 5
				threshold = 50

		circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
	                            param1=edge_thresh,param2=edge_thresh,minRadius=int(min_rad),maxRadius=int(max_rad))

	circles = np.uint16(np.around(circles))

	radius = circles[0,0][2];

	return (radius , circles[0,0]);

target_radius, circ = loopBody()

stored_circles.append(circ)

inputList = [[idx, target_radius] for idx in range(1,len(imgs))]
p = Pool(4)
circles = p.map(loopBody, inputList);

del p

stored_circles = stored_circles + [circ[1] for circ in circles]


target_radius = int(target_radius)+50;


try:  
    os.mkdir("output_translation_aligned")
except:
	pass

with progressbar.ProgressBar(max_value=len(imgs)) as bar:
	for i, file in enumerate(imgs):
		bar.update(i);
		raw_img = cv2.imread(file,cv2.IMREAD_COLOR)
		padded=cv2.copyMakeBorder(raw_img, top=PADDING, bottom=PADDING, left=PADDING, right=PADDING, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
		
		circ = stored_circles[i]

		x = stored_circles[i][0]+PADDING;
		y = stored_circles[i][1]+PADDING;
		adjusted_img = padded[y-target_radius:y+target_radius, x-target_radius:x+target_radius]
		cv2.imwrite("output_translation_aligned/frame_" + str(i) +".png",adjusted_img)


