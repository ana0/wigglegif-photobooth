import PIL
import images2gif

def make_gifs(devices, rotation, set_id=0):
	''' Stitches jpg captured by camera into gif '''
	print "Making your gif ..."
	images = []
	for device in devices:
		temp = PIL.Image.open("%d-%d-%d.JPG" % (set_id, device[0], device[1]))
		temp = resize_image(temp)
		images.append(set_image_rotation(temp, rotation))
	#images.insert(1, make_composite(images[0], images[1]))
	# temp = make_composite(images[0], images[1])
	# temp.save("test", format="jpeg")
	images2gif.writeGif("%d.GIF" % set_id, images)
	return

def make_gifs_test():
	one = PIL.Image.open("0-2-9.JPG")
	two = PIL.Image.open("0-2-10.JPG")
	images = [one.rotate(90), two.rotate(90)]
	images2gif.writeGif("test5.GIF", images)
	return

def set_image_rotation(image, rotation):
	''' Rotates pillow image objects according to camera mount specifications in run()'''
	if rotation == "clockwise":
		return image.rotate(-90)
	elif rotation == "counter-clockwise":
		return image.rotate(90)
	else:
		return image

def resize_image(image):
	'''scales images down by a factor of 7'''
	size = image.size
	return image.resize((size[0]/7, size[1]/7), resample=PIL.Image.ANTIALIAS)
	# temp = image.resize((size[0]/5, size[1]/5), resample=PIL.Image.ANTIALIAS)
	# temp.save(name, format="jpeg")
	# return

def make_composite(one, two):
	return PIL.Image.blend(one, two, 50)


# test = PIL.Image.open("0-2-10.JPG")
# resize_image(test, "0-2-10")