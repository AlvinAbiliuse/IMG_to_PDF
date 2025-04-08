# IMG_to_PDF.py

Extracts zip files and converts numbered images into PDF files

INSTRUCTONS:

only required once:
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ deactivate

then enter the command below everytime
$ ./IMG_to_PDF.py <path>

usage: python3 ./IMG_to_pdf.py -c path

**Prerequisites**

[Natsort](https://pypi.org/project/natsort/) For natural sorting of numbers  
[send2trash](https://pypi.org/project/Send2Trash/) To delete files that are no longer needed  
[PIL](https://pillow.readthedocs.io/en/stable/) To remove alpha layer from images  
[PyPDF2](https://pypi.org/project/PyPDF2/) To convert images to PDF

images need to be in a folder and numbered. folders can have subfolders with images

Tested on Linux only
