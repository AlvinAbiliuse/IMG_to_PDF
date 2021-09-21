from PIL import Image
import os
import send2trash


def splitImages(filename):
	im = Image.open(filename)
	
	newHeight = im.height / 20
	
	total = 0
	n = 1
	while True:
		if (im.height - total) < 1500:
			newImage = im.crop((0, total, im.width,  im.height))
			newImage.save(f'{filename}-{n}.jpg')
			break
		else:
			newMaxHeight = total + newHeight
			newImage = im.crop((0, total, im.width,  total + 1500))
			total += 1500
			newImage.save(f'{filename}-{n}.jpg')
			n += 1


for i in os.listdir():
	if os.path.isdir(i) == True:
		print(i)
		for j in os.listdir(i):
			splitImages(os.path.join(i, j))
			send2trash.send2trash(os.path.join(i, j))
