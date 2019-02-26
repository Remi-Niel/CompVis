import cv2
import glob
import numpy as np
import progressbar

PADDING = 100;
 
imgs = glob.glob('imgs/' +'*.tif',recursive=True)
imgs.sort()

stored_circles = [];
max_radius = 0;

with progressbar.ProgressBar(max_value=len(imgs)) as bar:
	for idx, file in enumerate(imgs):
		# if idx > 1:
		# 	break;
		bar.update(idx);
		raw_img = cv2.imread(file,cv2.IMREAD_COLOR)

		img = cv2.imread(file,0)

		#img = cv2.medianBlur(gray_img,5)
		cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

		threshold = 100;
		 
		circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
		                            param1=threshold,param2=40,minRadius=0,maxRadius=0)

		while circles is None:
			threshold -= 10;
			circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
			                            param1=threshold,param2=40,minRadius=0,maxRadius=0)	

		circles = np.uint16(np.around(circles))

		stored_circles.append(circles[0,0])

		radius = circles[0,0][2];

		if radius > max_radius:
			max_radius = radius


max_radius = int(max_radius)+50;


fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('eclipse.avi',fourcc,1,(2 * max_radius, 2 * max_radius))

with progressbar.ProgressBar(max_value=len(imgs)) as bar:
	for i, file in enumerate(imgs):
		bar.update(i);
		raw_img = cv2.imread(file,cv2.IMREAD_COLOR)
		padded=cv2.copyMakeBorder(raw_img, top=PADDING, bottom=PADDING, left=PADDING, right=PADDING, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
		
		circ = stored_circles[i]
		# draw the outer circle
		cv2.circle(padded,(circ[0]+PADDING,circ[1]+PADDING),circ[2],(0,255,0),10)
		# draw the center of the circle
		cv2.circle(padded,(circ[0]+PADDING,circ[1]+PADDING),5,(0,0,255),10)

		x = stored_circles[i][0]+PADDING;
		y = stored_circles[i][1]+PADDING;
		adjusted_img = padded[y-max_radius:y+max_radius, x-max_radius:x+max_radius]
		video.write(adjusted_img)

video.release()
cv2.destroyAllWindows()