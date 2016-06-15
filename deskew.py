from skew_detect import *

from skimage import img_as_uint 
from skimage.transform import rotate

class Deskew:
	
	def __init__(self, input_file, display_image, output_file, landscape):
		
		self.input_file = input_file
		self.display_image = display_image
		self.output_file = output_file
		self.landscape = landscape
		self.skewObj = Skew(self.input_file)
		
	def deskew(self):
		io.use_plugin('qt')
		img = io.imread(self.input_file)
		res = self.skewObj.process_single_file()
		angle = res['Estimated Angle']

		if angle >= 0 and angle <= 90:
			rot_angle = angle - 90
		if angle >= -90 and angle < 0:
			rot_angle = 90+angle
		if self.landscape:
			rot_angle = rot_angle + 90
		
		rotated = rotate(img, rot_angle, resize = True, preserve_range = True)
		
		if self.display_image:
			self.display(rotated)

		if self.output_file:
			self.saveImage(rotated)

	def saveImage(self,img):
		
		path = self.skewObj.check_path(self.output_file)
		io.imsave(path, img.astype(np.uint8))

	def display(self, img):
		
		plt.imshow(img)
		plt.show()

	def run(self):

		if self.input_file:
			self.deskew()

if __name__ == '__main__':

	parser = optparse.OptionParser()

	parser.add_option('-i', '--input', default = None, dest = 'input_file', help = 'Input file name')
	parser.add_option('-d', '--display', default = None, dest = 'display_image', help = "display the rotated image")
	parser.add_option('-o', '--output', default = None, dest = 'output_file', help = 'Output file name')
	parser.add_option('-l', '--landscape', default = None, dest = 'landscape', help = 'landscape landscape')
	options, args = parser.parse_args()
	deskew_obj = Deskew(options.input_file, options.display_image, options.output_file, options.landscape)
	deskew_obj.run()