import os
from natsort import natsorted
import send2trash
from PIL import Image
import zipfile

def extractFiles():

	# Extracts the zip file into current directory 
	for manga in os.listdir('./Convert'):
		if manga.endswith('.zip'):
			os.makedirs('./Convert/%s' % manga.split('.')[0])
			print('Extracting %s...' % manga.split('.')[0])
			zipfile.ZipFile('./Convert/%s' % manga, 'r').extractall('./Convert/%s' % manga.split('.')[0])
			send2trash.send2trash('./Convert/%s' % manga)

def writePDF():

	# Looping Folders
	for manga in os.listdir('./Convert'):
		if os.path.isdir('./Convert/%s' % manga):
			print('Converting %s...' % manga)

			# All the pages except the first page needs to be added to a list
			# to be set to append pages when saving
			firstPage = 0
			Pages = natsorted(os.listdir('./Convert/%s' % manga))
			finalList = []
			# Looping Images
			for pages in Pages:
				try:
					fileBase = pages.split('.')[0]
					image = Image.open('./Convert/%s/%s' % (manga, pages))
					pages = image.convert('RGB')
					finalList.append(pages)
				except:
					pass
			finalList[0].save('./Converted/%s.pdf' % manga, save_all=True, append_images=finalList[1:])
			send2trash.send2trash('./Convert/%s' % manga)
		else:
			print('%s is not a Zip File or Directory.' % manga)
extractFiles()
writePDF()
