import os
import shutil
import os.path as osp
import cv2
def move(source):
	file_list = os.listdir(source)
	dog_files = []
	cat_files = []
	os.mkdir(osp.join(source, str(0)))
	os.mkdir(osp.join(source, str(1)))
	for image_file in file_list:
		opt = image_file.split(".")[0]
		opt = 1 if opt=='dog' else 0
		shutil.move(osp.join(source, image_file), osp.join(source, str(opt)))


def resize(source):
	im = cv2.imread(source)
	im = cv2.resize(im, (227, 227))
	return im

if __name__ == "__main__":
	source = "/Users/HZzone/Downloads/test1"
	files = os.listdir(source)
	for im_file in files:
		path = osp.join(source, im_file)
		im = resize(path)	
		cv2.imwrite(path, im)
		print path
