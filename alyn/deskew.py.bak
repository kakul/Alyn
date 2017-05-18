""" Deskews file after getting skew angle """
import optparse
import numpy as np
import matplotlib.pyplot as plt

from skew_detect import SkewDetect
from skimage import io
from skimage.transform import rotate


class Deskew:

    def __init__(self, input_file, display_image, output_file, r_angle):

        self.input_file = input_file
        self.display_image = display_image
        self.output_file = output_file
        self.r_angle = r_angle
        self.skew_obj = SkewDetect(self.input_file)

    def deskew(self):

        img = io.imread(self.input_file)
        res = self.skew_obj.process_single_file()
        angle = res['Estimated Angle']

        if angle >= 0 and angle <= 90:
            rot_angle = angle - 90 + self.r_angle
        if angle >= -45 and angle < 0:
            rot_angle = angle - 90 + self.r_angle
        if angle >= -90 and angle < -45:
            rot_angle = 90 + angle + self.r_angle

        rotated = rotate(img, rot_angle, resize=True)

        if self.display_image:
            self.display(rotated)

        if self.output_file:
            self.saveImage(rotated*255)

    def saveImage(self, img):
        path = self.skew_obj.check_path(self.output_file)
        io.imsave(path, img.astype(np.uint8))

    def display(self, img):

        plt.imshow(img)
        plt.show()

    def run(self):

        if self.input_file:
            self.deskew()


if __name__ == '__main__':

    parser = optparse.OptionParser()

    parser.add_option(
        '-i',
        '--input',
        default=None,
        dest='input_file',
        help='Input file name')
    parser.add_option(
        '-d', '--display',
        default=None,
        dest='display_image',
        help="display the rotated image")
    parser.add_option(
        '-o', '--output',
        default=None,
        dest='output_file',
        help='Output file name')
    parser.add_option(
        '-r', '--rotate',
        default=0,
        dest='r_angle',
        help='Rotate the image to desired axis',
        type=int)
    options, args = parser.parse_args()
    deskew_obj = Deskew(
        options.input_file,
        options.display_image,
        options.output_file,
        options.r_angle)

    deskew_obj.run()
