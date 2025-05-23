from dependence import *

# merges the multiple pdf chunks created with writePDF() to ./Converted
def mergeFiles(path, destination, folder, number):
	mergeObject = PyPDF2.PdfMerger()

	for i in range(number):
		mergeObject.append(PyPDF2.PdfReader('./%s/%s.%s.pdf' %
							(path, i+1, folder), 'rb'))
		os.remove('./%s/%s.%s.pdf' % (path, i+1, folder))
	mergeObject.write('%s/%s.pdf' % (destination, folder))
