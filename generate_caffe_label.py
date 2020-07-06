import os
import random

def generate_image_label(folder_path,save_file):
	'''
	this is used to generate label
	'''
	sub_folder_list = os.listdir(folder_path)
	fw = open(save_file,'a+')
	for i,sub in enumerate(sub_folder_list):
		label = i
		sub_path = os.path.join(folder_path,sub)
		images_list = os.listdir(sub_path)
		for image in images_list:
			image_file = os.path.join(sub_path,image)
			each_line = image_file+"\n"
			fw.write(each_line)

def generate_folder_label(folder_path,save_file):
	sub_folder_list = os.listdir(folder_path)
	fw = open(save_file,'a+')
	for i,sub in enumerate(sub_folder_list):
		label = i
		each_line = sub+" "+str(label)+"\n"
		fw.write(each_line)


def generate_label_accord_file(folder_path,save_file,reference_file):
	reference_list = open(reference_file).read().split('\n')
	reference_list.remove("")
	reference_dict = {}
	for each_line in reference_list:
		sub,label = each_line.split()
		reference_dict[sub] = label
	fa = open(save_file,'a+')
	sub_folder_list = os.listdir(folder_path)
	for i,sub in enumerate(sub_folder_list):
		label = reference_dict[sub]
		sub_path = os.path.join(folder_path,sub)
		images_list = os.listdir(sub_path)
		for image in images_list:
			image_file = os.path.join(sub_path,image)
			each_line = image_file+" "+str(label)+"\n"
			fa.write(each_line)


def generate_label_accord_file_two(folder_path,save_file,reference_file):
	reference_list = open(reference_file).read().split('\n')
	reference_list.remove("")
	reference_dict = {}
	for each_line in reference_list:
		sub,label = each_line.split()
		reference_dict[sub] = label
	fa = open(save_file,'a+')
	sub_folder_list = os.listdir(folder_path)
	for i,sub in enumerate(sub_folder_list):
		label = reference_dict[sub]
		sub_path = os.path.join(folder_path,sub)
		sub_sub_folder_list = os.listdir(sub_path)
		for sub_sub_folder in sub_sub_folder_list:
			sub_sub_folder_path = os.path.join(sub_path,sub_sub_folder)
			images_list = os.listdir(sub_sub_folder_path)
			for image in images_list:
				image_file = os.path.join(sub_sub_folder_path,image)
				each_line = image_file+" "+str(label)+"\n"
				fa.write(each_line)

def split_train_val_file(file_path,save_path,number):
	fo = open(file_path)
	label_list = fo.read().split("\n")
	random.shuffle(label_list)
	extract_list = random.sample(label_list,number)
	ret = list(set(label_list) ^ set(extract_list))
	train_file = os.path.join(save_path,'train.txt')
	ftrain = open(train_file,'w')
	for each in ret:
		if each != "":
			each_line = each +'\n'
			ftrain.write(each_line)
	val_file = os.path.join(save_path,'val.txt')
	fval = open(val_file,'w')
	for each in extract_list:
		if each != "":
			each_line = each +'\n'
			fval.write(each_line)

def split_train_val_file_versoin(file_path,save_path,number):
	fo = open(file_path)
	label_list = fo.read().split("\n")
	extract_list_negative = []
	while len(extract_list_negative) < number:
		extract_one = random.sample(label_list,1)
		element_one = extract_one[0]
		if element_one in extract_list_negative:
			continue
		else:
			image_file,label = element_one.split()
			if label == "0":
				extract_list_negative.append(element_one)
	
	extract_list_positive = []
	while len(extract_list_positive) < number:
		extract_one = random.sample(label_list,1)
		element_one = extract_one[0]
		if element_one in extract_list_positive:
			continue
		else:
			image_file,label = element_one.split()
			if label == "1":
				extract_list_positive.append(element_one)

	extract_list_negative.extend(extract_list_positive)
	ret = list(set(label_list) ^ set(extract_list_negative))
	train_file = os.path.join(save_path,'train.txt')
	ftrain = open(train_file,'w')
	for each in ret:
		if each != "":
			each_line = each +'\n'
			ftrain.write(each_line)
	val_file = os.path.join(save_path,'val.txt')
	fval = open(val_file,'w')
	for each in extract_list_negative:
		if each != "":
			each_line = each +'\n'
			fval.write(each_line)

def generate_accord_file(folder_path,file_path,save_file):
	reference_list = open(file_path).read().split('\n')
	reference_list.remove("")
	fo = open(save_file,'w')
	for idx,each_line in enumerate(reference_list):
		if idx %100 == 0:
			print("has processed is {}/{}".format(idx,len(reference_list)))
		sub_folder_path = os.path.join(folder_path,each_line)
		image_list = os.listdir(sub_folder_path)
		for image in image_list:
			line_write = os.path.join(each_line,image) + " " +str(idx) + '\n'
			fo.write(line_write)



if __name__=="__main__":
	#generate_folder_label("/home/jl/datasets/oilrecognition/train",
	#	"/home/jl/datasets/oilrecognition/list.txt")
	generate_label_accord_file("/home/jl/datasets/oilrecognition/val",
		"/home/jl/datasets/oilrecognition/val.txt",
		"/home/jl/datasets/oilrecognition/list.txt")
	
	#split_train_val_file("/opt/datasets/maskimages/all.txt",
	#	"/opt/datasets/maskimages/",20000)
	#generate_accord_file("/opt/datasets/readwinelibrary","/home/nemo/code/winetrain_triplet/class.txt","/home/nemo/code/winetrain_triplet/train_val.txt")
