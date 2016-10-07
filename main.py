import collections
import os
import cv2
import functools

from map_reduce import mapper as mp


def mapper_func(image_path, save_to_folder):
	image_path.replace(r"\\", '/')
	image_name = "{}.png".format(image_path.split('\\')[-1].split('.')[0])
	saved_image_path = os.path.join(save_to_folder, image_name)
	image = cv2.imread(image_path)
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(saved_image_path,gray_image)
	return saved_image_path


def main():
	SAVE_TO_FOLDER = "./result_images"
	input_image_files = [os.path.join(r"./test_images", i) for i in os.listdir(r"./test_images")]

	## Using MapReduce
	partial_mapper = functools.partial(mapper_func, save_to_folder = SAVE_TO_FOLDER)
	mapper = mp.Mapper(partial_mapper) ## constructor of mapper with map-function
	output_image_files = mapper(input_image_files) ## call the mapper to tasks

	## Using single-processing
	# output_image_files = []
	# for each in input_image_files:
	# 	output_image_files.append(mapper_func(each, SAVE_TO_FOLDER))


if __name__ == "__main__":
	from datetime import datetime
	start_time = datetime.now()
	main()
	print("Cost {} seconds to finish!".format((datetime.now() - start_time).total_seconds()))



