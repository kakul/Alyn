#!/usr/bin/env python
import numpy as np

from skimage import io
from skimage.draw import line_aa
from skimage.transform import rotate

img = io.imread('line.jpg',as_grey=True)
#img = 1-img
for i in range(1,180):
	f1 = rotate(img, i, resize=False) * 255
	io.imsave(str(i)+'.jpg',f1.astype(np.uint8))
