#! /usr/bin/python3
# IMG_to_PDF.py - extracts zip files and converts images to pdf

from extractFiles import *
from writePDF import *
from convertMultipleFiles import *
import os
import sys

if __name__ == "__main__":
	# exits program if entered argument is not a folder path
	if len(sys.argv) < 2:
		print('Usage: ./IMG_to_PDF.py path')
		sys.exit()
	# exits program if entered argument is not a folder
	if os.path.isdir(sys.argv[1]) != True:
		print(sys.argv[1] + ' is not a folder!')
		sys.exit()
	os.makedirs('./Converted', exist_ok=True)
	convertMultipleFiles(sys.argv[1], './Converted')
	extractFiles(sys.argv[1])
	writePDF(sys.argv[1], './Converted')
