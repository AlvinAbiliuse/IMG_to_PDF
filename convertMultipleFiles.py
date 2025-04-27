from dependence import *
from writePDF import *
from extractFiles import *

def convertMultipleFiles(path, destination):
    # checks if files inside folder in path is a zip file or a folder
    # and sets multiFIle to 1 if it is.
    curr = os.listdir(path)
    curr.sort()
    for folders in curr:
        multiFile = 0
        if os.path.isdir('%s/%s' % (path, folders)):
            inFiles = os.listdir('%s/%s' % (path, folders))
            inFiles.sort()
            for files in inFIles:
                if files.endswith('.zip') or files.endswith(".cbz"):
                    multiFile = 1
                elif os.path.isdir('./%s/%s/%s' %
                                (path, folders, files)):
                    multiFile = 1
            # if multifile is 1, the funtion extracts and converts
            # files and moves it to appropriate folder after mkdir
            if multiFile == 1:
                print('\nWorking on %s: ' % folders)
                try:
                    extractFiles('%s/%s' % (path, folders))
                except IsADirectoryError:
                    pass
                os.makedirs('%s/%s' % (destination, folders),
                    exist_ok=True)
                writePDF('%s/%s' % (path, folders), '%s/%s' %
                    (destination, folders))
                send2trash('%s/%s' % (path, folders))
                multiFile = 0
                print('')
