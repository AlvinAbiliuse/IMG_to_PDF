from dependencies import *

def extractFiles(path):

    # Extracts the zip file into current directory 
    for manga in os.listdir(path):
        if manga.endswith('.zip'):
            print('Extracting %s...' % '.'.join(manga.split('.')[:-1]))
            zipfile.ZipFile('./%s/%s' %
                            (path, manga), 'r').extractall('./%s/%s' %
                            (path, ('.'.join(manga.split('.')[:-1]))))
            send2trash('./%s/%s' % (path, manga))

