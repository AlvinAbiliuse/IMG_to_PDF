#! /env/bin/python3

from dependence import *

def extractFiles(path):

	# Extracts the zip file into current directory 
	for folder in os.listdir(path):
		if folder.endswith('.zip') or folder.endswith(".cbz"):
			print('Extracting %s...' % '.'.join(folder.split('.')[:-1]))
			zipfile.ZipFile('./%s/%s' %
							(path, folder), 'r').extractall('./%s/%s' %
							(path, ('.'.join(folder.split('.')[:-1]))))
			# deletes the zip files after extracting
			send2trash('./%s/%s' % (path, folder))


if __name__ == "__main__":
    extractFIles("./CC")
