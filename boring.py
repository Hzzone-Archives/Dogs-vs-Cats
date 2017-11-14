import os
import shutil
import os.path as osp
import sys
import cv2
sys.path.insert(0, "/home/hzzone/caffe/python")
import caffe
import numpy as np
def move(source):
	file_list = os.listdir(source)
	os.mkdir(osp.join(source, str(0)))
	os.mkdir(osp.join(source, str(1)))
	for image_file in file_list:
		opt = image_file.split(".")[0]
		opt = 1 if opt=='dog' else 0
		shutil.move(osp.join(source, image_file), osp.join(source, str(opt)))


def resize(source):
	files = os.listdir(source)
	for im_file in files:
		path = osp.join(source, im_file)
		im = cv2.resize(cv2.imread(path), (227, 227))	
		cv2.imwrite(path, im)
		print path

def generate_val(source):
	files = os.listdir(source)
	with open("val.txt", "w") as f:
		for im_file in files:
			path = osp.join(source, im_file)
			f.write(path+"\n")

def predict(source, deploy, caffemodel):
	files = os.listdir(source)
	caffe.set_mode_gpu()
	net = caffe.Net(deploy, caffemodel, caffe.TEST)
	net.blobs['data'].reshape(1, 3, 227, 227)
	with open("predict_result.txt", "w") as f:
		for index, im_file in enumerate(files):
			path = osp.join(source, im_file)
			net.blobs['data'].data[...] = np.transpose(cv2.imread(path), (2, 0, 1))
			output = net.forward()
			result = output['prob'][0].argmax()
			f.write("%s %s\n" % (im_file, 0.995 if result==1 else 0.005))
			print(index, path, result)


if __name__ == "__main__":
    # generate("/home/hzzone/dogs vs cats/test1")
	predict("/home/hzzone/dogs vs cats/test1", "/home/hzzone/Dogs-vs-Cats/deploy.prototxt", "/home/hzzone/Dogs-vs-Cats/snapshot_iter_4900.caffemodel")
