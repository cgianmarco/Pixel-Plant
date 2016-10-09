from PIL import Image
import glob
import shutil
import os
from random import shuffle

file_names = glob.glob("random/*.jpg")
if os.path.exists('random_out'):
	shutil.rmtree('random_out')
os.makedirs('random_out')

print len(file_names)
shuffle(file_names)

size = 100,100

for x in file_names[0:30]:
	image_file = Image.open(x)
	x = 'random_out'+x[6:]

	# image_file = image_file.resize((160, 120), Image.ANTIALIAS)
	image_file.thumbnail(size, Image.ANTIALIAS)
	image_file.save(x, optimize=True, quality=95)
	# new_file_name = x.replace("type2", "resType2")
	# image_file.save(new_file_name, optimize=True, quality=95)
	image_file_flipped = image_file.transpose(Image.FLIP_LEFT_RIGHT)
	new_file_name = x.replace(".jpg", "_flipped.jpg")
	image_file_flipped.save(new_file_name, optimize=True, quality=95)

	image_file_updown = image_file.transpose(Image.FLIP_TOP_BOTTOM)
	new_file_name = x.replace(".jpg", "_updown.jpg")
	image_file_updown.save(new_file_name, optimize=True, quality=95)

	image_file_updown_flipped = image_file_flipped.transpose(Image.FLIP_TOP_BOTTOM)
	new_file_name = x.replace(".jpg", "_flipped_updown.jpg")
	image_file_updown_flipped.save(new_file_name, optimize=True, quality=95)
	
	print x




