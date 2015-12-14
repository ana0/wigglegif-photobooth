import PIL
import images2gif

def make_gifs(devices, rotation, set_id=0):
	''' Stitches jpg captured by camera into gif '''
	images = []
	for device in devices:
		temp = PIL.Image.open("%d-%d-%d.JPG" % (set_id, device[0], device[1]))
		images.append(set_image_rotation(temp, rotation))
	images2gif.writeGif("%d-%d-%d.GIF" % (set_id, device[0], device[1]), images)
	return

# def make_gifs_test():
# 	one = PIL.Image.open("2-2-9.JPG")
# 	two = PIL.Image.open("2-2-10.JPG")
# 	images = [one, two]
# 	images2gif.writeGif("test3.GIF", images)
# 	return

def set_image_rotation(image, rotation):
	''' Rotates pillow image objects according to camera mountint specifications in run()'''
	if rotation == "clockwise":
		return image.rotate(90)
	elif rotation == "counter-clockwise":
		return image.rotate(180)
	else:
		return image
