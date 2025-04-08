#! ./env/bin/python3
# IMG_to_PDF.py - deletes the unnecessary files, extracts zip files and converts images to pdf

from extractFiles import *
from writePDF import *
from convertMultipleFiles import *
from cleanPath import *
import os
import sys

def img_to_pdf():
    # exits program if entered argument is not a folder path
    if len(sys.argv) < 2:
        print('Usage: python3 ./IMG_to_PDF.py -c path')
        sys.exit()
    # exits program if entered argument is not a folder
    if os.path.isdir(sys.argv[-1]) != True:
        print(sys.argv[-1] + ' is not a folder!')
        print('Usage: python3 ./IMG_to_PDF.py -c path')
        sys.exit()
    if len(sys.argv) > 2:
        if sys.argv[1] == "--clean" or sys.argv[1] == "-c":
            cleanPath(sys.argv[-1])
    os.makedirs('./Converted', exist_ok=True)
    convertMultipleFiles(sys.argv[-1], './Converted')
    extractFiles(sys.argv[-1])
    writePDF(sys.argv[-1], './Converted')


if __name__ == "__main__":
    img_to_pdf()
