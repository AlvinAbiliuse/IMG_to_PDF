import os
from natsort import natsorted
import send2trash
from PIL import Image
import zipfile

def extractFiles():

	# Extracts the zip file into current directory 
	for manga in os.listdir('./Convert'):
		if manga.endswith('.zip'):
			print('Extracting %s...' % '.'.join(manga.split('.')[:-1]))
			zipfile.ZipFile('./Convert/%s' % manga, 'r').extractall(
				'./Convert/%s' % ('.'.join(manga.split('.')[:-1])))
			send2trash.send2trash('./Convert/%s' % manga)

def writePDF():
	global finalList
	# Looping Folders
	for manga in os.listdir('./Convert'):
		if os.path.isdir('./Convert/%s' % manga):
			print('Converting %s...' % manga)
			# All the pages except the first page needs to be added to 
			# a list to be set to append pages when saving
			Pages = natsorted(os.listdir('./Convert/%s' % manga))
			finalList = []
			number = 0
			chunkNum = 0
			# Looping Images
			print(Pages)
			for pages in Pages:
				try:
					print(pages)
					image = Image.open('./Convert/%s/%s' % 
									(manga, pages))
					cPages = image.convert('RGB')
					finalList.append(cPages)
					number += 1
				except:
					pass
				if number != 5:
					pass
				else:
					chunkNum += 1
					print('\n\n')
					# print(finalList)
					finalList[0].save('./Convert/%s.%s.pdf' % (chunkNum, manga), 
						save_all=True, append_images=finalList[1:])
					finalList = []
					number = 0
				if pages == Pages[-1]:
					print('\n\n')
					chunkNum += 1
                    # print(finalList)
					finalList[0].save('./Convert/%s.%s.pdf' % (chunkNum, manga),
						save_all=True, append_images=finalList[1:])
					finalList = []
					number = 0
					
			# send2trash.send2trash('./Convert/%s' % manga)
		else:
			print('%s is not a Zip File or Directory.' % manga)


if __name__ == "__main__":
	extractFiles()
	writePDF()
