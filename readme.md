# Alyn

## Skew detection and correction in images containing text

###Requires

* `numpy`
* `matplotlib`
* `scipy`
* `scikit-image'

###Techniques used

* Canny Edge Detection
* Hough Transform

###Features

* Detect the skew in given images
* View Hough Transform of a given image
* Rotate the image to remove the skew

###Usage

To calculate the skew angle for given image file:

	skew_detect.py -i 'image.jpg'

To save output in a text file add `-o` option:
	
	skew_detect.py