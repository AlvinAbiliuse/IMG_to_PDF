from dependence import *
from mergeFiles import *
# Loops through all the pages in the folder and creates a PIL object
# for each and then creates multiple files with ~5 pages per pdf.

def writePDF(path, destination):

	# Looping Folders
	for folders in os.listdir(path):

		if os.path.isdir(f'./{path}/{folders}'):
			print(f'Converting {folders}...')
			# All the pages except the first page needs to be added to 
			# a list to be set to append pages when saving
			#converts webp pages to jpg
			for i in os.listdir(f'./{path}/{folders}'):
				if i.split('.')[-1] == "webp":
					im = Image.open(
						f'./{path}/{folders}/{i}').convert("RGB")
					im.save(f"./{path}/{folders}/{i}.jpg")
					send2trash(f"./{path}/{folders}/{i}")
			Pages = natsorted(os.listdir( f'./{path}/{folders}'))
			finalList = []
			number = 0
			chunkNum = 0
			# Looping Images
			for pages in Pages:
				try:
					image = Image.open(
						f'./{path}/{folders}/{pages}')
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
						finalList[0].save(
								f'./{path}/{chunkNum}/{folders}',
								save_all=True,
								append_images=finalList[1:])
					else:
						finalList[0].save(
								f'./{path}/{chunkNum}/{folders}')
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
					finalList[0].save(
								f'./{path}/{chunkNum}/{folders}', save_all=True, append_images=finalList[1:])
					finalList = []
					number = 0
			mergeFiles(path, destination, folders, chunkNum)
			send2trash(f'./{path}/{folders}')

		else:
			print(f'{folders} is not a Zip File or Directory.')
			pass
