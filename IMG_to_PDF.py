import os
from natsort import natsorted
import send2trash
from PIL import Image
import zipfile
import PyPDF2

def extractFiles(path):

	# Extracts the zip file into current directory 
	for manga in os.listdir(path):
		if manga.endswith('.zip'):
			print('Extracting %s...' % '.'.join(manga.split('.')[:-1]))
			zipfile.ZipFile('./%s/%s' % (path, manga), 'r').extractall(
				'./%s/%s' % (path, ('.'.join(manga.split('.')[:-1]))))
			send2trash.send2trash('./%s/%s' % (path, manga))



# Loops through all the pages in the folder and creates a PIL object
# for each and then creates multiple files with ~5 pages per pdf.
def writePDF(path, destination):

	# Looping Folders
	for manga in os.listdir(path):
		if os.path.isdir('./%s/%s' % (path, manga)):
			print('Converting %s...' % manga)
			# All the pages except the first page needs to be added to 
			# a list to be set to append pages when saving
			Pages = natsorted(os.listdir('./%s/%s' % (path, manga)))
			finalList = []
			number = 0
			chunkNum = 0
			# Looping Images


			for pages in Pages:
				try:
					image = Image.open('./%s/%s/%s' % 
									(path, manga, pages))
					cPages = image.convert('RGB')
					finalList.append(cPages)
					number += 1
				except:
					pass

				# if statement to make sure that the program saves the last few
				# pages even if number variable is not 5
				if pages == Pages[-1]:
					chunkNum += 1
					if len(finalList) > 1:
						finalList[0].save('./%s/%s.%s.pdf' % (path, chunkNum, manga),
										save_all=True, append_images=finalList[1:])
					else:
						finalList[0].save('./%s/%s.%s.pdf' % (path, chunkNum, manga))
					finalList = []
					number = 0
				else:
					pass

				# creates pdf with 5 pages with the name prefixed with the checkNum
				# number
				if number != 5:
					pass
				else:
					chunkNum += 1
					finalList[0].save('./%s/%s.%s.pdf' % (path, chunkNum, manga), 
								save_all=True, append_images=finalList[1:])
					finalList = []
					number = 0

		else:
			print('%s is not a Zip File or Directory.' % manga)
		send2trash.send2trash('./%s/%s' % (path, manga))
		mergeFiles(path, destination, manga, chunkNum)

# merges the multiple pdf chunks created with writePDF() to ./Converted
def mergeFiles(path, destination,  manga, number):
	mergeObject = PyPDF2.PdfFileMerger()

	for i in range(number):
		mergeObject.append(PyPDF2.PdfFileReader('./%s/%s.%s.pdf' % (path, i+1, manga), 'rb'))
		send2trash.send2trash('./%s/%s.%s.pdf' % (path, i+1, manga))
	mergeObject.write('./Converted/%s.pdf' % manga)

if __name__ == "__main__":
	extractFiles('./Convert')
	writePDF('./Convert', './Converted')

