import cv2
import glob
import numpy as np

PADDING = 200;
 


def getBest(img, template, y, x, radius, search_size = 10):
	# cv2.imshow('detected circles',template)
	# cv2.waitKey(0)

	res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
	yT = y + PADDING - radius
	xT = x + PADDING - radius
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res[yT - search_size : yT + search_size, xT - search_size : xT + search_size])

	return y - (max_loc[1] - search_size), x - (max_loc[0] - search_size);




imgs = glob.glob('imgs/' +'*.png',recursive=True)
imgs.sort();
print(imgs)

stored_imgs = [];
adjusted_imgs = [];
stored_circles = [];
max_radius = 0;

for idx, file in enumerate(imgs):
	raw_img = cv2.imread(file,cv2.IMREAD_COLOR)
	border=cv2.copyMakeBorder(raw_img, top=PADDING, bottom=PADDING, left=PADDING, right=PADDING, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
	stored_imgs.append(border)

	gray_img = cv2.imread(file,0)

	img = cv2.medianBlur(gray_img,5)
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

	threshold = 100;
	 
	circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
	                            param1=threshold,param2=40,minRadius=0,maxRadius=0)

	while circles is None:
		threshold -= 1;
		circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
		                            param1=threshold,param2=40,minRadius=0,maxRadius=0)	

	circles = np.uint16(np.around(circles))
	for i in circles[0,0:1]:
	    # draw the outer circle
	    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
	    # draw the center of the circle
	    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

	centerX = circles[0,0][0];
	centerY = circles[0,0][1];
	radius = circles[0,0][2];

	if radius > max_radius:
		max_radius = radius

	if idx != 0:
		prevY += PADDING
		prevX += PADDING
		template = stored_imgs[idx - 1][prevY - max_radius : prevY + max_radius, prevX - max_radius : prevX + max_radius]
		centerY, centerX = getBest(border, template, centerY, centerX, max_radius);

	circles[0,0][0] = centerX;
	circles[0,0][1] = centerY;
	
	stored_circles.append(circles[0,0])
	
	prevX = centerX;
	prevY = centerY;

	#cv2.imshow('detected circles',cimg)
	#cv2.waitKey(0)

max_radius = int(max_radius) + 50;


for i in range(len(stored_imgs)):
	x = stored_circles[i][0]+PADDING;
	y = stored_circles[i][1]+PADDING;
	adjusted_imgs.append(stored_imgs[i][y-max_radius:y+max_radius, x-max_radius:x+max_radius])
	print(adjusted_imgs[i].shape)

# for im in adjusted_imgs:
# 	cv2.imshow('adjusted',im)
# 	cv2.waitKey(0)

width , height, channels = adjusted_imgs[0].shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('eclipse_with.avi',fourcc,1,(width, height))

for im in adjusted_imgs:
	# cv2.imshow('detected circles',im)
	# cv2.waitKey(0)

	video.write(im);

video.release()
cv2.destroyAllWindows()