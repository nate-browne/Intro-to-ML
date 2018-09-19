from os import walk, remove, rmdir
from os.path import join, expanduser

def find_and_remove(name, from_home=True):
    '''Helper function for deleting datasets. Some datasets are a bit finnicky
    about loading them in, so this function can be used to remove them before
    redownloading.'''
    removed = False
    path = expanduser('~') if from_home else '/'
    for root, dirs, files in walk(path):
        if name in files:
            remove(join(root, name))
            rmdir(root)
            removed = True

    if not removed:
        print("File not found")
