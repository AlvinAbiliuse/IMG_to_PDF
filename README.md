# IMG_to_PDF 

Extracts zip files and converts numbered images into PDF files

USAGE: ./IMG_to_pdf.py path

**Prerequisites**

[Natsort](https://pypi.org/project/natsort/) For natural sorting of numbers  
[send2trash](https://pypi.org/project/Send2Trash/) To delete files that are no longer needed  
[PIL](https://pillow.readthedocs.io/en/stable/) To remove alpha layer from images  
[PyPDF2](https://pypi.org/project/PyPDF2/) To convert images to PDF  

images need to be in a folder and numbered. folders can have subfolders with images 

Tested on Linux only
