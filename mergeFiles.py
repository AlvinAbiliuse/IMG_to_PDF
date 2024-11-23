from dependence import *

# merges the multiple pdf chunks created with writePDF() to ./Converted
def mergeFiles(path, destination, folders, number):
	mergeObject = PyPDF2.PdfFileMerger()

	for i in range(number):
		mergeObject.append(PyPDF2.PdfFileReader(
					f'./{path}/{i+1}/{folders}', 'rb'))
		os.remove('./%s/%s.%s.pdf' % f'./{path}/{i+1}/{folders}')
	mergeObject.write(f'{destination}/{folders}')
