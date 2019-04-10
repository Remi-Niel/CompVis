# CompVis
Project for computer vision in which we had to align eclipse images.

align.py can be called and will process .tif files in the "imgs/" folder. It will store the translationally aligned images in "output_translation_aligned_marked/" and "output_translation_aligned/". Where the marked images have indication where circular Hough algorithm found the circle and an indication of the center of mass.

align.py als accepts 3 optional flags -p --padding followed by an int, -u --ulim followed by an int and -m --marge followed by an int. Where padding is simply padding added to the images around the observed object. Ulim determines the maximum radius checked in the first frame while looking for the object. And marge how much the radius of an object after the first frame is allowed to deviate from the radius in the first frame.


rot_align.py can be called after align.py has been called. It reads files from "output_translation_aligned/" and outputs to "output_rotation_aligned/"
