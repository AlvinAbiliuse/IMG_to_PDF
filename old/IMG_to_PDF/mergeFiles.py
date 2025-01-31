from dependence import *

# merges the multiple pdf chunks created with writePDF() to ./Converted
def mergeFiles(path, destination,  manga, number):
	mergeObject = PyPDF2.PdfFileMerger()

	for i in range(number):
		mergeObject.append(PyPDF2.PdfFileReader('./%s/%s.%s.pdf' %
							(path, i+1, manga), 'rb'))
		os.remove('./%s/%s.%s.pdf' % (path, i+1, manga))
	mergeObject.write('%s/%s.pdf' % (destination, manga))
