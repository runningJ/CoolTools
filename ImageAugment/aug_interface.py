from data_augmentor import DataAugmentor
import shutil
import os
import cv2

da=DataAugmentor()
def do_augment_folder(folder_path, factor, save_path):
	str_factor = str(factor).replace('.','-')
	image_list = os.listdir(folder_path)
	for i,image_name in enumerate(image_list):
		if i % 1000 == 0:
			print "has been processed %d / %d \r"%(i,len(image_list)),
		image_file = os.path.join(folder_path, image_name)
		if os.path.exists(image_file):
			try:
				res,method = da.rotate_90(image_file,factor)
				if res == None:
					continue
				save_name = os.path.splitext(image_name)[0] + "_"+method +str_factor+".jpg"
				save_file = os.path.join(save_path, save_name)
				cv2.imwrite(save_file,res)
				#res.save(save_file)
			except:
				print("occurs problem {}".format(image_file))
		else:
			print image_file

def process_train(folder_path,save_folder_path,factor):
	folder_list = os.listdir(folder_path)
	for i, each_folder in enumerate(folder_list):
		each_folder_path = os.path.join(folder_path, each_folder)
		print "do %s %d / %d %f" %(each_folder_path,i,len(folder_list),factor)
		each_save_folder = os.path.join(save_folder_path,each_folder)
		if not os.path.exists(each_save_folder):
			os.mkdir(each_save_folder)
		do_augment_folder(each_folder_path,factor,each_save_folder)
		#do_nosie_folder(each_folder_path,each_save_folder)

def generate(folder_path,save_path,factor):
	sub_folder_list = os.listdir(folder_path)
	for sub_folder in sub_folder_list:
		sub_folder_path = os.path.join(folder_path,sub_folder)
		save_folder_path = os.path.join(save_path,sub_folder)
		if not os.path.exists(save_folder_path):
			os.mkdir(save_folder_path)
		process_train(sub_folder_path,save_folder_path,factor)


if __name__=="__main__":
	#generate("/opt/datasets/anti-data/train20190114","/opt/datasets/anti-data/enhancetrain20190114",0.7)
	process_train("/opt/datasets/wineimages/winetrainimages/images","/opt/datasets/wineimages/winetrainimages/augments",-90)
