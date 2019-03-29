import cv2
import progressbar

def correlation(image1, image2):
    res = cv2.matchTemplate(image1, image2, cv2.TM_CCORR_NORMED)
    return res[0,0];


def angle_offset(image1, image2):
	maxCor = -1
	bestRot = 0

	for angle in progressbar.progressbar(range(-10,11)):
		(h, w) = image1.shape[:2];
		M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0) 
		rotated = cv2.warpAffine(image1, M, (h, w)) 

		corr = correlation(rotated, image2)

		if corr > maxCor:
			maxCor = corr
			bestRot = angle
			
	return bestRot;

if __name__ == "__main__":
	cimg = cv2.imread("output_translation_aligned/frame_0.png",0)

	(h, w) = cimg.shape[:2];

	M = cv2.getRotationMatrix2D((w / 2, h / 2), 15, 1.0) 
	rotated = cv2.warpAffine(cimg, M, (h, w)) 

	angle = angle_offset(cimg, rotated)

	print(angle);
