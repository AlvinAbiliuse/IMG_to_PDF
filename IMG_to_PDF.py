#! /usr/bin/python3
# IMG_to_PDF.py - extracts zip files and converts images to pdf

#import os
#from natsort import natsorted
#from send2trash import send2trash
#from PIL import Image
#import zipfile
#import PyPDF2
#import sys

from dependancies import *
import extractFiles

# def extractFiles(path):
#
#	# Extracts the zip file into current directory 
#	for manga in os.listdir(path):
#		if manga.endswith('.zip'):
#			print('Extracting %s...' % '.'.join(manga.split('.')[:-1]))
#			zipfile.ZipFile('./%s/%s' % 
#							(path, manga), 'r').extractall('./%s/%s' % 
#							(path, ('.'.join(manga.split('.')[:-1]))))
#			send2trash('./%s/%s' % (path, manga))



# Loops through all the pages in the folder and creates a PIL object
# for each and then creates multiple files with ~5 pages per pdf.
def writePDF(path, destination):

	# Looping Folders
	for manga in os.listdir(path):

		if os.path.isdir('./%s/%s' % (path, manga)):
			print('Converting %s...' % manga)
			# All the pages except the first page needs to be added to 
			# a list to be set to append pages when saving
			for i in os.listdir('./%s/%s' % (path, manga)):
				if i.endswith('.json'):
					send2trash('./%s/%s/%s' % (path, manga, i))
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
				except Exception:
					print('Error: ' + str(Exception))
				# if statement to make sure that the program saves
				# the last few pages even if number variable is not 5
				if pages == Pages[-1]:
					chunkNum += 1
					if len(finalList) > 1:
						finalList[0].save('./%s/%s.%s.pdf' % 
											(path, chunkNum, manga),
											save_all=True, 
											append_images=finalList[1:])
					else:
						finalList[0].save('./%s/%s.%s.pdf' % 
											(path, chunkNum, manga))
					finalList = []
					number = 0
				else:
					pass

				# creates pdf with 5 pages with the name prefixed with 
				# the checkNum number
				if number != 5:
					pass
				else:
					chunkNum += 1
					finalList[0].save('./%s/%s.%s.pdf' % 
										(path, chunkNum, manga), 
										save_all=True, 
										append_images=finalList[1:])
					finalList = []
					number = 0
			mergeFiles(path, destination, manga, chunkNum)
			send2trash('./%s/%s' % (path, manga))

		else:
			print('%s is not a Zip File or Directory.' % manga)
			pass

# merges the multiple pdf chunks created with writePDF() to ./Converted
def mergeFiles(path, destination,  manga, number):
	mergeObject = PyPDF2.PdfFileMerger()

	for i in range(number):
		mergeObject.append(PyPDF2.PdfFileReader('./%s/%s.%s.pdf' % 
											(path, i+1, manga), 'rb'))
		send2trash('./%s/%s.%s.pdf' % (path, i+1, manga))
	mergeObject.write('%s/%s.pdf' % (destination, manga))

def convertMultipleFiles(path, destination):

	# checks if files inside folder in path is a zip file or a folder
	# and sets multiFIle to 1 if it is.
	for folders in os.listdir(path):
		multiFile = 0
		if os.path.isdir('%s/%s' % (path, folders)):
			for files in os.listdir('%s/%s' % (path, folders)):
				if files.endswith('.zip'):
					multiFile = 1
				elif os.path.isdir('./%s/%s/%s' % 
									(path, folders, files)):
					multiFile = 1
			# if multifile is 1, the funtion extracts and converts
			# files and moves it to appropriate folder after mkdir
			if multiFile == 1:
				print('')
				print('Working on %s: ' % folders)
				try:
					extractFiles('%s/%s' % (path, folders))
				except IsADirectoryError:
					pass
				os.makedirs('%s/%s' % (destination, folders), 
							exist_ok=True) 
				writePDF('%s/%s' % (path, folders), '%s/%s' % 
												(destination, folders))
				send2trash('%s/%s' % (path, folders))
				multiFile = 0
				print('')

	
if __name__ == "__main__":
	# exits program if entered ergument is not a folder path
	if len(sys.argv) < 2:
		print('Usage: ./IMG_to_PDF.py path')
		exit()
	# exits program if entered argument is not a folder
	if os.path.isdir(sys.argv[1]) != True:
		print(sys.argv[1] + ' is not a folder!')
		exit()
	os.makedirs('./Converted', exist_ok=True)
	convertMultipleFiles(sys.argv[1], './Converted')
	extractFiles.extractFiles(sys.argv[1])
	writePDF(sys.argv[1], './Converted')
