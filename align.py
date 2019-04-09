import cv2
import os
import glob
import progressbar
from first_frame import first_frame
from other_frames import other_frames
from multiprocessing import Pool
import getopt, sys

# read commandline arguments, first
fullCmdArguments = sys.argv
# - further arguments
argumentList = fullCmdArguments[1:]

unixOptions = "p:m:u:"
gnuOptions = ["padding=", "marge=", "ulim="]  

try:  
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:  
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

PADDING = 100	#Padding added around the aligned images
MARGE = 5		#Error allowed between the radii of circles

imgs = glob.glob('imgs/' +'*.tif',recursive=True)
imgs.sort()

upper_lim = min(cv2.imread(imgs[0],0).shape[:2]) / 2 #Max radius of celestial body

for arg, val in arguments:
	if arg in ("-p", "--padding"):
		PADDING = int(val)
	elif arg in ("-m", "--marge"):
		MARGE = int(val)
	elif arg in ("-u", "--ulim"):
		upper_lim = int(val)

stored_circles = []
stored_COM = []

#Process first frame
target_radius, circ, com = first_frame([imgs[0], upper_lim, upper_lim / 2])

stored_circles.append(circ)
stored_COM.append(com)

#Create input list and process pool
inputList = [[imgs[idx], target_radius+MARGE,2*MARGE] for idx in range(1,len(imgs))]
p = Pool(4)
#Process the other frames in parallel
results = p.map(other_frames, inputList);

#clean up process pool
del p 

stored_circles = stored_circles + [res[1] for res in results]
stored_COM = stored_COM + [res[2] for res in results]

# make dir, continue if it already exists
try:  
    os.mkdir("output_translation_aligned_marked")
except:
	pass

#make dir, continue if it already exists
try:  
    os.mkdir("output_translation_aligned")
except:
	pass

#Create aligned images and store unmarked and marked versions to disk.
#The marked version are rescaled to 800x800
with progressbar.ProgressBar(max_value=len(imgs)) as bar:
	for i, file in enumerate(imgs):
		bar.update(i);
		raw_img = cv2.imread(file,cv2.IMREAD_COLOR)
		padded=cv2.copyMakeBorder(raw_img, top=2*PADDING, bottom=2*PADDING, left=2*PADDING, right=2*PADDING, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
		
		circ = stored_circles[i]

		x = stored_circles[i][0]+2*PADDING;
		y = stored_circles[i][1]+2*PADDING;
		adjusted_img = padded[y-target_radius - PADDING:y+target_radius+PADDING, x-target_radius-PADDING:x+target_radius+PADDING]
		cv2.imwrite("output_translation_aligned/frame_" + "{:05}".format(i) +".png",adjusted_img)


		# draw the outer circle
		cv2.circle(padded,(circ[0]+2*PADDING,circ[1]+2*PADDING),circ[2],(0,255,0),20)
		# draw the center of the circle
		cv2.circle(padded,(circ[0]+2*PADDING,circ[1]+2*PADDING),20,(0,0,255),40)

		com = stored_COM[i]
		cv2.circle(padded,(int(com[1] + 0.5) + 2*PADDING,int(com[0] + 0.5) + 2*PADDING),20,(255,0,255),40)

		adjusted_img = padded[y-target_radius-PADDING:y+target_radius+PADDING, x-target_radius-PADDING:x+target_radius+PADDING]

		cv2.imwrite("output_translation_aligned_marked/frame_" + "{:05}".format(i) +".png",cv2.resize(adjusted_img, (800, 800)))







