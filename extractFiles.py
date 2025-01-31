from dependence import *

def extractFiles(path):

    # Extracts the zip file into current directory 
    for folders in os.listdir(path):
        if folders.endswith('.zip'):
            print(folders)
            name = '.'.join(folders.split('.')[:-1    ])
            print(f'Extracting {name}...')
            zipfile.ZipFile(f'./{path}{folders}', 'r').extractall(
                f'./{path}/{name}')
            # deletes the zip files after extracting
            send2trash(f'./{path}/{folder}')
