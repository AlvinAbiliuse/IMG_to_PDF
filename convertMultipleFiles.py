from dependence import *
from writePDF import *
from extractFiles import *

def convertMultipleFiles(path, destination):
	# checks if files inside folder in path is a zip file or a folder
	# and sets multiFile to 1 if it is and then calls the function
	# again with new path and destination.
	for folders in os.listdir(path):
		multiFile = 0
		if os.path.isdir(f'{path}/{folders}'):
			for files in os.listdir(f'{path}/{folders}'):
				if files.endswith('.zip'):
					multiFile = 1
				elif os.path.isdir(f'./{path}/{folders}/{files}':
					multiFile = 1
			# if multifile is 1, the function extracts and converts
			# files and moves it to appropriate folder after mkdir
			if multiFile == 1:
				print(f'\nWorking on {folders}: ')
				try:
					extractFiles(f'{path}/{folders}')
				except IsADirectoryError:
					pass
				os.makedirs(f'{destination}/{folders}',
								exist_ok=True)
				writePDF(f'{path}/{folders}',
						f'{destination}/{folders}')
				send2trash(f'{path}/{folders}')
				multiFile = 0
				print('')
