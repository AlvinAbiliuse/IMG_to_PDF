from PIL import Image
import os
import send2trash


def splitImages(filename):
	im = Image.open(filename)
	
	newHeight = im.height / 20
	
	total = 0
	for i in range(1, 21):
		if i == 20:
			newImage = im.crop((0, total, im.width,  im.height))
			newImage.save(f'{filename}-20.jpg')
		else:
			newMaxHeight = total + newHeight
			newImage = im.crop((0, total, im.width,  newMaxHeight))
			total += newHeight
			newImage.save(f'{filename}-{i}.jpg')


for i in os.listdir():
	if os.path.isdir(i) == True:
		print(i)
		for j in os.listdir(i):
			splitImages(os.path.join(i, j))
			send2trash.send2trash(os.path.join(i, j))
